"""Build modification functionality.

This module provides BuildModifier class for modifying builds,
separating modification logic from the main API class.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pobapi import models
from pobapi.exceptions import ValidationError
from pobapi.types import ItemSlot

if TYPE_CHECKING:
    from pobapi.api import PathOfBuildingAPI

__all__ = ["BuildModifier"]


class BuildModifier:
    """Class for modifying Path of Building builds.

    This class handles all build modification operations including:
    - Adding/removing passive tree nodes
    - Equipping items
    - Adding skills

    :param api: PathOfBuildingAPI instance to modify.
    """

    def __init__(self, api: PathOfBuildingAPI):
        """Initialize build modifier.

        :param api: PathOfBuildingAPI instance to modify.
        """
        self._api = api

    def add_node(self, node_id: int, tree_index: int = 0) -> None:
        """Add a passive tree node.

        :param node_id: Node ID to add
            (e.g., PassiveNodeID.ELEMENTAL_EQUILIBRIUM or 39085).
        :param tree_index: Index of tree (default: 0).
        :raises: ValidationError if tree_index is invalid.
        """
        # node_id can be int or PassiveNodeID.<CONSTANT> (which is also int)
        actual_node_id = int(node_id)

        if tree_index < 0 or tree_index >= len(self._api.trees):
            raise ValidationError(f"Invalid tree index: {tree_index}")

        tree = self._api.trees[tree_index]
        if actual_node_id not in tree.nodes:
            tree.nodes.append(actual_node_id)
            self._api._is_mutable = True
            # Invalidate cached properties that depend on tree
            if hasattr(self._api, "_active_skill_tree"):
                delattr(self._api, "_active_skill_tree")

    def remove_node(self, node_id: int, tree_index: int = 0) -> None:
        """Remove a passive tree node.

        :param node_id: Node ID to remove.
        :param tree_index: Index of tree (default: 0).
        """
        if 0 <= tree_index < len(self._api.trees):
            tree = self._api.trees[tree_index]
            if node_id in tree.nodes:
                tree.nodes.remove(node_id)
                self._api._is_mutable = True
                # Invalidate cached properties
                if hasattr(self._api, "_active_skill_tree"):
                    delattr(self._api, "_active_skill_tree")

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
        # Add item to pending items list
        if not hasattr(self._api, "_pending_items"):
            self._api._pending_items = []

        # Calculate index based on current items count (including pending)
        item_index = len(list(self._api.items))

        # Add to pending items
        self._api._pending_items.append(item)

        # Invalidate items cache
        if hasattr(self._api, "_items"):
            delattr(self._api, "_items")

        # Get or create item set
        # First, get current item_sets (may be cached)
        current_item_sets = list(self._api.item_sets)
        if item_set_index >= len(current_item_sets):
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
            # Create new item sets and add to pending
            if not hasattr(self._api, "_pending_item_sets"):
                self._api._pending_item_sets = {}
            while len(current_item_sets) <= item_set_index:
                new_set = ItemSetBuilder._build_single(empty_set_data)
                current_item_sets.append(new_set)
                # Save to pending_item_sets so it persists after cache invalidation
                self._api._pending_item_sets[len(current_item_sets) - 1] = new_set

        item_set = current_item_sets[item_set_index]

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

        # Note: This modifies the model, but XML won't be updated
        # until to_xml() is called
        setattr(item_set, slot_attr, item_index)  # Store 0-based index
        self._api._is_mutable = True

        # Save modified item_set to pending list to preserve changes
        # (since item_sets property reads from XML, we need to track
        # modifications separately)
        if not hasattr(self._api, "_pending_item_sets"):
            self._api._pending_item_sets = {}
        self._api._pending_item_sets[item_set_index] = item_set

        # Invalidate cached properties
        if hasattr(self._api, "_active_item_set"):
            delattr(self._api, "_active_item_set")
        if hasattr(self._api, "_item_sets"):
            delattr(self._api, "_item_sets")

        return item_index

    def add_skill(
        self,
        gem: models.Gem | models.GrantedAbility,
        group_label: str = "Main",
    ) -> None:
        """Add a skill gem to a skill group.

        :param gem: Gem or GrantedAbility to add.
        :param group_label: Label of skill group to add to.
        """
        # Find or create skill group
        skill_group = None
        for group in self._api.skill_groups:
            if group.label == group_label:
                skill_group = group
                break

        if skill_group is None:
            skill_group = models.SkillGroup(
                enabled=True, label=group_label, active=None, abilities=[]
            )
            # Store pending skill groups
            if not hasattr(self._api, "_pending_skill_groups"):
                self._api._pending_skill_groups = []
            self._api._pending_skill_groups.append(skill_group)
            self._api._is_mutable = True
            # Invalidate cached properties
            if hasattr(self._api, "_skill_groups"):
                delattr(self._api, "_skill_groups")
            if hasattr(self._api, "_active_skill_group"):
                delattr(self._api, "_active_skill_group")

        skill_group.abilities.append(gem)
        self._api._is_mutable = True
