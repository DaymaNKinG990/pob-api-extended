from __future__ import annotations

from typing import TYPE_CHECKING

from lxml.etree import Element, fromstring

from pobapi import config, constants, models, stats

if TYPE_CHECKING:
    from pobapi.build_builder import BuildBuilder
from pobapi.build_modifier import BuildModifier
from pobapi.builders import ConfigBuilder, ItemSetBuilder, StatsBuilder
from pobapi.decorators import listify, memoized_property
from pobapi.exceptions import ParsingError, ValidationError
from pobapi.interfaces import BuildParser
from pobapi.parsers import DefaultBuildParser
from pobapi.types import ItemSlot
from pobapi.util import (
    _fetch_xml_from_import_code,
    _fetch_xml_from_url,
    _get_stat,
    _get_text,
    _skill_tree_nodes,
    clean_pob_formatting,
)
from pobapi.validators import InputValidator, XMLValidator

"""API for PathOfBuilding's XML export format."""

__all__ = ["PathOfBuildingAPI", "from_url", "from_import_code"]


class PathOfBuildingAPI:
    """Instances of this class are single Path Of Building pastebins.

    :param xml: Path of Building XML document in byte format or Element.

    .. note:: XML must me in byte format, not string format.
        This is required because the XML contains encoding information.

    .. note:: To instantiate from pastebin.com links or import codes, use
        :func:`~pobapi.api.from_url` or
        :func:`~pobapi.api.from_import_code`, respectively."""

    def __init__(
        self,
        xml: bytes | Element,
        parser: BuildParser | None = None,
    ):
        """Initialize PathOfBuildingAPI.

        :param xml: XML content as bytes or Element.
        :param parser: Optional parser implementation.
        :raises: ParsingError, ValidationError
        """
        if isinstance(xml, bytes):
            InputValidator.validate_xml_bytes(xml)
            try:
                self.xml = fromstring(xml)
            except Exception as e:
                raise ParsingError("Failed to parse XML") from e
        elif isinstance(xml, Element):
            self.xml = xml
        else:
            raise ValidationError("xml must be bytes or Element")

        XMLValidator.validate_build_structure(self.xml)
        self._parser = parser or DefaultBuildParser()
        self._build_info: dict | None = None
        self._is_mutable = False  # Flag to track if build has been modified
        self._pending_items: list[models.Item] = []  # Items to add on serialization
        self._pending_item_sets: dict[int, models.Set] = {}  # Modified item sets
        self._pending_skill_groups: list[models.SkillGroup] = []  # Added skill groups
        self._modifier = BuildModifier(self)  # Build modification handler

    @property
    def _build_info_cache(self) -> dict:
        """Cache for build info to avoid repeated parsing."""
        if self._build_info is None:
            self._build_info = self._parser.parse_build_info(self.xml)
        return self._build_info

    @memoized_property
    def class_name(self) -> str:
        """Get a character's class.

        :return: Character class.
        :rtype: :class:`str`"""
        result = self._build_info_cache["class_name"]
        return result if result is not None else ""

    @memoized_property
    def ascendancy_name(self) -> str | None:
        """Get a character's ascendancy class.

        :return: Character ascendancy class, if ascended.
        :rtype: :data:`~typing.Optional`\\[:class:`str`]"""
        return self._build_info_cache["ascendancy_name"]  # type: ignore[no-any-return]

    @memoized_property
    def level(self) -> int:
        """Get a character's level.

        :return: Character level.
        :rtype: :class:`int`"""
        level_str = self._build_info_cache["level"]
        return int(level_str) if level_str else 1

    @memoized_property
    def bandit(self) -> str | None:
        """Get a character's bandit choice.

        :return: Character bandit choice.
        :rtype: :data:`~typing.Optional`\\[:class:`str`]"""
        return self._build_info_cache["bandit"]  # type: ignore[no-any-return]

    @memoized_property
    def active_skill_group(self) -> models.SkillGroup:
        """Get a character's main skill setup.

        :return: Main skill setup.
        :rtype: :class:`~pobapi.models.SkillGroup`"""
        main_socket_group = self._build_info_cache["main_socket_group"]
        index = int(main_socket_group) - 1 if main_socket_group else 0
        return self.skill_groups[index]  # type: ignore[no-any-return]

    @memoized_property
    def stats(self) -> stats.Stats:
        """Namespace for character stats.

        :return: Character stats.
        :rtype: :class:`~pobapi.stats.Stats`"""
        return StatsBuilder.build(self.xml)

    @memoized_property
    @listify
    def skill_groups(self) -> list[models.SkillGroup]:  # type: ignore[misc]
        """Get a character's skill setups.

        :return: Skill setups.
        :rtype: :class:`~typing.List`\\[:class:`~pobapi.models.SkillGroup`]"""
        # First yield pending skill groups (from add_skill calls)
        if hasattr(self, "_pending_skill_groups"):
            yield from self._pending_skill_groups

        # Then yield skill groups from XML
        skills_element = self.xml.find("Skills")
        if skills_element is None:
            return

        # Handle new structure with SkillSet (Path of Building 2.0+)
        # Check if there are SkillSet elements
        skill_sets = skills_element.findall("SkillSet")
        if skill_sets:
            # New structure: Skills -> SkillSet -> Skill
            for skill_set in skill_sets:
                for skill in skill_set.findall("Skill"):
                    enabled = skill.get("enabled") == "true"
                    label = skill.get("label")
                    active = (
                        int(skill.get("mainActiveSkill"))
                        if skill.get("mainActiveSkill")
                        and skill.get("mainActiveSkill") != "nil"
                        else None
                    )
                    abilities = self._abilities(skill)
                    yield models.SkillGroup(enabled, label, active, abilities)
        else:
            # Old structure: Skills -> Skill (direct)
            for skill in skills_element.findall("Skill"):
                enabled = skill.get("enabled") == "true"
                label = skill.get("label")
                main_active = skill.get("mainActiveSkill")
                active = (
                    int(main_active) if main_active and main_active != "nil" else None
                )
                abilities = self._abilities(skill)
                yield models.SkillGroup(enabled, label, active, abilities)

    @memoized_property
    def active_skill(self) -> models.Gem | models.GrantedAbility | None:
        """Get a character's main skill.

        :return: Main skill.
        :rtype: :data:`~typing.Union`\\[:class:`~pobapi.models.Gem`,
            :class:`~pobapi.models.GrantedAbility`]"""
        if self.active_skill_group.active is None:
            return None
        index = self.active_skill_group.active - 1
        # Short-circuited for the most common case
        if not index:
            return self.active_skill_group.abilities[index]  # type: ignore[no-any-return]
        # For base skills on Vaal skill gems,
        # the offset is as if the base skill gems would also be present.
        # Simulating this is easier than calculating the adjusted offset.
        active = [gem for gem in self.active_skill_group.abilities if not gem.support]
        duplicate = []
        for gem in active:
            if gem.name.startswith("Vaal"):
                duplicate.append(gem)
            duplicate.append(gem)
        if len(duplicate) > 1 and duplicate[index] == duplicate[index - 1]:
            gem = duplicate[index - 1]
            name = constants.VAAL_SKILL_MAP.get(
                gem.name, gem.name.rpartition("Vaal ")[2]
            )
            return models.Gem(name, gem.enabled, gem.level, gem.quality, gem.support)
        return self.active_skill_group.abilities[index]  # type: ignore[no-any-return]

    @memoized_property
    @listify
    def skill_gems(self) -> list[models.Gem]:  # type: ignore[misc]  # Added for convenience
        """Get a list of all skill gems on a character.

        .. note: Excludes abilities granted by items.

        :return: Skill gems.
        :rtype: :class:`~typing.List`\\[:class:`~pobapi.models.Gem`]"""
        skills_element = self.xml.find("Skills")
        if skills_element is None:
            return []

        # Handle new structure with SkillSet (Path of Building 2.0+)
        skill_sets = skills_element.findall("SkillSet")
        if skill_sets:
            # New structure: Skills -> SkillSet -> Skill
            for skill_set in skill_sets:
                for skill in skill_set.findall("Skill"):
                    if not skill.get("source"):
                        for ability in self._abilities(skill):
                            if isinstance(ability, models.Gem):
                                yield ability
        else:
            # Old structure: Skills -> Skill (direct)
            for skill in skills_element.findall("Skill"):
                if not skill.get("source"):
                    for ability in self._abilities(skill):
                        if isinstance(ability, models.Gem):
                            yield ability

    @memoized_property
    def active_skill_tree(self) -> models.Tree:
        """Get a character's current skill tree.

        :return: Skill tree.
        :rtype: :class:`~pobapi.models.Tree`"""
        index = int(self.xml.find("Tree").get("activeSpec")) - 1
        return self.trees[index]  # type: ignore[no-any-return]

    @memoized_property
    @listify
    def trees(self) -> list[models.Tree]:  # type: ignore[misc]
        """Get a list of all skill trees of a character.

        :return: Skill trees.
        :rtype: :class:`~typing.List`\\[:class:`~pobapi.models.Tree`]"""
        for spec in self.xml.find("Tree").findall("Spec"):
            url_elem = spec.find("URL")
            url = (
                url_elem.text.strip("\n\r\t")
                if url_elem is not None and url_elem.text
                else ""
            )

            # If URL is empty, try to get nodes from Nodes element
            nodes_elem = spec.find("Nodes")
            if url:
                nodes = _skill_tree_nodes(url)
            elif nodes_elem is not None:
                # Extract nodes from XML Nodes element
                nodes = [
                    int(node_elem.get("id")) for node_elem in nodes_elem.findall("Node")
                ]
            else:
                nodes = []
            # Socket elements can be either:
            # 1. Direct children of Spec: <Spec><Socket .../></Spec>
            # 2. Inside Sockets element: <Spec><Sockets><Socket .../></Sockets></Spec>
            sockets_element = spec.find("Sockets")
            if sockets_element is not None:
                socket_elements = sockets_element.findall("Socket")
            else:
                socket_elements = spec.findall("Socket")
            sockets = {
                int(s.get("nodeId")): int(s.get("itemId")) for s in socket_elements
            }
            yield models.Tree(url, nodes, sockets)

    @memoized_property
    def keystones(self) -> models.Keystones:
        """Namespace for a character's keystones.

        Iterate over the keystones property to only get active keystones.

        :return: Keystones.
        :rtype: :class:`~pobapi.models.Keystones`"""
        # Get all field names from Keystones dataclass
        from dataclasses import fields

        keystone_fields = {f.name for f in fields(models.Keystones)}
        kwargs = {
            keystone: id_ in self.active_skill_tree.nodes
            for keystone, id_ in constants.KEYSTONE_IDS.items()
            if keystone in keystone_fields
        }
        return models.Keystones(**kwargs)

    @memoized_property
    def notes(self) -> str:
        """Get notes of a build's author.

        Notes are automatically cleaned from Path of Building formatting codes.

        :return: Build notes without formatting codes.
        :rtype: :class:`str`"""
        notes_element = self.xml.find("Notes")
        if notes_element is None or notes_element.text is None:
            return ""
        raw_notes = notes_element.text.strip("\n\r\t").rstrip("\n\r\t")
        return clean_pob_formatting(raw_notes)

    def add_node(self, node_id: int, tree_index: int = 0) -> None:
        """Add a passive tree node.

        :param node_id: Node ID to add
            (e.g., PassiveNodeID.ELEMENTAL_EQUILIBRIUM or 39085).
        :param tree_index: Index of tree (default: 0).
        :raises: ValidationError if tree_index is invalid.
        """
        self._modifier.add_node(node_id, tree_index)

    def remove_node(self, node_id: int, tree_index: int = 0) -> None:
        """Remove a passive tree node.

        :param node_id: Node ID to remove.
        :param tree_index: Index of tree (default: 0).
        """
        self._modifier.remove_node(node_id, tree_index)

    def equip_item(
        self,
        item: models.Item,
        slot: ItemSlot | str,
        item_set_index: int = 0,
    ) -> int:
        """Equip an item in a slot.

        :param item: Item to equip.
        :param slot: Slot name (e.g., "Body Armour", "Helmet").
        :param item_set_index: Index of item set (default: 0).
        :return: Index of added item.
        :raises: ValidationError if slot is invalid.
        """
        return self._modifier.equip_item(item, slot, item_set_index)

    def add_skill(
        self,
        gem: models.Gem | models.GrantedAbility,
        group_label: str = "Main",
    ) -> None:
        """Add a skill gem to a skill group.

        :param gem: Gem or GrantedAbility to add.
        :param group_label: Label of skill group to add to.
        """
        self._modifier.add_skill(gem, group_label)

    def to_xml(self) -> bytes:
        """Export build to XML format.

        :return: XML bytes representing the build.
        """
        from lxml.etree import tostring

        from pobapi.serializers import BuildXMLSerializer

        xml_element = BuildXMLSerializer.serialize_from_api(self)
        xml_bytes: bytes = tostring(
            xml_element, encoding="utf-8", xml_declaration=True, pretty_print=False
        )
        return xml_bytes

    def to_import_code(self) -> str:
        """Export build to import code format.

        :return: Import code string.
        """
        from pobapi.serializers import ImportCodeGenerator

        return ImportCodeGenerator.generate_from_api(self)

    @memoized_property
    def second_weapon_set(self) -> bool:
        """Get whether a character primarily uses their second weapon set.

        :return: Truth value.
        :rtype: :class:`bool`"""
        return self.xml.find("Items").get("useSecondWeaponSet") == "true"  # type: ignore[no-any-return]

    @memoized_property
    @listify
    def items(self) -> list[models.Item]:  # type: ignore[misc]
        """Get a list of all items of a Path Of Building build.

        :return: Items.
        :rtype: :class:`~typing.List`\\[:class:`~pobapi.models.Item`]"""
        # First yield pending items (from equip_item calls)
        if hasattr(self, "_pending_items"):
            yield from self._pending_items

        # Then yield items from XML
        items_element = self.xml.find("Items")
        if items_element is None:
            return

        for text in items_element.findall("Item"):
            variant = text.get("variant")
            alt_variant = text.get("variantAlt")
            # "variantAlt" is for the second Watcher's Eye unique mod.
            # The 3-stat variant obtained from Uber Elder is not yet implemented in PoB.
            mod_ranges = [float(i.get("range")) for i in text.findall("ModRange")]
            item_lines = text.text.strip("\n\r\t").splitlines()
            # Strip leading/trailing whitespace from each line
            item_lines = [line.strip() for line in item_lines if line.strip()]
            rarity_stat = _get_stat(item_lines, "Rarity: ")
            rarity = (
                rarity_stat.capitalize()
                if isinstance(rarity_stat, str) and rarity_stat
                else "Normal"
            )
            name = item_lines[1] if len(item_lines) > 1 else ""
            base = (
                name
                if rarity in ("Normal", "Magic")
                else (item_lines[2] if len(item_lines) > 2 else name)
            )
            uid = _get_stat(item_lines, "Unique ID: ") or ""
            shaper = bool(_get_stat(item_lines, "Shaper Item"))
            elder = bool(_get_stat(item_lines, "Elder Item"))
            crafted = bool(_get_stat(item_lines, "{crafted}"))
            _quality = _get_stat(item_lines, "Quality: ")
            quality = int(_quality) if _quality else None
            _sockets = _get_stat(item_lines, "Sockets: ")
            sockets: tuple | None = (
                tuple(tuple(group.split("-")) for group in _sockets.split())
                if isinstance(_sockets, str) and _sockets
                else None
            )
            level_req = int(_get_stat(item_lines, "LevelReq: ") or 0)
            item_level = int(_get_stat(item_lines, "Item Level: ") or 1)
            implicit = int(_get_stat(item_lines, "Implicits: ") or 0)
            item_text = _get_text(item_lines, variant, alt_variant, mod_ranges)
            # fmt: off
            yield models.Item(
                rarity, name, base, str(uid), shaper, elder, crafted, quality,
                sockets, level_req, item_level, implicit, item_text
            )
            # fmt: on

    @memoized_property
    def active_item_set(self) -> models.Set:
        """Get the item set a character is currently wearing.

        :return: Item set.
        :rtype: :class:`~pobapi.models.Set`"""
        items_elem = self.xml.find("Items")
        if items_elem is None:
            # If no Items element, return first item set or create empty one
            if self.item_sets:
                first_set: models.Set = self.item_sets[0]
                return first_set
            from pobapi.builders import ItemSetBuilder

            empty_set_data = {
                slot_name: None
                for slot_name in [
                    "weapon1",
                    "weapon1_swap",
                    "weapon2",
                    "weapon2_swap",
                    "helmet",
                    "body_armour",
                    "gloves",
                    "boots",
                    "amulet",
                    "ring1",
                    "ring2",
                    "belt",
                    "flask1",
                    "flask2",
                    "flask3",
                    "flask4",
                    "flask5",
                ]
            }
            return ItemSetBuilder._build_single(empty_set_data)

        active_item_set_attr = items_elem.get("activeItemSet")
        if active_item_set_attr is None:
            # Default to first item set (0-based index)
            index = 0
        else:
            index = int(active_item_set_attr) - 1

        if index < 0 or index >= len(self.item_sets):
            # If no item sets exist, return empty set
            if not self.item_sets:
                from pobapi.builders import ItemSetBuilder

                empty_set_data = {
                    slot_name: None
                    for slot_name in [
                        "weapon1",
                        "weapon1_swap",
                        "weapon2",
                        "weapon2_swap",
                        "helmet",
                        "body_armour",
                        "gloves",
                        "boots",
                        "amulet",
                        "ring1",
                        "ring2",
                        "belt",
                        "flask1",
                        "flask2",
                        "flask3",
                        "flask4",
                        "flask5",
                    ]
                }
                return ItemSetBuilder._build_single(empty_set_data)
            index = 0

        return self.item_sets[index]  # type: ignore[no-any-return]

    @memoized_property
    def item_sets(self) -> list[models.Set]:
        """Get a list of all item sets of a character.

        .. note:: Slot IDs are 0-indexed.

        :return: Item sets.
        :rtype: :class:`~typing.List`\\[:class:`~pobapi.models.Set`]"""

        item_sets_list = ItemSetBuilder.build_all(self.xml)

        # Apply pending modifications (from equip_item calls)
        if hasattr(self, "_pending_item_sets"):
            empty_set_data = {
                slot_name: None
                for slot_name in [
                    "weapon1",
                    "weapon1_swap",
                    "weapon2",
                    "weapon2_swap",
                    "helmet",
                    "body_armour",
                    "gloves",
                    "boots",
                    "amulet",
                    "ring1",
                    "ring2",
                    "belt",
                    "flask1",
                    "flask2",
                    "flask3",
                    "flask4",
                    "flask5",
                ]
            }
            for index, modified_set in self._pending_item_sets.items():
                if index < len(item_sets_list):
                    # Update the item_set with modifications
                    item_sets_list[index] = modified_set
                else:
                    # Append new item set (index >= len)
                    while len(item_sets_list) <= index:
                        # Fill gaps with empty sets if needed
                        item_sets_list.append(
                            ItemSetBuilder._build_single(empty_set_data)
                        )
                    # After while loop, len(item_sets_list) > index always
                    # So we can directly set the modified set at the correct index
                    item_sets_list[index] = modified_set

        return item_sets_list

    @memoized_property
    def config(self) -> config.Config:
        """Namespace for Path Of Building config tab's options and values.

        :return: Path Of Building config.
        :rtype: :class:`~pobapi.config.Config`"""
        return ConfigBuilder.build(self.xml, self.level)

    @classmethod
    @listify
    def _abilities(cls, skill) -> list[models.Gem | models.GrantedAbility]:  # type: ignore[misc]
        """Get a list of abilities, whether they are granted by gems or by items.

        :return: Abilities.
        :rtype: :class:`~typing.List`\\
            [:data:`~typing.Union`\\[:class:`~pobapi.models.Gem`,
            :class:`~pobapi.models.GrantedAbility`]]"""
        for ability in skill:
            gem_id = ability.get("gemId")
            name = ability.get("nameSpec")
            enabled = ability.get("enabled") == "true"
            level = int(ability.get("level"))
            if gem_id:
                quality = int(ability.get("quality"))
                skill_id = ability.get("skillId")
                support = skill_id.startswith("Support") if skill_id else False
                # Ensure name is not None for Gem
                if not name:
                    name = skill_id or ""
                yield models.Gem(name, enabled, level, quality, support)
            else:
                skill_id = ability.get("skillId")
                name = (
                    name
                    or (constants.SKILL_MAP.get(skill_id) if skill_id else None)
                    or ""
                )
                yield models.GrantedAbility(name, enabled, level)


def from_url(url: str, timeout: float = 6.0) -> PathOfBuildingAPI:
    """Instantiate build class from a pastebin.com link generated with Path Of Building.

    :raises: :class:`~pobapi.exceptions.InvalidURLError`,
        :class:`~pobapi.exceptions.NetworkError`,
        :class:`~pobapi.exceptions.ParsingError`

    :param url: pastebin.com link generated with Path Of Building.
    :param timeout: Timeout for the request."""
    InputValidator.validate_url(url)
    xml_bytes = _fetch_xml_from_url(url, timeout)
    return PathOfBuildingAPI(xml_bytes)


def from_import_code(import_code: str) -> PathOfBuildingAPI:
    """Instantiate build class from an import code generated with Path Of Building.

    :raises: :class:`~pobapi.exceptions.InvalidImportCodeError`,
        :class:`~pobapi.exceptions.ParsingError`

    :param import_code: import code generated with Path Of Building."""
    InputValidator.validate_import_code(import_code)
    xml_bytes = _fetch_xml_from_import_code(import_code)
    return PathOfBuildingAPI(xml_bytes)


def create_build() -> BuildBuilder:
    """Create a new empty build using BuildBuilder.

    :return: BuildBuilder instance for building a new build.
    """
    from pobapi.build_builder import BuildBuilder

    return BuildBuilder()
