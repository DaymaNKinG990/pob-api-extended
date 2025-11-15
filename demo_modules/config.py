"""Module for displaying build configuration."""

import dataclasses

from pobapi import PathOfBuildingAPI


def print_config(build: PathOfBuildingAPI) -> None:
    """
    Show the build's configuration grouped by category and print any non-default or enabled settings.
    
    Displays the character level and prints configuration fields from build.config organized into predefined categories. Only fields with meaningful values are shown: boolean fields when True, non-None fields that differ from their defaults, and the `resistance_penalty` field is always included even if it equals its default.
    
    Parameters:
        build (PathOfBuildingAPI): Build instance whose configuration will be displayed.
    """
    print("=" * 80)
    print("  3. Build Configuration")
    print("=" * 80)
    print()
    config = build.config

    # Get all config fields
    config_fields = dataclasses.fields(config)

    # Filter out InitVar fields and get non-default values
    config_with_values = []
    for field in config_fields:
        # Skip InitVar fields (they're not actual instance attributes)
        if isinstance(field, dataclasses.Field):
            value = getattr(config, field.name)
            # Skip None values
            if value is not None:
                # For bool fields, show if True (since False is default)
                if isinstance(value, bool):
                    if value:
                        config_with_values.append((field.name, value))
                else:
                    # For other types, show if not default
                    # Special case: resistance_penalty default is -60,
                    # but we want to show it
                    if field.name == "resistance_penalty" or value != field.default:
                        config_with_values.append((field.name, value))

    # Group config by category
    categories = {
        "General": [
            "resistance_penalty",
            "enemy_level",
            "enemy_physical_hit_damage",
            "detonate_dead_corpse_life",
        ],
        "Player State": [
            "is_stationary",
            "is_moving",
            "on_full_life",
            "on_low_life",
            "on_full_energy_shield",
            "has_energy_shield",
            "minions_on_full_life",
        ],
        "Buffs & Effects": [
            "focus",
            "onslaught",
            "unholy_might",
            "phasing",
            "fortify",
            "tailwind",
            "adrenaline",
            "divinity",
            "rage",
            "leeching",
            "leeching_life",
            "leeching_energy_shield",
            "leeching_mana",
            "using_flask",
            "has_totem",
        ],
        "Charges": [
            "use_power_charges",
            "max_power_charges",
            "use_frenzy_charges",
            "max_frenzy_charges",
            "use_endurance_charges",
            "max_endurance_charges",
            "use_siphoning_charges",
            "use_challenger_charges",
            "use_blitz_charges",
            "use_inspiration_charges",
        ],
        "Enemy Configuration": [
            "enemy_boss",
            "enemy_rare_or_unique",
            "enemy_physical_reduction",
            "enemy_hexproof",
            "enemy_fire_resist",
            "enemy_cold_resist",
            "enemy_lightning_resist",
            "enemy_chaos_resist",
        ],
        "Map Mods": [
            "less_curse_effect",
            "enemy_avoid_poison_blind_bleed",
            "enemy_resistances",
            "elemental_equilibrium",
            "no_leech",
            "reduced_flask_charges",
            "minus_max_resists",
            "less_aoe",
            "enemy_avoid_status_ailment",
            "enemy_increased_accuracy",
            "less_armour_block",
            "point_blank",
            "less_recovery",
            "no_regen",
        ],
        "Curses": [
            "curse_assassins_mark",
            "curse_conductivity",
            "curse_despair",
            "curse_elemental_weakness",
            "curse_enfeeble",
            "curse_flammability",
            "curse_frostbite",
            "curse_poachers_mark",
            "curse_projectile_weakness",
            "curse_punishment",
            "curse_temporal_chains",
            "curse_vulnerability",
            "curse_warlords_mark",
        ],
        "Skill Configuration": [
            "ignite_mode",
            "aspect_of_the_avian_avians_might",
            "aspect_of_the_avian_avians_flight",
            "aspect_of_the_cat_cats_stealth",
            "aspect_of_the_cat_cats_agility",
            "banner_planted",
            "banner_stages",
            "stance",
            "wave_of_conviction_exposure_type",
            "winter_orb_stages",
            "intensify_stacks",
            "herald_of_agony_stacks",
        ],
        "Other": [
            "number_of_nearby_allies",
            "number_of_nearby_enemies",
            "number_of_nearby_corpses",
            "projectile_distance",
            "number_of_times_skill_has_chained",
        ],
    }

    # Print Character Level (from build, not config)
    print(f"Character Level: {build.level}")
    print()

    # Print config grouped by category
    printed_configs = set()
    for category, config_names in categories.items():
        category_configs = [
            (name, value) for name, value in config_with_values if name in config_names
        ]
        if category_configs:
            print(f"{category}:")
            for name, value in sorted(category_configs):
                display_name = name.replace("_", " ").title()
                print(f"  {display_name}: {value}")
                printed_configs.add(name)
            print()

    # Print any remaining configs that weren't categorized
    remaining_configs = [
        (name, value)
        for name, value in config_with_values
        if name not in printed_configs
    ]
    if remaining_configs:
        print("Other Configuration:")
        for name, value in sorted(remaining_configs):
            display_name = name.replace("_", " ").title()
            print(f"  {display_name}: {value}")
        print()


def main():
    """
    Build a demo PathOfBuildingAPI instance from embedded code and print its configuration.
    
    This function prepends the module's parent directory to sys.path to allow local imports, constructs a build using demo import code, and calls print_config to display the build's configuration.
    """
    import sys
    from pathlib import Path

    # Add parent directory to path to import from utils
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pobapi import from_import_code
    from utils.demo_pobapi import import_code

    build = from_import_code(import_code())
    print_config(build)


if __name__ == "__main__":
    main()