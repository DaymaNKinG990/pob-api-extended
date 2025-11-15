"""Builder for creating Path of Building builds programmatically."""

from typing import Any

from pobapi import models
from pobapi.api import PathOfBuildingAPI
from pobapi.exceptions import ValidationError
from pobapi.types import (
    Ascendancy,
    BanditChoice,
    CharacterClass,
    ItemSlot,
)

__all__ = ["BuildBuilder"]


class BuildBuilder:
    """Builder for creating Path of Building builds programmatically.

    This class allows you to create a build from scratch without needing
    to start from an existing XML or import code.
    """

    def __init__(self):
        """Initialize empty build builder."""
        self.class_name: str = "Scion"
        self.ascendancy_name: str | None = None
        self.level: int = 1
        self.bandit: str | None = None
        self.main_socket_group: int | None = None

        self.items: list[models.Item] = []
        self.item_sets: list[models.Set] = []
        self.trees: list[models.Tree] = []
        self.active_spec: int = 1
        self.skill_groups: list[models.SkillGroup] = []
        self.config: Any | None = None
        self.notes: str = ""
        self.second_weapon_set: bool = False

    def set_class(
        self,
        class_name: CharacterClass | str,
        ascendancy_name: Ascendancy | str | None = None,
    ) -> "BuildBuilder":
        """Set character class and ascendancy.

        :param class_name: Character class (e.g., CharacterClass.WITCH or "Witch").
        :param ascendancy_name: Optional ascendancy class
            (e.g., Ascendancy.NECROMANCER).
        :return: Self for method chaining.
        """
        if isinstance(class_name, CharacterClass):
            self.class_name = class_name.value
        else:
            self.class_name = class_name

        if isinstance(ascendancy_name, Ascendancy):
            self.ascendancy_name = ascendancy_name.value
        elif ascendancy_name is not None:
            self.ascendancy_name = ascendancy_name
        else:
            self.ascendancy_name = None
        return self

    def set_level(self, level: int) -> "BuildBuilder":
        """Set character level.

        :param level: Character level (1-100).
        :return: Self for method chaining.
        :raises: ValidationError if level is invalid.
        """
        if not 1 <= level <= 100:
            raise ValidationError(f"Level must be between 1 and 100, got {level}")
        self.level = level
        return self

    def set_bandit(self, bandit: BanditChoice | str | None) -> "BuildBuilder":
        """Set bandit choice.

        :param bandit: Bandit choice (e.g., BanditChoice.ALIRA or "Alira").
        :return: Self for method chaining.
        """
        if isinstance(bandit, BanditChoice):
            self.bandit = bandit.value
        elif bandit not in (None, "Alira", "Oak", "Kraityn"):
            raise ValidationError(f"Invalid bandit choice: {bandit}")
        else:
            self.bandit = bandit
        return self

    def add_item(self, item: models.Item) -> int:
        """Add item to build.

        :param item: Item to add.
        :return: Index of added item (0-based).
        """
        self.items.append(item)
        return len(self.items) - 1

    def create_item_set(self) -> models.Set:
        """Create a new empty item set.

        :return: New empty Set instance.
        """
        item_set = models.Set(
            weapon1=None,
            weapon1_as1=None,
            weapon1_as2=None,
            weapon1_swap=None,
            weapon1_swap_as1=None,
            weapon1_swap_as2=None,
            weapon2=None,
            weapon2_as1=None,
            weapon2_as2=None,
            weapon2_swap=None,
            weapon2_swap_as1=None,
            weapon2_swap_as2=None,
            helmet=None,
            helmet_as1=None,
            helmet_as2=None,
            body_armour=None,
            body_armour_as1=None,
            body_armour_as2=None,
            gloves=None,
            gloves_as1=None,
            gloves_as2=None,
            boots=None,
            boots_as1=None,
            boots_as2=None,
            amulet=None,
            ring1=None,
            ring2=None,
            belt=None,
            belt_as1=None,
            belt_as2=None,
            flask1=None,
            flask2=None,
            flask3=None,
            flask4=None,
            flask5=None,
        )
        self.item_sets.append(item_set)
        return item_set

    def equip_item(
        self,
        item_index: int,
        slot: ItemSlot | str,
        item_set_index: int = 0,
    ) -> "BuildBuilder":
        """Equip item in a slot.

        :param item_index: Index of item in items list (0-based).
        :param slot: Slot name (e.g., "Body Armour", "Helmet", "Ring1").
        :param item_set_index: Index of item set (default: 0).
        :return: Self for method chaining.
        :raises: ValidationError if item_index or item_set_index is invalid.
        """
        if item_index < 0 or item_index >= len(self.items):
            raise ValidationError(f"Invalid item index: {item_index}")
        if item_set_index < 0 or item_set_index >= len(self.item_sets):
            # Create item set if it doesn't exist
            while len(self.item_sets) <= item_set_index:
                self.create_item_set()

        item_set = self.item_sets[item_set_index]

        # Map slot names to Set attributes
        slot_mapping = {
            "Weapon1": "weapon1",
            "Weapon1 Swap": "weapon1_swap",
            "Weapon2": "weapon2",
            "Weapon2 Swap": "weapon2_swap",
            "Helmet": "helmet",
            "Body Armour": "body_armour",
            "Gloves": "gloves",
            "Boots": "boots",
            "Amulet": "amulet",
            "Ring1": "ring1",
            "Ring2": "ring2",
            "Belt": "belt",
            "Flask1": "flask1",
            "Flask2": "flask2",
            "Flask3": "flask3",
            "Flask4": "flask4",
            "Flask5": "flask5",
        }

        # Get slot string value
        if isinstance(slot, ItemSlot):
            slot_str = slot.value
        else:
            slot_str = slot

        slot_attr = slot_mapping.get(slot_str)
        if slot_attr is None:
            raise ValidationError(f"Invalid slot name: {slot_str}")

        setattr(item_set, slot_attr, item_index)
        return self

    def create_tree(self, url: str = "") -> models.Tree:
        """Create a new passive skill tree.

        :param url: Optional tree URL from pathofexile.com.
        :return: New Tree instance.
        """
        tree = models.Tree(url=url, nodes=[], sockets={})
        self.trees.append(tree)
        return tree

    def allocate_node(self, node_id: int, tree_index: int = 0) -> "BuildBuilder":
        """Allocate a passive tree node.

        :param node_id: Node ID to allocate
            (e.g., PassiveNodeID.ELEMENTAL_EQUILIBRIUM or 39085).
        :param tree_index: Index of tree (default: 0).
        :return: Self for method chaining.
        :raises: ValidationError if tree_index is invalid.
        """
        # node_id can be int or PassiveNodeID.<CONSTANT> (which is also int)
        actual_node_id = int(node_id)

        if tree_index < 0 or tree_index >= len(self.trees):
            # Create tree if it doesn't exist
            if len(self.trees) == 0:
                self.create_tree()
            else:
                raise ValidationError(f"Invalid tree index: {tree_index}")

        tree = self.trees[tree_index]
        if actual_node_id not in tree.nodes:
            tree.nodes.append(actual_node_id)
        return self

    def remove_node(self, node_id: int, tree_index: int = 0) -> "BuildBuilder":
        """Remove a passive tree node.

        :param node_id: Node ID to remove.
        :param tree_index: Index of tree (default: 0).
        :return: Self for method chaining.
        """
        if 0 <= tree_index < len(self.trees):
            tree = self.trees[tree_index]
            if node_id in tree.nodes:
                tree.nodes.remove(node_id)
        return self

    def socket_jewel(
        self, socket_id: int, item_index: int, tree_index: int = 0
    ) -> "BuildBuilder":
        """Socket a jewel in a passive tree socket.

        :param socket_id: Socket node ID.
        :param item_index: Index of jewel item.
        :param tree_index: Index of tree (default: 0).
        :return: Self for method chaining.
        """
        if item_index < 0 or item_index >= len(self.items):
            raise ValidationError(f"Invalid item index: {item_index}")
        if tree_index < 0 or tree_index >= len(self.trees):
            if len(self.trees) == 0:
                self.create_tree()
            else:
                raise ValidationError(f"Invalid tree index: {tree_index}")

        tree = self.trees[tree_index]
        tree.sockets[socket_id] = item_index
        return self

    def add_skill_group(
        self,
        label: str = "Main",
        enabled: bool = True,
        active: int | None = None,
    ) -> models.SkillGroup:
        """Add a skill group.

        :param label: Skill group label.
        :param enabled: Whether the group is enabled.
        :param active: Index of active skill in group.
        :return: New SkillGroup instance.
        """
        skill_group = models.SkillGroup(
            enabled=enabled, label=label, active=active, abilities=[]
        )
        self.skill_groups.append(skill_group)

        # Set as main socket group if it's the first one
        if len(self.skill_groups) == 1 and self.main_socket_group is None:
            self.main_socket_group = 1

        return skill_group

    def add_skill(
        self,
        gem: models.Gem | models.GrantedAbility,
        group_label: str = "Main",
    ) -> "BuildBuilder":
        """Add a skill gem to a skill group.

        :param gem: Gem or GrantedAbility to add.
        :param group_label: Label of skill group to add to.
        :return: Self for method chaining.
        """
        # Find or create skill group
        skill_group = None
        for group in self.skill_groups:
            if group.label == group_label:
                skill_group = group
                break

        if skill_group is None:
            skill_group = self.add_skill_group(label=group_label)

        skill_group.abilities.append(gem)
        return self

    def set_config(self, config: Any) -> "BuildBuilder":
        """Set build configuration.

        :param config: Config object.
        :return: Self for method chaining.
        """
        self.config = config
        return self

    def set_notes(self, notes: str) -> "BuildBuilder":
        """Set build notes.

        :param notes: Notes text.
        :return: Self for method chaining.
        """
        self.notes = notes
        return self

    def set_active_spec(self, spec_index: int) -> "BuildBuilder":
        """Set active tree specification.

        :param spec_index: Index of active spec (1-based).
        :return: Self for method chaining.
        """
        if spec_index < 1:
            raise ValidationError(f"Spec index must be >= 1, got {spec_index}")
        self.active_spec = spec_index
        return self

    def build(self) -> PathOfBuildingAPI:
        """Build PathOfBuildingAPI instance.

        :return: PathOfBuildingAPI instance with created build.
        """
        from pobapi.serializers import BuildXMLSerializer

        # Serialize to XML
        xml_element = BuildXMLSerializer.serialize(self)

        # Create PathOfBuildingAPI from XML
        return PathOfBuildingAPI(xml_element)
