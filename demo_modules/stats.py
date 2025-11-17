"""Module for displaying character stats."""

import dataclasses

from pobapi import PathOfBuildingAPI


def print_stats(build: PathOfBuildingAPI) -> None:
    """
    Print a PathOfBuildingAPI character's stats organized by category.

    Prints only stats with non-None values, grouping them under predefined
    category headers.
    Any stats not matched to a category are listed under "Other Stats".

    Parameters:
        build (PathOfBuildingAPI): The build whose `stats` will be displayed.
    """
    print("=" * 80)
    print("  2. Character Stats")
    print("=" * 80)
    print()

    stats = build.stats

    # Get all stats fields and print only non-None values
    stats_fields = dataclasses.fields(stats)
    stats_with_values = [
        (field.name, getattr(stats, field.name))
        for field in stats_fields
        if getattr(stats, field.name) is not None
    ]

    # Group stats by category for better readability
    categories = {
        "Damage": [
            "average_hit",
            "average_damage",
            "total_dps",
            "total_dot",
            "bleed_dps",
            "ignite_dps",
            "ignite_damage",
            "poison_dps",
            "poison_damage",
            "decay_dps",
            "total_dps_with_ignite",
            "total_dps_with_poison",
            "average_damage_with_ignite",
            "average_damage_with_poison",
        ],
        "Speed & Cooldown": [
            "cast_speed",
            "attack_speed",
            "trap_throwing_speed",
            "trap_cooldown",
            "mine_laying_speed",
            "totem_placement_speed",
            "skill_cooldown",
            "effective_movement_speed_modifier",
        ],
        "Critical": [
            "pre_effective_crit_chance",
            "crit_chance",
            "crit_multiplier",
            "hit_chance",
        ],
        "Attributes": [
            "strength",
            "strength_required",
            "dexterity",
            "dexterity_required",
            "intelligence",
            "intelligence_required",
        ],
        "Life": [
            "life",
            "life_increased",
            "life_unreserved",
            "life_unreserved_percent",
            "life_regen",
            "life_leech_rate_per_hit",
            "life_leech_gain_per_hit",
        ],
        "Mana": [
            "mana",
            "mana_increased",
            "mana_unreserved",
            "mana_unreserved_percent",
            "mana_regen",
            "mana_leech_rate_per_hit",
            "mana_leech_gain_per_hit",
            "mana_cost",
            "mana_cost_per_second",
        ],
        "Energy Shield": [
            "energy_shield",
            "energy_shield_increased",
            "energy_shield_regen",
            "energy_shield_leech_rate_per_hit",
            "energy_shield_leech_gain_per_hit",
        ],
        "Defense": [
            "armour",
            "armour_increased",
            "physical_damage_reduction",
            "evasion",
            "evasion_increased",
            "melee_evade_chance",
            "projectile_evade_chance",
            "block_chance",
            "spell_block_chance",
            "spell_suppression_chance",
            "attack_dodge_chance",
            "spell_dodge_chance",
        ],
        "Resistances": [
            "fire_resistance",
            "cold_resistance",
            "lightning_resistance",
            "chaos_resistance",
            "fire_resistance_over_cap",
            "cold_resistance_over_cap",
            "lightning_resistance_over_cap",
            "chaos_resistance_over_cap",
        ],
        "Charges": [
            "power_charges",
            "power_charges_maximum",
            "frenzy_charges",
            "frenzy_charges_maximum",
            "endurance_charges",
            "endurance_charges_maximum",
        ],
        "Defensive Calculations": [
            "physical_maximum_hit_taken",
            "fire_maximum_hit_taken",
            "cold_maximum_hit_taken",
            "lightning_maximum_hit_taken",
            "chaos_maximum_hit_taken",
            "total_effective_health_pool",
        ],
        "Other": [
            "total_degen",
            "net_life_regen",
            "net_mana_regen",
            "area_of_effect_radius",
            "active_totem_limit",
            "active_minion_limit",
            "rage",
        ],
    }

    # Print stats grouped by category
    printed_stats = set()
    for category, stat_names in categories.items():
        category_stats = [
            (name, value) for name, value in stats_with_values if name in stat_names
        ]
        if category_stats:
            print(f"\n{category}:")
            for name, value in sorted(category_stats):
                # Format name: convert snake_case to Title Case
                display_name = name.replace("_", " ").title()
                print(f"  {display_name}: {value}")
                printed_stats.add(name)

    # Print any remaining stats that weren't categorized
    remaining_stats = [
        (name, value) for name, value in stats_with_values if name not in printed_stats
    ]
    if remaining_stats:
        print("\nOther Stats:")
        for name, value in sorted(remaining_stats):
            display_name = name.replace("_", " ").title()
            print(f"  {display_name}: {value}")


def main():
    """
    Construct a PathOfBuildingAPI instance from the bundled demo import
    code and print its categorized stats.

    This function loads the demo import code, builds a PathOfBuildingAPI
    object from it, and invokes print_stats to display the character's
    stats.
    """
    import sys
    from pathlib import Path

    # Add parent directory to path to import from utils
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pobapi import from_import_code
    from utils.demo_pobapi import import_code

    build = from_import_code(import_code())
    print_stats(build)


if __name__ == "__main__":
    main()
