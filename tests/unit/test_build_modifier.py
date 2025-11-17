"""Tests for BuildModifier class."""

import pytest

from pobapi import create_build, models
from pobapi.build_modifier import BuildModifier
from pobapi.exceptions import ValidationError
from pobapi.types import ItemSlot, PassiveNodeID


class TestBuildModifier:
    """Tests for BuildModifier class."""

    @pytest.fixture
    def simple_build(self):
        """Create a simple build for testing."""
        builder = create_build()
        builder.set_class("Witch", "Necromancer")
        builder.set_level(90)
        builder.create_tree()
        builder.create_item_set()
        return builder.build()

    @pytest.fixture
    def modifier(self, simple_build):
        """Create BuildModifier instance."""
        return BuildModifier(simple_build)

    def test_init(self, simple_build):
        """Test BuildModifier initialization."""
        modifier = BuildModifier(simple_build)
        assert modifier._api is simple_build

    def test_add_node(self, modifier, simple_build):
        """Test adding a node to the tree."""
        initial_count = len(simple_build.trees[0].nodes)
        modifier.add_node(PassiveNodeID.ELEMENTAL_EQUILIBRIUM)
        assert len(simple_build.trees[0].nodes) == initial_count + 1
        assert PassiveNodeID.ELEMENTAL_EQUILIBRIUM in simple_build.trees[0].nodes
        assert simple_build._is_mutable is True

    def test_add_node_duplicate(self, modifier, simple_build):
        """Test adding a duplicate node doesn't add it twice."""
        modifier.add_node(PassiveNodeID.ELEMENTAL_EQUILIBRIUM)
        initial_count = len(simple_build.trees[0].nodes)
        modifier.add_node(PassiveNodeID.ELEMENTAL_EQUILIBRIUM)
        assert len(simple_build.trees[0].nodes) == initial_count

    def test_add_node_invalid_tree_index(self, modifier):
        """Test adding node with invalid tree index."""
        with pytest.raises(ValidationError, match="Invalid tree index"):
            modifier.add_node(PassiveNodeID.ELEMENTAL_EQUILIBRIUM, tree_index=999)

    def test_remove_node(self, modifier, simple_build):
        """Test removing a node from the tree."""
        node_id = PassiveNodeID.ELEMENTAL_EQUILIBRIUM
        modifier.add_node(node_id)
        assert node_id in simple_build.trees[0].nodes
        modifier.remove_node(node_id)
        assert node_id not in simple_build.trees[0].nodes
        assert simple_build._is_mutable is True

    def test_remove_node_not_present(self, modifier, simple_build):
        """Test removing a node that doesn't exist."""
        initial_count = len(simple_build.trees[0].nodes)
        modifier.remove_node(99999)
        assert len(simple_build.trees[0].nodes) == initial_count

    def test_equip_item(self, modifier, simple_build):
        """Test equipping an item."""
        item = models.Item(
            rarity="Rare",
            name="Test Helmet",
            base="Iron Helmet",
            uid="",
            shaper=False,
            elder=False,
            crafted=False,
            quality=None,
            sockets=None,
            level_req=1,
            item_level=80,
            implicit=None,
            text="+50 to maximum Life\n+20% to Fire Resistance",
        )
        item_index = modifier.equip_item(item, ItemSlot.HELMET)
        assert item_index >= 0
        assert simple_build._is_mutable is True
        assert item in simple_build._pending_items

    def test_equip_item_invalid_slot(self, modifier):
        """Test equipping item with invalid slot."""
        item = models.Item(
            rarity="Rare",
            name="Test Item",
            base="Test Base",
            uid="",
            shaper=False,
            elder=False,
            crafted=False,
            quality=None,
            sockets=None,
            level_req=1,
            item_level=80,
            implicit=None,
            text="",
        )
        with pytest.raises(ValidationError, match="Invalid slot name"):
            modifier.equip_item(item, "InvalidSlot")

    def test_equip_item_string_slot(self, modifier, simple_build):
        """Test equipping item with string slot name."""
        item = models.Item(
            rarity="Rare",
            name="Test Body",
            base="Plate Vest",
            uid="",
            shaper=False,
            elder=False,
            crafted=False,
            quality=None,
            sockets=None,
            level_req=1,
            item_level=80,
            implicit=None,
            text="",
        )
        item_index = modifier.equip_item(item, "Body Armour")
        assert item_index >= 0

    def test_add_skill(self, modifier, simple_build):
        """Test adding a skill gem."""
        gem = models.Gem(
            name="Fireball",
            level=20,
            quality=0,
            enabled=True,
            support=False,
        )
        modifier.add_skill(gem, "Main")
        assert simple_build._is_mutable is True
        # Check that skill was added
        skill_groups = list(simple_build.skill_groups)
        main_group = next((g for g in skill_groups if g.label == "Main"), None)
        assert main_group is not None
        assert gem in main_group.abilities

    def test_add_skill_new_group(self, modifier, simple_build):
        """Test adding skill to a new group."""
        gem = models.Gem(
            name="Flame Dash",
            level=1,
            quality=0,
            enabled=True,
            support=False,
        )
        modifier.add_skill(gem, "Movement")
        skill_groups = list(simple_build.skill_groups)
        movement_group = next((g for g in skill_groups if g.label == "Movement"), None)
        assert movement_group is not None
        assert movement_group.enabled is True
        assert gem in movement_group.abilities

    def test_add_skill_granted_ability(self, modifier, simple_build):
        """Test adding a granted ability."""
        ability = models.GrantedAbility(
            name="Herald of Ash",
            level=20,
            enabled=True,
        )
        modifier.add_skill(ability, "Auras")
        skill_groups = list(simple_build.skill_groups)
        aura_group = next((g for g in skill_groups if g.label == "Auras"), None)
        assert aura_group is not None
        assert ability in aura_group.abilities

    def test_equip_item_creates_new_item_set(self, modifier, simple_build):
        """Test equipping item to non-existent item set creates it and
        initializes _pending_item_sets."""
        # Ensure _pending_item_sets doesn't exist
        if hasattr(simple_build, "_pending_item_sets"):
            delattr(simple_build, "_pending_item_sets")

        item = models.Item(
            rarity="Rare",
            name="Test Ring",
            base="Iron Ring",
            uid="",
            shaper=False,
            elder=False,
            crafted=False,
            quality=None,
            sockets=None,
            level_req=1,
            item_level=80,
            implicit=None,
            text="",
        )
        # Equip to item_set_index=1 (doesn't exist yet)
        item_index = modifier.equip_item(item, ItemSlot.RING1, item_set_index=1)
        assert item_index >= 0
        # Check that _pending_item_sets was initialized
        assert hasattr(simple_build, "_pending_item_sets")
        assert isinstance(simple_build._pending_item_sets, dict)
        assert 1 in simple_build._pending_item_sets

    def test_equip_item_modifies_existing_set_initializes_pending(
        self, modifier, simple_build
    ):
        """Test modifying existing item set initializes _pending_item_sets
        if not exists."""
        # Ensure _pending_item_sets doesn't exist
        if hasattr(simple_build, "_pending_item_sets"):
            delattr(simple_build, "_pending_item_sets")

        item = models.Item(
            rarity="Rare",
            name="Test Belt",
            base="Leather Belt",
            uid="",
            shaper=False,
            elder=False,
            crafted=False,
            quality=None,
            sockets=None,
            level_req=1,
            item_level=80,
            implicit=None,
            text="",
        )
        # Equip to existing item_set_index=0
        item_index = modifier.equip_item(item, ItemSlot.BELT, item_set_index=0)
        assert item_index >= 0
        # Check that _pending_item_sets was initialized
        assert hasattr(simple_build, "_pending_item_sets")
        assert isinstance(simple_build._pending_item_sets, dict)
        assert 0 in simple_build._pending_item_sets

    def test_add_skill_initializes_pending_skill_groups(self, modifier, simple_build):
        """Test adding skill to new group initializes _pending_skill_groups
        if not exists."""
        # Ensure _pending_skill_groups doesn't exist
        if hasattr(simple_build, "_pending_skill_groups"):
            delattr(simple_build, "_pending_skill_groups")

        gem = models.Gem(
            name="Vaal Righteous Fire",
            level=20,
            quality=0,
            enabled=True,
            support=False,
        )
        # Add to a completely new group name
        modifier.add_skill(gem, "Vaal Skills")
        # Check that _pending_skill_groups was initialized
        assert hasattr(simple_build, "_pending_skill_groups")
        assert isinstance(simple_build._pending_skill_groups, list)
        assert len(simple_build._pending_skill_groups) > 0
