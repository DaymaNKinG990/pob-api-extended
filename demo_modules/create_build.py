"""Module for creating simple Path of Building builds programmatically."""

from pobapi import create_build, models
from pobapi.api import PathOfBuildingAPI
from pobapi.types import (
    Ascendancy,
    CharacterClass,
    ItemSlot,
    PassiveNodeID,
    SkillName,
)


def create_simple_build() -> PathOfBuildingAPI:
    """
    Create a minimal programmatic Path of Building example build.

    Constructs a level 90 Witch with the Necromancer ascendancy including
    a small passive tree allocation, three skill gems (Arc, Minion Damage
    support, Raise Zombie), and a simple rare Leather Belt equipped in the
    belt slot. Intended for demonstration of build creation APIs.

    Returns:
        PathOfBuildingAPI: The built Path of Building object containing
            the created build.
    """
    # Create build builder
    builder = create_build()

    # Set character class and level
    builder.set_class(CharacterClass.WITCH, Ascendancy.NECROMANCER)
    builder.set_level(90)

    # Create passive skill tree
    builder.create_tree()

    # Allocate some passive nodes (keystones and notable nodes)
    builder.allocate_node(PassiveNodeID.MINION_INSTABILITY)
    builder.allocate_node(PassiveNodeID.ZEALOTS_OATH)
    builder.allocate_node(PassiveNodeID.ELEMENTAL_EQUILIBRIUM)

    # Add some skill gems
    # Main skill: Arc
    arc_gem = models.Gem(
        name=SkillName.ARC.value,
        enabled=True,
        level=20,
        quality=20,
        support=False,
    )
    builder.add_skill(arc_gem, group_label="Main")

    # Support gems for Arc
    minion_damage_gem = models.Gem(
        name=SkillName.MINION_DAMAGE.value,
        enabled=True,
        level=20,
        quality=20,
        support=True,
    )
    builder.add_skill(minion_damage_gem, group_label="Main")

    # Minion skill: Raise Zombie
    raise_zombie_gem = models.Gem(
        name=SkillName.RAISE_ZOMBIE.value,
        enabled=True,
        level=20,
        quality=20,
        support=False,
    )
    builder.add_skill(raise_zombie_gem, group_label="Minions")

    # Add a simple item (Leather Belt)
    belt_item = models.Item(
        rarity="Rare",
        name="Leather Belt",
        base="Leather Belt",
        uid="",
        shaper=False,
        elder=False,
        crafted=False,
        quality=20,
        sockets=None,
        level_req=1,
        item_level=84,
        implicit=None,
        text="""Rarity: RARE
Leather Belt
--------
Requirements:
Level: 1
--------
Item Level: 84
--------
+25 to maximum Life
+15% to Fire Resistance
+15% to Cold Resistance
+15% to Lightning Resistance
--------
""",
    )
    belt_index = builder.add_item(belt_item)

    # Create item set and equip the belt
    builder.create_item_set()
    builder.equip_item(belt_index, ItemSlot.BELT, item_set_index=0)

    # Set notes
    builder.set_notes(
        "Simple demo build created programmatically.\n"
        "This build demonstrates basic build creation capabilities."
    )

    # Build and return the PathOfBuildingAPI instance
    build = builder.build()
    return build
