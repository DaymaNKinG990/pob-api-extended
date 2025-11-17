"""Module for displaying items and item sets."""

from pobapi import PathOfBuildingAPI


def print_items(build: PathOfBuildingAPI) -> None:
    """
    Display item details from the given PathOfBuildingAPI build to standard output.

    Parameters:
        build (PathOfBuildingAPI): Build whose items will be listed; each
            item's name, base, rarity, optional unique id, item level,
            level requirement, shaper/elder/crafted flags, quality,
            sockets, implicit count, and non-empty item text lines are
            printed.
    """
    print("=" * 80)
    print("  6. Items")
    print("=" * 80)
    print()
    print(f"Number of items: {len(build.items)}")
    for i, item in enumerate(build.items, 1):  # Show all items
        print(f"\n  Item {i}:")
        print(f"    Name: {item.name}")
        print(f"    Base: {item.base}")
        print(f"    Rarity: {item.rarity}")
        if item.uid:
            print(f"    Unique ID: {item.uid}")
        print(f"    Item Level: {item.item_level}")
        print(f"    Level Requirement: {item.level_req}")
        if item.shaper:
            print("    Shaper Item: Yes")
        if item.elder:
            print("    Elder Item: Yes")
        if item.crafted:
            print("    Crafted: Yes")
        if item.quality is not None:
            print(f"    Quality: {item.quality}%")
        if item.sockets:
            # Format sockets: ((B, B, B), (R, R)) -> "B-B-B R-R"
            socket_str = " ".join("-".join(group) for group in item.sockets)
            print(f"    Sockets: {socket_str}")
        if item.implicit and item.implicit > 0:
            print(f"    Implicits: {item.implicit}")
        if item.text:
            print("    Item Text:")
            for line in item.text.split("\n"):
                if line.strip():
                    print(f"      {line}")


def print_item_sets(build: PathOfBuildingAPI) -> None:
    """
    Display the active item set and all configured item sets from the provided build.

    Prints a header, attempts to print the active item set (including
    weapon swaps and abyssal sockets) and then lists each item set's
    equipped item indices. If the active set cannot be read, an error
    message is printed.

    Parameters:
        build (PathOfBuildingAPI): Build object containing
            `active_item_set` and `item_sets` used for output.
    """
    print("=" * 80)
    print("  7. Item Sets")
    print("=" * 80)
    print()

    # Show active item set first
    try:
        active_set = build.active_item_set
        print("Active Item Set:")
        print(
            f"  Weapon 1: Item #{active_set.weapon1 + 1}"
            if active_set.weapon1 is not None
            else "  Weapon 1: None"
        )
        if active_set.weapon1_as1 is not None:
            print(f"    Weapon 1 Abyssal Socket 1: Item #{active_set.weapon1_as1 + 1}")
        if active_set.weapon1_as2 is not None:
            print(f"    Weapon 1 Abyssal Socket 2: Item #{active_set.weapon1_as2 + 1}")
        if active_set.weapon1_swap is not None:
            print(f"    Weapon 1 Swap: Item #{active_set.weapon1_swap + 1}")
        print(
            f"  Weapon 2: Item #{active_set.weapon2 + 1}"
            if active_set.weapon2 is not None
            else "  Weapon 2: None"
        )
        if active_set.weapon2_as1 is not None:
            print(f"    Weapon 2 Abyssal Socket 1: Item #{active_set.weapon2_as1 + 1}")
        if active_set.weapon2_as2 is not None:
            print(f"    Weapon 2 Abyssal Socket 2: Item #{active_set.weapon2_as2 + 1}")
        if active_set.weapon2_swap is not None:
            print(f"    Weapon 2 Swap: Item #{active_set.weapon2_swap + 1}")
        print(
            f"  Helmet: Item #{active_set.helmet + 1}"
            if active_set.helmet is not None
            else "  Helmet: None"
        )
        if active_set.helmet_as1 is not None:
            print(f"    Helmet Abyssal Socket 1: Item #{active_set.helmet_as1 + 1}")
        if active_set.helmet_as2 is not None:
            print(f"    Helmet Abyssal Socket 2: Item #{active_set.helmet_as2 + 1}")
        print(
            f"  Body Armour: Item #{active_set.body_armour + 1}"
            if active_set.body_armour is not None
            else "  Body Armour: None"
        )
        if active_set.body_armour_as1 is not None:
            item_num = active_set.body_armour_as1 + 1
            print(f"    Body Armour Abyssal Socket 1: Item #{item_num}")
        if active_set.body_armour_as2 is not None:
            item_num = active_set.body_armour_as2 + 1
            print(f"    Body Armour Abyssal Socket 2: Item #{item_num}")
        print(
            f"  Gloves: Item #{active_set.gloves + 1}"
            if active_set.gloves is not None
            else "  Gloves: None"
        )
        if active_set.gloves_as1 is not None:
            print(f"    Gloves Abyssal Socket 1: Item #{active_set.gloves_as1 + 1}")
        if active_set.gloves_as2 is not None:
            print(f"    Gloves Abyssal Socket 2: Item #{active_set.gloves_as2 + 1}")
        print(
            f"  Boots: Item #{active_set.boots + 1}"
            if active_set.boots is not None
            else "  Boots: None"
        )
        if active_set.boots_as1 is not None:
            print(f"    Boots Abyssal Socket 1: Item #{active_set.boots_as1 + 1}")
        if active_set.boots_as2 is not None:
            print(f"    Boots Abyssal Socket 2: Item #{active_set.boots_as2 + 1}")
        print(
            f"  Amulet: Item #{active_set.amulet + 1}"
            if active_set.amulet is not None
            else "  Amulet: None"
        )
        print(
            f"  Ring 1: Item #{active_set.ring1 + 1}"
            if active_set.ring1 is not None
            else "  Ring 1: None"
        )
        print(
            f"  Ring 2: Item #{active_set.ring2 + 1}"
            if active_set.ring2 is not None
            else "  Ring 2: None"
        )
        print(
            f"  Belt: Item #{active_set.belt + 1}"
            if active_set.belt is not None
            else "  Belt: None"
        )
        if active_set.belt_as1 is not None:
            print(f"    Belt Abyssal Socket 1: Item #{active_set.belt_as1 + 1}")
        if active_set.belt_as2 is not None:
            print(f"    Belt Abyssal Socket 2: Item #{active_set.belt_as2 + 1}")
        if active_set.flask1 is not None:
            print(f"  Flask 1: Item #{active_set.flask1 + 1}")
        if active_set.flask2 is not None:
            print(f"  Flask 2: Item #{active_set.flask2 + 1}")
        if active_set.flask3 is not None:
            print(f"  Flask 3: Item #{active_set.flask3 + 1}")
        if active_set.flask4 is not None:
            print(f"  Flask 4: Item #{active_set.flask4 + 1}")
        if active_set.flask5 is not None:
            print(f"  Flask 5: Item #{active_set.flask5 + 1}")
        print()
    except (IndexError, AttributeError) as e:
        print(f"Could not determine active item set: {e}\n")

    print(f"Number of item sets: {len(build.item_sets)}")
    for i, item_set in enumerate(build.item_sets, 1):
        print(f"\n  Item Set {i}:")
        if item_set.weapon1 is not None:
            print(f"    Weapon 1: Item #{item_set.weapon1 + 1}")
        if item_set.weapon2 is not None:
            print(f"    Weapon 2: Item #{item_set.weapon2 + 1}")
        if item_set.body_armour is not None:
            print(f"    Body Armour: Item #{item_set.body_armour + 1}")
        if item_set.helmet is not None:
            print(f"    Helmet: Item #{item_set.helmet + 1}")
        if item_set.gloves is not None:
            print(f"    Gloves: Item #{item_set.gloves + 1}")
        if item_set.boots is not None:
            print(f"    Boots: Item #{item_set.boots + 1}")
        if item_set.amulet is not None:
            print(f"    Amulet: Item #{item_set.amulet + 1}")
        if item_set.ring1 is not None:
            print(f"    Ring 1: Item #{item_set.ring1 + 1}")
        if item_set.ring2 is not None:
            print(f"    Ring 2: Item #{item_set.ring2 + 1}")
        if item_set.belt is not None:
            print(f"    Belt: Item #{item_set.belt + 1}")
        if item_set.flask1 is not None:
            print(f"    Flask 1: Item #{item_set.flask1 + 1}")
        if item_set.flask2 is not None:
            print(f"    Flask 2: Item #{item_set.flask2 + 1}")
        if item_set.flask3 is not None:
            print(f"    Flask 3: Item #{item_set.flask3 + 1}")
        if item_set.flask4 is not None:
            print(f"    Flask 4: Item #{item_set.flask4 + 1}")
        if item_set.flask5 is not None:
            print(f"    Flask 5: Item #{item_set.flask5 + 1}")


def main():
    """
    Construct a PathOfBuildingAPI build from the bundled demo import code
    and print the build's items.

    This prepares the demo environment, creates a build using the demo
    import code, and invokes print_items(build) to display item
    information.
    """
    import sys
    from pathlib import Path

    # Add parent directory to path to import from utils
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pobapi import from_import_code
    from utils.demo_pobapi import import_code

    build = from_import_code(import_code())
    print_items(build)


if __name__ == "__main__":
    main()
