"""Test loading of unique items from scraped data."""

from pobapi.calculator.game_data import GameDataLoader


def test_loading():
    """Test loading unique items."""
    print("Testing unique items loading...")

    loader = GameDataLoader()

    # Try to load from processed file
    uniques = loader.load_unique_item_data("data/uniques_processed.json")

    print(f"Loaded: {len(uniques)} unique items")

    # Test finding specific items
    test_items = [
        "Headhunter",
        "Shavronne's Wrappings",
        "Starforge",
        "Abberath's Hooves",
    ]

    for item_name in test_items:
        item = loader.get_unique_item(item_name)
        if item:
            print(f"\n{item_name}:")
            print(f"  Base type: {item.base_type}")
            print(f"  Explicit mods: {len(item.explicit_mods)}")
            print(f"  Special effects: {len(item.special_effects)}")
            if item.explicit_mods:
                print(f"  Sample mod: {item.explicit_mods[0][:50]}...")
        else:
            print(f"\n{item_name}: NOT FOUND")

    # Statistics
    items_with_base = sum(1 for v in uniques.values() if v.base_type)
    items_with_mods = sum(1 for v in uniques.values() if v.explicit_mods)
    items_with_effects = sum(1 for v in uniques.values() if v.special_effects)

    print("\nStatistics:")
    base_pct = items_with_base * 100 // len(uniques)
    print(f"  Items with base_type: {items_with_base}/{len(uniques)} ({base_pct}%)")
    mods_pct = items_with_mods * 100 // len(uniques)
    print(f"  Items with modifiers: {items_with_mods}/{len(uniques)} ({mods_pct}%)")
    effects_pct = items_with_effects * 100 // len(uniques)
    print(
        f"  Items with special_effects: {items_with_effects}/{len(uniques)} "
        f"({effects_pct}%)"
    )


if __name__ == "__main__":
    test_loading()
