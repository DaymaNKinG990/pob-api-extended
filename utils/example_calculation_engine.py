"""Example usage of the Calculation Engine.

This script demonstrates how to use the Path of Building calculation engine
to calculate character statistics from a build.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from pobapi import CalculationEngine, from_import_code  # noqa: E402
from utils.demo_pobapi import import_code  # noqa: E402


def main():
    """Main function demonstrating calculation engine usage."""
    print("=" * 80)
    print("Path of Building Calculation Engine - Example Usage")
    print("=" * 80)
    print()

    # Load build from import code
    print("Loading build from import code...")
    build = from_import_code(import_code())
    print(f"Build loaded: {build.character_class} Level {build.level}")
    print()

    # Create calculation engine
    print("Initializing calculation engine...")
    engine = CalculationEngine()

    # Load build data into engine
    print("Loading build data (items, passive tree, skills, config)...")
    engine.load_build(build)
    print("Build data loaded successfully!")
    print()

    # Prepare calculation context
    print("Preparing calculation context...")
    context = {
        # Base stats (would come from character class and level)
        "base_life": 100.0,
        "base_mana": 50.0,
        "base_energy_shield": 0.0,
        "base_armour": 0.0,
        "base_evasion": 0.0,
        # Enemy configuration (from config)
        "enemy_fire_resist": 0.0,
        "enemy_cold_resist": 0.0,
        "enemy_lightning_resist": 0.0,
        "enemy_chaos_resist": 0.0,
    }

    # Add enemy configuration from build config if available
    try:
        config = build.config
        if config.enemy_fire_resist is not None:
            context["enemy_fire_resist"] = float(config.enemy_fire_resist)
        if config.enemy_cold_resist is not None:
            context["enemy_cold_resist"] = float(config.enemy_cold_resist)
        if config.enemy_lightning_resist is not None:
            context["enemy_lightning_resist"] = float(config.enemy_lightning_resist)
        if config.enemy_chaos_resist is not None:
            context["enemy_chaos_resist"] = float(config.enemy_chaos_resist)
    except AttributeError:
        pass

    print("Context prepared:")
    for key, value in context.items():
        print(f"  {key}: {value}")
    print()

    # Calculate all stats
    print("Calculating all character statistics...")
    stats = engine.calculate_all_stats(context, build_data=build)
    print("Calculation complete!")
    print()

    # Display results
    print("=" * 80)
    print("CALCULATED STATISTICS")
    print("=" * 80)
    print()

    # Defensive stats
    print("DEFENSIVE STATS:")
    print(f"  Life: {stats.life:.1f}" if stats.life else "  Life: N/A")
    print(f"  Mana: {stats.mana:.1f}" if stats.mana else "  Mana: N/A")
    print(
        f"  Energy Shield: {stats.energy_shield:.1f}"
        if stats.energy_shield
        else "  Energy Shield: N/A"
    )
    print(f"  Armour: {stats.armour:.1f}" if stats.armour else "  Armour: N/A")
    print(f"  Evasion: {stats.evasion:.1f}" if stats.evasion else "  Evasion: N/A")
    print(
        f"  Physical Damage Reduction: {stats.physical_damage_reduction:.1f}%"
        if stats.physical_damage_reduction
        else "  Physical Damage Reduction: N/A"
    )
    print(
        f"  Fire Resistance: {stats.fire_resistance:.1f}%"
        if stats.fire_resistance is not None
        else "  Fire Resistance: N/A"
    )
    print(
        f"  Cold Resistance: {stats.cold_resistance:.1f}%"
        if stats.cold_resistance is not None
        else "  Cold Resistance: N/A"
    )
    print(
        f"  Lightning Resistance: {stats.lightning_resistance:.1f}%"
        if stats.lightning_resistance is not None
        else "  Lightning Resistance: N/A"
    )
    print(
        f"  Chaos Resistance: {stats.chaos_resistance:.1f}%"
        if stats.chaos_resistance is not None
        else "  Chaos Resistance: N/A"
    )
    print()

    # Offensive stats
    print("OFFENSIVE STATS:")
    print(
        f"  Total DPS: {stats.total_dps:.1f}" if stats.total_dps else "  Total DPS: N/A"
    )
    print(
        f"  Average Hit: {stats.average_hit:.1f}"
        if stats.average_hit
        else "  Average Hit: N/A"
    )
    print(
        f"  Attack Speed: {stats.attack_speed:.2f}"
        if stats.attack_speed
        else "  Attack Speed: N/A"
    )
    print(
        f"  Cast Speed: {stats.cast_speed:.2f}"
        if stats.cast_speed
        else "  Cast Speed: N/A"
    )
    print(
        f"  Crit Chance: {stats.crit_chance:.2f}%"
        if stats.crit_chance is not None
        else "  Crit Chance: N/A"
    )
    print(
        f"  Crit Multiplier: {stats.crit_multiplier:.1f}%"
        if stats.crit_multiplier is not None
        else "  Crit Multiplier: N/A"
    )
    print(
        f"  Hit Chance: {stats.hit_chance}%"
        if stats.hit_chance is not None
        else "  Hit Chance: N/A"
    )
    print()

    # DoT stats
    if stats.total_dot or stats.ignite_dps or stats.poison_dps or stats.bleed_dps:
        print("DAMAGE OVER TIME:")
        if stats.total_dot:
            print(f"  Total DoT: {stats.total_dot:.1f}")
        if stats.ignite_dps:
            print(f"  Ignite DPS: {stats.ignite_dps:.1f}")
        if stats.poison_dps:
            print(f"  Poison DPS: {stats.poison_dps:.1f}")
        if stats.bleed_dps:
            print(f"  Bleed DPS: {stats.bleed_dps:.1f}")
        print()

    # Resource stats
    if (
        stats.life_regen
        or stats.mana_regen
        or stats.life_leech_rate_per_hit
        or stats.mana_leech_rate_per_hit
    ):
        print("RESOURCE STATS:")
        if stats.life_regen:
            print(f"  Life Regen: {stats.life_regen:.1f}/s")
        if stats.mana_regen:
            print(f"  Mana Regen: {stats.mana_regen:.1f}/s")
        if stats.life_leech_rate_per_hit:
            print(f"  Life Leech: {stats.life_leech_rate_per_hit:.1f}/s")
        if stats.mana_leech_rate_per_hit:
            print(f"  Mana Leech: {stats.mana_leech_rate_per_hit:.1f}/s")
        print()

    # Maximum hit taken
    if (
        stats.physical_maximum_hit_taken
        or stats.fire_maximum_hit_taken
        or stats.cold_maximum_hit_taken
    ):
        print("MAXIMUM HIT TAKEN:")
        if stats.physical_maximum_hit_taken:
            print(f"  Physical: {stats.physical_maximum_hit_taken:.1f}")
        if stats.fire_maximum_hit_taken:
            print(f"  Fire: {stats.fire_maximum_hit_taken:.1f}")
        if stats.cold_maximum_hit_taken:
            print(f"  Cold: {stats.cold_maximum_hit_taken:.1f}")
        if stats.lightning_maximum_hit_taken:
            print(f"  Lightning: {stats.lightning_maximum_hit_taken:.1f}")
        if stats.chaos_maximum_hit_taken:
            print(f"  Chaos: {stats.chaos_maximum_hit_taken:.1f}")
        print()

    # EHP
    if stats.total_effective_health_pool:
        print(f"Effective Health Pool (EHP): {stats.total_effective_health_pool:.1f}")
        print()

    # Attributes
    if stats.strength or stats.dexterity or stats.intelligence:
        print("ATTRIBUTES:")
        if stats.strength:
            print(f"  Strength: {stats.strength:.0f}")
        if stats.dexterity:
            print(f"  Dexterity: {stats.dexterity:.0f}")
        if stats.intelligence:
            print(f"  Intelligence: {stats.intelligence:.0f}")
        print()

    # Skill-specific stats
    if stats.area_of_effect_radius or stats.mana_cost or stats.skill_cooldown:
        print("SKILL STATS:")
        if stats.area_of_effect_radius:
            print(f"  Area of Effect Radius: {stats.area_of_effect_radius:.2f}")
        if stats.mana_cost:
            print(f"  Mana Cost: {stats.mana_cost:.1f}")
        if stats.mana_cost_per_second:
            print(f"  Mana Cost per Second: {stats.mana_cost_per_second:.1f}")
        if stats.skill_cooldown:
            print(f"  Skill Cooldown: {stats.skill_cooldown:.2f}s")
        print()

    print("=" * 80)
    print("Example completed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()
