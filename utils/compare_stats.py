#!/usr/bin/env python3
"""Compare stats from screenshots with what we extract from API."""

import dataclasses

from pobapi import from_import_code

# Load build
code = open("data/import_code.txt").read().strip()
build = from_import_code(code)
stats = build.stats

print("=" * 80)
print("Comparison: Screenshot Stats vs API Stats")
print("=" * 80)
print()

# Stats from screenshots (based on image descriptions)
screenshot_stats = {
    # Skill Damage
    "Average Damage": 927262.6,
    "Attack Rate": 7.25,
    "Crit Chance": 96.80,
    "Crit Multiplier": 505,
    "Hit Chance": 100,
    "Hit DPS": 6723391.7,
    "Bleed DPS": 411.1,
    "Poison DPS": 109.0,
    "Total DoT DPS": 466.4,
    "AoE Radius": 1.4,
    "Mana Cost": 37,
    "Mana Cost per second": 268.28,
    # Attributes
    "Strength": 117,
    "Strength Required": 148,
    "Dexterity": 258,
    "Intelligence": 152,
    "Intelligence Required": 188,
    # Life
    "Total Life": 3580,
    "%Inc Life from Tree": 100,
    "Life Regen": 71.6,
    "Life Leech/On Hit Rate": 874.8,
    # Mana
    "Total Mana": 747,
    "%Inc Mana from Tree": 8,
    "Unreserved Mana": 115,
    "Unreserved Mana %": 15,
    "Mana Regen": 13.1,
    "Mana Leech/On Hit Rate": 191.0,
    # Energy Shield
    "Energy Shield": 1413,
    "%Inc ES from Tree": 40,
    "ES Leech/On Hit Rate": 192.5,
    # Defense
    "Armour": 512,
    "Phys. Damage Reduction": 9,
    "Evasion rating": 11946,
    "%Inc Evasion from Tree": 23,
    "Evade Chance": 64,
    "Block Chance": 49,
    "Spell Suppression Chance": 100,
    # Resistances
    "Fire Resistance": 75,
    "Fire Resistance Over Cap": 73,
    "Cold Resistance": 75,
    "Cold Resistance Over Cap": 73,
    "Lightning Resistance": 75,
    "Lightning Resistance Over Cap": 92,
    "Chaos Resistance": -17,
    # Charges
    "Power Charges": 4,
    "Frenzy Charges": 3,
    "Endurance Charges": 0,
    # Other
    "Rage": 20,
    "Total Degen": 199.7,
    "Net Life Recovery": -128.1,
    "Net Mana Recovery": 13.1,
    "Movement Speed Modifier": 140,  # +140%
}

# Map screenshot stats to API fields
api_mapping = {
    "Average Damage": ("average_damage", stats.average_damage),
    "Attack Rate": ("cast_speed", stats.cast_speed),  # or attack_speed
    "Crit Chance": ("crit_chance", stats.crit_chance),
    "Crit Multiplier": ("crit_multiplier", stats.crit_multiplier),
    "Hit Chance": ("hit_chance", stats.hit_chance),
    "Hit DPS": ("total_dps", stats.total_dps),
    "Bleed DPS": ("bleed_dps", stats.bleed_dps),
    "Poison DPS": ("poison_dps", stats.poison_dps),
    "Total DoT DPS": ("total_dot", stats.total_dot),
    "AoE Radius": ("area_of_effect_radius", stats.area_of_effect_radius),
    "Mana Cost": ("mana_cost", stats.mana_cost),
    "Mana Cost per second": ("mana_cost_per_second", stats.mana_cost_per_second),
    "Strength": ("strength", stats.strength),
    "Strength Required": ("strength_required", stats.strength_required),
    "Dexterity": ("dexterity", stats.dexterity),
    "Intelligence": ("intelligence", stats.intelligence),
    "Intelligence Required": ("intelligence_required", stats.intelligence_required),
    "Total Life": ("life", stats.life),
    "%Inc Life from Tree": ("life_increased", stats.life_increased),
    "Life Regen": ("life_regen", stats.life_regen),
    "Life Leech/On Hit Rate": (
        "life_leech_rate_per_hit",
        stats.life_leech_rate_per_hit,
    ),
    "Total Mana": ("mana", stats.mana),
    "%Inc Mana from Tree": ("mana_increased", stats.mana_increased),
    "Unreserved Mana": ("mana_unreserved", stats.mana_unreserved),
    "Unreserved Mana %": ("mana_unreserved_percent", stats.mana_unreserved_percent),
    "Mana Regen": ("mana_regen", stats.mana_regen),
    "Mana Leech/On Hit Rate": (
        "mana_leech_rate_per_hit",
        stats.mana_leech_rate_per_hit,
    ),
    "Energy Shield": ("energy_shield", stats.energy_shield),
    "%Inc ES from Tree": ("energy_shield_increased", stats.energy_shield_increased),
    "ES Leech/On Hit Rate": (
        "energy_shield_leech_rate_per_hit",
        stats.energy_shield_leech_rate_per_hit,
    ),
    "Armour": ("armour", stats.armour),
    "Phys. Damage Reduction": (
        "physical_damage_reduction",
        stats.physical_damage_reduction,
    ),
    "Evasion rating": ("evasion", stats.evasion),
    "%Inc Evasion from Tree": ("evasion_increased", stats.evasion_increased),
    "Evade Chance": (
        "melee_evade_chance",
        stats.melee_evade_chance,
    ),  # or projectile_evade_chance
    "Block Chance": ("block_chance", stats.block_chance),
    "Spell Suppression Chance": (
        "spell_suppression_chance",
        stats.spell_suppression_chance,
    ),
    "Fire Resistance": ("fire_resistance", stats.fire_resistance),
    "Fire Resistance Over Cap": (
        "fire_resistance_over_cap",
        stats.fire_resistance_over_cap,
    ),
    "Cold Resistance": ("cold_resistance", stats.cold_resistance),
    "Cold Resistance Over Cap": (
        "cold_resistance_over_cap",
        stats.cold_resistance_over_cap,
    ),
    "Lightning Resistance": ("lightning_resistance", stats.lightning_resistance),
    "Lightning Resistance Over Cap": (
        "lightning_resistance_over_cap",
        stats.lightning_resistance_over_cap,
    ),
    "Chaos Resistance": ("chaos_resistance", stats.chaos_resistance),
    "Power Charges": ("power_charges", stats.power_charges),
    "Frenzy Charges": ("frenzy_charges", stats.frenzy_charges),
    "Endurance Charges": ("endurance_charges", stats.endurance_charges),
    "Rage": ("rage", stats.rage),
    "Total Degen": ("total_degen", stats.total_degen),
    "Net Life Recovery": ("net_life_regen", stats.net_life_regen),
    "Net Mana Recovery": ("net_mana_regen", stats.net_mana_regen),
    "Movement Speed Modifier": (
        "effective_movement_speed_modifier",
        stats.effective_movement_speed_modifier,
    ),
}

print("Checking stats from screenshots:")
print()

matched = []
missing = []
different = []

for screenshot_name, screenshot_value in screenshot_stats.items():
    if screenshot_name in api_mapping:
        api_field, api_value = api_mapping[screenshot_name]

        if api_value is None:
            missing.append((screenshot_name, screenshot_value, api_field))
        else:
            # Compare values (allow small floating point differences)
            if isinstance(screenshot_value, float) and isinstance(
                api_value, int | float
            ):
                diff = abs(screenshot_value - float(api_value))
                if diff < 0.1:  # Allow small differences
                    matched.append((screenshot_name, screenshot_value, api_value))
                else:
                    different.append(
                        (screenshot_name, screenshot_value, api_value, diff)
                    )
            elif screenshot_value == api_value:
                matched.append((screenshot_name, screenshot_value, api_value))
            else:
                different.append(
                    (
                        screenshot_name,
                        screenshot_value,
                        api_value,
                        abs(screenshot_value - float(api_value)),
                    )
                )
    else:
        missing.append((screenshot_name, screenshot_value, "NOT MAPPED"))

print(f"[OK] Matched: {len(matched)}")
for name, screenshot_val, api_val in matched[:10]:
    print(f"  {name}: {screenshot_val} == {api_val}")
if len(matched) > 10:
    print(f"  ... and {len(matched) - 10} more")

print()
print(f"[DIFF] Different values: {len(different)}")
for name, screenshot_val, api_val, diff in different:
    print(f"  {name}: Screenshot={screenshot_val}, API={api_val}, Diff={diff:.2f}")

print()
print(f"[MISSING] Missing/Not mapped: {len(missing)}")
for name, screenshot_val, api_field in missing:
    print(f"  {name}: Screenshot={screenshot_val}, API field={api_field}")

print()
print("=" * 80)
print("Checking for additional stats in API not shown in screenshots:")
print("=" * 80)

# Get all stats fields
all_fields = dataclasses.fields(stats)
all_values = {
    f.name: getattr(stats, f.name)
    for f in all_fields
    if getattr(stats, f.name) is not None
}

print(f"\nTotal stats fields in API: {len(all_fields)}")
print(f"Stats with values: {len(all_values)}")
print("\nStats with values (not in screenshots):")
for field_name, value in sorted(all_values.items()):
    if field_name not in [m[1] for m in api_mapping.values()]:
        print(f"  {field_name}: {value}")
