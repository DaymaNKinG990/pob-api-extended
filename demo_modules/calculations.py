"""Module for displaying all calculated build information."""

from pobapi import PathOfBuildingAPI
from pobapi.calculator.engine import CalculationEngine


def print_calculations(build: PathOfBuildingAPI) -> None:
    """
    Print a comprehensive, PoB-style report of calculated build statistics to stdout.
    
    Generates a detailed human-readable breakdown (attributes, life/mana/ES, defenses,
    resists, damage, skill-specific stats, minion stats, modifier sources, etc.) by
    loading the provided PathOfBuildingAPI build into the CalculationEngine and
    querying its calculators.
    
    Parameters:
        build (PathOfBuildingAPI): The PoB build to evaluate and display.
    """
    print("=" * 80)
    print("  Calculated Build Information")
    print("=" * 80)
    print()

    # Initialize calculation engine
    engine = CalculationEngine()
    engine.load_build(build)

    # Prepare context from config
    context = {}
    if build.config:
        config = build.config
        if config.enemy_level is not None:
            context["enemy_level"] = config.enemy_level
        if config.enemy_fire_resist is not None:
            context["enemy_fire_resist"] = float(config.enemy_fire_resist)
        if config.enemy_cold_resist is not None:
            context["enemy_cold_resist"] = float(config.enemy_cold_resist)
        if config.enemy_lightning_resist is not None:
            context["enemy_lightning_resist"] = float(config.enemy_lightning_resist)
        if config.enemy_chaos_resist is not None:
            context["enemy_chaos_resist"] = float(config.enemy_chaos_resist)
        if config.enemy_physical_damage_reduction is not None:
            context["enemy_physical_damage_reduction"] = float(
                config.enemy_physical_damage_reduction
            )

    # Calculate all stats (not used in this demo, but available)
    # calculated_stats = engine.calculate_all_stats(context, build)

    # Calculate defense stats separately for detailed breakdown
    defense_stats = engine.defense_calc.calculate_all_defenses(context)

    # Print Skill Details Section (if active skill exists)
    if build.active_skill_group and build.active_skill_group.abilities:
        try:
            active_skill_group = build.active_skill_group
            active_skill = active_skill_group.abilities[
                (active_skill_group.active or 1) - 1
            ]
            if active_skill:
                print("View Skill Details:")
                print("-" * 80)
                print(f"  Socket Group: {active_skill_group.label or 'Unnamed'}")
                print(f"  Active Skill: {active_skill.name}")
                if hasattr(active_skill, "level"):
                    print(f"  Gem Level: {active_skill.level}")
                if hasattr(active_skill, "quality"):
                    print(f"  Gem Quality: {active_skill.quality}")
                print("  Calculation Mode: Effective DPS")
                print()

                # Aura and Buff Skills
                if build.config:
                    config = build.config
                    auras = []
                    if config.hatred:
                        auras.append("Hatred")
                    if config.anger:
                        auras.append("Anger")
                    if config.wrath:
                        auras.append("Wrath")
                    if config.grace:
                        auras.append("Grace")
                    if config.determination:
                        auras.append("Determination")
                    if config.discipline:
                        auras.append("Discipline")
                    if config.precision:
                        auras.append("Precision")
                    if auras:
                        print(f"  Aura and Buff Skills: {', '.join(auras)}")

                    # Combat Buffs
                    buffs = []
                    if config.use_power_charges:
                        max_charges = config.max_power_charges or 0
                        buffs.append(f"{max_charges} Power Charges")
                    if config.use_frenzy_charges:
                        max_charges = config.max_frenzy_charges or 0
                        buffs.append(f"{max_charges} Frenzy Charges")
                    if config.use_endurance_charges:
                        max_charges = config.max_endurance_charges or 0
                        buffs.append(f"{max_charges} Endurance Charges")
                    if config.onslaught:
                        buffs.append("Onslaught")
                    if config.tailwind:
                        buffs.append("Tailwind")
                    if config.fortify:
                        buffs.append("Fortify")
                    if config.adrenaline:
                        buffs.append("Adrenaline")
                    if buffs:
                        print(f"  Combat Buffs: {', '.join(buffs)}")

                    # Curses and Debuffs
                    curses = []
                    if config.curse_flammability:
                        curses.append("Flammability")
                    if config.curse_frostbite:
                        curses.append("Frostbite")
                    if config.curse_conductivity:
                        curses.append("Conductivity")
                    if config.curse_elemental_weakness:
                        curses.append("Elemental Weakness")
                    if config.curse_vulnerability:
                        curses.append("Vulnerability")
                    if config.curse_assassins_mark:
                        curses.append("Assassin's Mark")
                    if curses:
                        print(f"  Curses and Debuffs: {', '.join(curses)}")
                print()
        except (AttributeError, IndexError):
            pass

    # Print Attributes with Requirements
    print("Attributes:")
    print("-" * 80)
    strength = engine.modifiers.calculate_stat("Strength", 0.0, context)
    dexterity = engine.modifiers.calculate_stat("Dexterity", 0.0, context)
    intelligence = engine.modifiers.calculate_stat("Intelligence", 0.0, context)
    strength_required = engine.modifiers.calculate_stat(
        "StrengthRequired", 0.0, context
    )
    dexterity_required = engine.modifiers.calculate_stat(
        "DexterityRequired", 0.0, context
    )
    intelligence_required = engine.modifiers.calculate_stat(
        "IntelligenceRequired", 0.0, context
    )
    print(f"  Strength: {strength:.0f}")
    if strength_required > 0:
        print(f"  Str. Required: {strength_required:.0f}")
    print(f"  Dexterity: {dexterity:.0f}")
    if dexterity_required > 0:
        print(f"  Dex. Required: {dexterity_required:.0f}")
    print(f"  Intelligence: {intelligence:.0f}")
    if intelligence_required > 0:
        print(f"  Int. Required: {intelligence_required:.0f}")
    print()

    # Print Life with detailed breakdown
    print("Life:")
    print("-" * 80)
    # Get modifiers for life breakdown
    life_base = context.get("base_life", 0.0)
    # Get flat life from modifiers
    life_modifiers = engine.modifiers.get_modifiers("Life", context)
    life_flat = sum(mod.value for mod in life_modifiers if mod.mod_type.value == "flat")
    life_increased = sum(
        mod.value for mod in life_modifiers if mod.mod_type.value == "increased"
    )
    total_more = engine.modifiers.calculate_stat("LifeMore", 0.0, context)
    total_life = defense_stats.life
    life_unreserved = engine.resource_calc.calculate_unreserved_life(
        total_life, context
    )
    life_regen = engine.defense_calc.calculate_life_regen(context)
    total_base = life_base + life_flat
    print(f"  Base from Gear: {life_flat:.0f}")
    print(f"  Inc. from Tree: {life_increased:.0f}%")
    print(f"  Total Base: {total_base:.0f}")
    print(f"  Total Increased: {life_increased:.0f}%")
    print(f"  Total More: {total_more:.0f}%")
    print(f"  Total: {total_life:.0f}")
    reserved_pct = (
        ((total_life - life_unreserved) / total_life * 100) if total_life > 0 else 0
    )
    print(f"  Reserved: {total_life - life_unreserved:.0f} ({reserved_pct:.0f}%)")
    print(
        f"  Unreserved: {life_unreserved:.0f} "
        f"({((life_unreserved / total_life) * 100) if total_life > 0 else 0:.0f}%)"
    )
    if life_regen > 0:
        print(
            f"  Recovery: {life_regen:.1f} "
            f"({((life_regen / total_life) * 100) if total_life > 0 else 0:.1f}%)"
        )
    print()

    # Print Mana with detailed breakdown
    print("Mana:")
    print("-" * 80)
    mana_base = context.get("base_mana", 0.0)
    # Get flat mana from modifiers
    mana_modifiers = engine.modifiers.get_modifiers("Mana", context)
    mana_flat = sum(mod.value for mod in mana_modifiers if mod.mod_type.value == "flat")
    mana_increased = sum(
        mod.value for mod in mana_modifiers if mod.mod_type.value == "increased"
    )
    total_mana_base = mana_base + mana_flat
    total_mana = defense_stats.mana
    mana_unreserved = engine.resource_calc.calculate_unreserved_mana(
        total_mana, context
    )
    mana_regen = engine.defense_calc.calculate_mana_regen(context)
    print(f"  Base from Gear: {mana_flat:.0f}")
    print(f"  Inc. from Tree: {mana_increased:.0f}%")
    print(f"  Total Base: {total_mana_base:.0f}")
    print(f"  Total Increased: {mana_increased:.0f}%")
    print(f"  Total: {total_mana:.0f}")
    reserved_pct = (
        ((total_mana - mana_unreserved) / total_mana * 100) if total_mana > 0 else 0
    )
    print(f"  Reserved: {total_mana - mana_unreserved:.0f} ({reserved_pct:.0f}%)")
    print(
        f"  Unreserved: {mana_unreserved:.0f} "
        f"({((mana_unreserved / total_mana) * 100) if total_mana > 0 else 0:.0f}%)"
    )
    if mana_regen > 0:
        print(
            f"  Recovery: {mana_regen:.1f} "
            f"({((mana_regen / total_mana) * 100) if total_mana > 0 else 0:.1f}%)"
        )
    print()

    # Print Energy Shield with detailed breakdown
    print("Energy Shield:")
    print("-" * 80)
    es_base = context.get("base_energy_shield", 0.0)
    # Get flat ES from modifiers
    es_modifiers = engine.modifiers.get_modifiers("EnergyShield", context)
    es_flat = sum(mod.value for mod in es_modifiers if mod.mod_type.value == "flat")
    es_increased = sum(
        mod.value for mod in es_modifiers if mod.mod_type.value == "increased"
    )
    # total_es_base = es_base + es_flat  # Not used
    total_es_more = engine.modifiers.calculate_stat("EnergyShieldMore", 0.0, context)
    total_es = defense_stats.energy_shield
    es_regen = engine.defense_calc.calculate_energy_shield_regen(context)
    print(f"  Base from Armours: {es_flat:.0f}")
    print(f"  Global Base: {es_base:.0f}")
    print(f"  Inc. from Tree: {es_increased:.0f}%")
    print(f"  Total Increased: {es_increased:.0f}%")
    print(f"  Total More: {total_es_more:.0f}%")
    print(f"  Total: {total_es:.0f}")
    if es_regen > 0:
        print(f"  Recharge Rate: {es_regen:.0f}")
        print("  Recharge Delay: 2s")
        print(
            f"  Recovery: {es_regen:.1f} "
            f"({((es_regen / total_es) * 100) if total_es > 0 else 0:.1f}%)"
        )
    print()

    # Print Resistances with over cap
    print("Resists:")
    print("-" * 80)
    fire_res = defense_stats.fire_resistance
    cold_res = defense_stats.cold_resistance
    lightning_res = defense_stats.lightning_resistance
    chaos_res = defense_stats.chaos_resistance
    fire_over_cap = max(0, fire_res - 75.0)
    cold_over_cap = max(0, cold_res - 75.0)
    lightning_over_cap = max(0, lightning_res - 75.0)
    chaos_over_cap = max(0, chaos_res - 75.0)
    print(f"  Fire Resist: {min(fire_res, 75.0):.0f}% (+{fire_over_cap:.0f}%)")
    print(f"  Cold Resist: {min(cold_res, 75.0):.0f}% (+{cold_over_cap:.0f}%)")
    print(
        f"  Lightning Resist: {min(lightning_res, 75.0):.0f}% "
        f"(+{lightning_over_cap:.0f}%)"
    )
    print(f"  Chaos Resist: {min(chaos_res, 75.0):.0f}% (+{chaos_over_cap:.0f}%)")
    print()

    # Print Armour with breakdown
    print("Armour:")
    print("-" * 80)
    armour_base = context.get("base_armour", 0.0)
    # Get flat armour from modifiers
    armour_modifiers = engine.modifiers.get_modifiers("Armour", context)
    armour_flat = sum(
        mod.value for mod in armour_modifiers if mod.mod_type.value == "flat"
    )
    armour_increased = sum(
        mod.value for mod in armour_modifiers if mod.mod_type.value == "increased"
    )
    # total_armour_base = armour_base + armour_flat  # Not used
    total_armour_more = engine.modifiers.calculate_stat("ArmourMore", 0.0, context)
    total_armour = defense_stats.armour
    print(f"  Base from Armours: {armour_flat:.0f}")
    print(f"  Global Base: {armour_base:.0f}")
    print(f"  Inc. from Tree: {armour_increased:.0f}%")
    print(f"  Total Increased: {armour_increased:.0f}%")
    print(f"  Total More: {total_armour_more:.0f}%")
    print(f"  Total: {total_armour:.0f}")
    if total_armour > 0:
        physical_reduction = engine.defense_calc.calculate_physical_damage_reduction(
            1000.0, context
        )
        print(f"  Phys. Dmg. Reduct: {physical_reduction * 100:.0f}%")
    print()

    # Print Evasion with breakdown
    print("Evasion:")
    print("-" * 80)
    evasion_base = context.get("base_evasion", 0.0)
    # Get flat evasion from modifiers
    evasion_modifiers = engine.modifiers.get_modifiers("Evasion", context)
    evasion_flat = sum(
        mod.value for mod in evasion_modifiers if mod.mod_type.value == "flat"
    )
    evasion_increased = sum(
        mod.value for mod in evasion_modifiers if mod.mod_type.value == "increased"
    )
    # total_evasion_base = evasion_base + evasion_flat  # Not used
    total_evasion_more = engine.modifiers.calculate_stat("EvasionMore", 0.0, context)
    total_evasion = defense_stats.evasion
    print(f"  Base from Armours: {evasion_flat:.0f}")
    print(f"  Global Base: {evasion_base:.0f}")
    print(f"  Inc. from Tree: {evasion_increased:.0f}%")
    print(f"  Total Increased: {evasion_increased:.0f}%")
    print(f"  Total More: {total_evasion_more:.0f}%")
    print(f"  Total: {total_evasion:.0f}")
    if total_evasion > 0:
        evade_chance = engine.defense_calc.calculate_evade_chance(1000.0, context)
        print(f"  Evade Chance: {evade_chance * 100:.0f}%")
    print()

    # Print Damage Avoidance
    print("Damage Avoidance:")
    print("-" * 80)
    block_chance = defense_stats.block_chance
    spell_block_chance = defense_stats.spell_block_chance
    dodge_chance = engine.modifiers.calculate_stat("DodgeChance", 0.0, context)
    spell_dodge_chance = engine.modifiers.calculate_stat(
        "SpellDodgeChance", 0.0, context
    )
    spell_suppression = defense_stats.spell_suppression_chance
    print(f"  Block: {block_chance:.0f}%/{spell_block_chance:.0f}%")
    print(f"    Block Chance: {block_chance:.0f}% (+0%)")
    print(f"    Spell Block Chance: {spell_block_chance:.0f}% (+0%)")
    print(f"  Dodge: {dodge_chance:.0f}%/{spell_dodge_chance:.0f}%")
    print(f"    Dodge Chance: {dodge_chance:.0f}% (+0%)")
    print(f"    Spell Ddg. Chance: {spell_dodge_chance:.0f}% (+0%)")
    print(f"  Spell Suppression: {spell_suppression:.0f}%")
    print(f"    Suppression Ch.: {spell_suppression:.0f}% (+0%)")
    suppression_effect = engine.modifiers.calculate_stat(
        "SpellSuppressionEffect", 50.0, context
    )
    print(f"    Suppression Effect: {suppression_effect:.0f}%")
    print()

    # Print Charges
    print("Charges:")
    print("-" * 80)
    if build.config:
        config = build.config
        power_charges = config.max_power_charges or 0 if config.use_power_charges else 0
        frenzy_charges = (
            config.max_frenzy_charges or 0 if config.use_frenzy_charges else 0
        )
        endurance_charges = (
            config.max_endurance_charges or 0 if config.use_endurance_charges else 0
        )
        print(f"  Power Charges: {power_charges}")
        print(f"  Frenzy Charges: {frenzy_charges}")
        print(f"  Endurance Charges: {endurance_charges}")
    print()

    # Print Maximum Hit Taken
    print("Maximum Hit Taken:")
    print("-" * 80)
    physical_max = engine.defense_calc.calculate_maximum_hit_taken("Physical", context)
    fire_max = engine.defense_calc.calculate_maximum_hit_taken("Fire", context)
    cold_max = engine.defense_calc.calculate_maximum_hit_taken("Cold", context)
    lightning_max = engine.defense_calc.calculate_maximum_hit_taken(
        "Lightning", context
    )
    chaos_max = engine.defense_calc.calculate_maximum_hit_taken("Chaos", context)
    print(f"  Physical: {physical_max:.0f}")
    print(f"  Fire: {fire_max:.0f}")
    print(f"  Cold: {cold_max:.0f}")
    print(f"  Lightning: {lightning_max:.0f}")
    print(f"  Chaos: {chaos_max:.0f}")
    print()

    # Print Effective Health Pool
    ehp = engine.defense_calc.calculate_effective_health_pool(context)
    print("Effective Health Pool:")
    print("-" * 80)
    print(f"  Effective Hit Pool: {ehp:.0f}")
    total_pool = defense_stats.life + defense_stats.energy_shield
    if total_pool > 0:
        mitigated_pct = (ehp / total_pool) * 100.0 if total_pool > 0 else 0.0
        print(f"  Unmitigated %: {100.0 - mitigated_pct:.0f}%")
    print()

    # Print Regeneration
    print("Regeneration:")
    print("-" * 80)
    life_regen = engine.defense_calc.calculate_life_regen(context)
    mana_regen = engine.defense_calc.calculate_mana_regen(context)
    es_regen = engine.defense_calc.calculate_energy_shield_regen(context)
    print(f"  Life Regeneration: {life_regen:.2f}/s")
    print(f"  Mana Regeneration: {mana_regen:.2f}/s")
    print(f"  Energy Shield Regeneration: {es_regen:.2f}/s")
    print()

    # Print Leech Rates
    leech_rates = engine.defense_calc.calculate_leech_rates(context)
    if (
        leech_rates.get("life_leech_rate", 0.0) > 0
        or leech_rates.get("mana_leech_rate", 0.0) > 0
        or leech_rates.get("energy_shield_leech_rate", 0.0) > 0
    ):
        print("Leech & Gain on Hit:")
        print("-" * 80)
        life_gain_on_kill = engine.modifiers.calculate_stat(
            "LifeGainOnKill", 0.0, context
        )
        if life_gain_on_kill > 0:
            print(f"  Life Gain on Kill: {life_gain_on_kill:.0f}")
        if leech_rates.get("energy_shield_leech_rate", 0.0) > 0:
            es_leech_cap = engine.modifiers.calculate_stat(
                "EnergyShieldLeechCap", 0.0, context
            )
            print(f"  ES Leech Cap: {es_leech_cap:.1f}")
            print(
                f"  ES Leech per Hit: "
                f"{leech_rates.get('energy_shield_leech_rate', 0.0):.1f}"
            )
        es_gain_on_kill = engine.modifiers.calculate_stat(
            "EnergyShieldGainOnKill", 0.0, context
        )
        if es_gain_on_kill > 0:
            print(f"  ES Gain on Kill: {es_gain_on_kill:.0f}")
        print()

    # Print Speed Stats
    print("Speed Stats:")
    print("-" * 80)
    attack_speed = engine.modifiers.calculate_stat("AttackSpeed", 1.0, context)
    cast_speed = engine.modifiers.calculate_stat("CastSpeed", 1.0, context)
    movement_speed = engine.modifiers.calculate_stat("MovementSpeed", 1.0, context)
    print(f"  Attack Speed: {attack_speed:.2f}")
    print(f"  Cast Speed: {cast_speed:.2f}")
    print(f"  Movement Speed: {movement_speed:.2f}x")
    print()

    # Print Critical Strike Stats
    print("Crits:")
    print("-" * 80)
    inc_crit_chance = engine.modifiers.calculate_stat("CritChance", 0.0, context)
    crit_chance = engine.modifiers.calculate_stat("CritChance", 0.0, context)
    crit_multiplier = engine.modifiers.calculate_stat("CritMultiplier", 150.0, context)
    crit_effect_mod = (
        engine.modifiers.calculate_stat("CritEffect", 100.0, context) / 100.0
    )
    print(f"  Inc. Crit Chance: {inc_crit_chance:.0f}%")
    print(f"  Crit Chance: {crit_chance:.1f}%")
    print(f"  Crit Multiplier: x {crit_multiplier / 100.0:.2f}")
    print(f"  Crit Effect Mod: x {crit_effect_mod:.3f}")
    print()

    # Print Other Effects
    print("Other Effects:")
    print("-" * 80)
    stun_threshold = engine.modifiers.calculate_stat("StunThreshold", 0.0, context)
    stun_duration = engine.modifiers.calculate_stat("StunDuration", 0.0, context)
    item_quantity = engine.modifiers.calculate_stat("ItemQuantity", 0.0, context)
    item_rarity = engine.modifiers.calculate_stat("ItemRarity", 0.0, context)
    culling_strike = engine.modifiers.calculate_stat("CullingStrike", 0.0, context)
    if stun_threshold > 0:
        print(f"  Stun Threshold: x {stun_threshold:.0f}")
    if stun_duration > 0:
        print(f"  Stun Duration: {stun_duration:.2f}s")
    if item_quantity > 0:
        print(f"  Inc. Item Quantity: {item_quantity:.0f}%")
    if item_rarity > 0:
        print(f"  Inc. Item Rarity: {item_rarity:.0f}%")
    if culling_strike > 0:
        print(f"  Culling Strike: {culling_strike:.0f}%")
    print()

    # Print Other Defences
    print("Other Defences:")
    print("-" * 80)
    curse_effect = engine.modifiers.calculate_stat("CurseEffectOnYou", 0.0, context)
    exposure_effect = engine.modifiers.calculate_stat("ExposureEffect", 100.0, context)
    wither_effect = engine.modifiers.calculate_stat("WitherEffect", 100.0, context)
    debuff_duration_mult = (
        engine.modifiers.calculate_stat("DebuffDuration", 100.0, context) / 100.0
    )
    print(f"  Movement Speed: x {movement_speed:.2f}")
    light_radius_mod = engine.modifiers.calculate_stat("LightRadius", 1.0, context)
    print(f"  Light Radius Mod: x {light_radius_mod:.0f}")
    if curse_effect != 0:
        print(f"  Curse Effect on You: {curse_effect:.0f}%")
    print(f"  Exposure Effect: {exposure_effect:.0f}%")
    print(f"  Wither Effect: {wither_effect:.0f}%")
    print(f"  Debuff Dur. Mult.: {debuff_duration_mult * 100:.1f}%")
    print()

    # Print Stun Duration
    print("Stun Duration:")
    print("-" * 80)
    stun_avoid_chance = engine.modifiers.calculate_stat("StunAvoidChance", 0.0, context)
    stun_chance = 100.0 - stun_avoid_chance if stun_avoid_chance < 100.0 else 0.0
    block_stun_duration = engine.modifiers.calculate_stat(
        "BlockStunDuration", 0.0, context
    )
    print(f"  Stun Avoid Chance: {stun_avoid_chance:.0f}%")
    if stun_threshold > 0:
        print(f"  Stun Threshold: {stun_threshold:.0f}")
    print(f"  Stun Chance: {stun_chance:.0f}%")
    if stun_duration > 0:
        print(f"  Stun Duration: {stun_duration:.2f}s")
    if block_stun_duration > 0:
        print(f"  Block Stun Duration: {block_stun_duration:.2f}s")
    print()

    # Print Skill-Specific Stats (if active skill exists)
    if build.active_skill_group and build.active_skill_group.abilities:
        try:
            active_skill = build.active_skill_group.abilities[
                (build.active_skill_group.active or 1) - 1
            ]
            if active_skill:
                skill_name = active_skill.name
                print(f"Active Skill: {skill_name}")
                print("-" * 80)

                # Skill type-specific Stats
                if hasattr(active_skill, "level"):
                    print(f"  Gem Level: {active_skill.level}")
                if hasattr(active_skill, "quality"):
                    print(f"  Gem Quality: {active_skill.quality}")

                # Mana Cost
                mana_cost = engine.resource_calc.calculate_mana_cost(
                    skill_name, context
                )
                mana_cost_per_second = (
                    engine.resource_calc.calculate_mana_cost_per_second(
                        skill_name, context
                    )
                )
                print(f"  Mana Cost: {mana_cost:.0f}")
                print(f"  Mana Cost per Second: {mana_cost_per_second:.1f}")

                # Duration Modifiers
                duration_mod = (
                    engine.modifiers.calculate_stat("SkillDuration", 100.0, context)
                    / 100.0
                )
                skill_duration = engine.modifiers.calculate_stat(
                    f"{skill_name}Duration", 0.0, context
                )
                if duration_mod != 1.0:
                    print(f"  Duration Mod: x {duration_mod:.2f}")
                if skill_duration > 0:
                    print(f"  Skill Duration: {skill_duration:.3f}s")

                # Reserve Modifiers
                mana_reserve_mod = (
                    engine.modifiers.calculate_stat("ManaReservation", 100.0, context)
                    / 100.0
                )
                life_reserve_mod = (
                    engine.modifiers.calculate_stat("LifeReservation", 100.0, context)
                    / 100.0
                )
                if mana_reserve_mod != 1.0:
                    print(f"  Mana Reserve Mod: x {mana_reserve_mod:.2f}")
                if life_reserve_mod != 1.0:
                    print(f"  Life Reserve Mod: x {life_reserve_mod:.2f}")

                # Area of Effect
                aoe_radius = engine.skill_stats_calc.calculate_area_of_effect_radius(
                    skill_name, 1.0, context
                )
                aoe_mod = (
                    engine.modifiers.calculate_stat("AreaOfEffect", 100.0, context)
                    / 100.0
                )
                if aoe_mod != 1.0:
                    print(f"  Area of Effect Mod: x {aoe_mod:.2f}")
                print(f"  Radius: {aoe_radius:.1f}m")

                # Projectile Count
                projectile_count = engine.skill_stats_calc.calculate_projectile_count(
                    skill_name, 1, context
                )
                print(f"  Projectile Count: {projectile_count:.0f}")

                # Projectile Speed
                projectile_speed = engine.skill_stats_calc.calculate_projectile_speed(
                    skill_name, 1.0, context
                )
                print(f"  Projectile Speed: {projectile_speed:.2f}")

                # Cooldowns
                skill_cooldown = engine.skill_stats_calc.calculate_skill_cooldown(
                    skill_name, 0.0, context
                )
                if skill_cooldown > 0:
                    print(f"  Skill Cooldown: {skill_cooldown:.2f}s")

                trap_cooldown = engine.skill_stats_calc.calculate_trap_cooldown(context)
                if trap_cooldown > 0:
                    print(f"  Trap Cooldown: {trap_cooldown:.2f}s")

                mine_cooldown = engine.skill_stats_calc.calculate_mine_cooldown(context)
                if mine_cooldown > 0:
                    print(f"  Mine Cooldown: {mine_cooldown:.2f}s")

                totem_placement = (
                    engine.skill_stats_calc.calculate_totem_placement_time(context)
                )
                if totem_placement > 0:
                    print(f"  Totem Placement Time: {totem_placement:.2f}s")

                print()

                # Skill Hit Damage - Detailed Breakdown
                print("Skill Hit Damage:")
                print("-" * 80)

                # Get base damage
                base_damage = engine.damage_calc.calculate_base_damage(
                    skill_name, context
                )

                # Get added damage modifiers
                added_phys_min = engine.modifiers.calculate_stat(
                    f"{skill_name}AddedPhysicalDamageMin", 0.0, context
                )
                added_phys_max = engine.modifiers.calculate_stat(
                    f"{skill_name}AddedPhysicalDamageMax", 0.0, context
                )
                added_fire_min = engine.modifiers.calculate_stat(
                    f"{skill_name}AddedFireDamageMin", 0.0, context
                )
                added_fire_max = engine.modifiers.calculate_stat(
                    f"{skill_name}AddedFireDamageMax", 0.0, context
                )
                added_cold_min = engine.modifiers.calculate_stat(
                    f"{skill_name}AddedColdDamageMin", 0.0, context
                )
                added_cold_max = engine.modifiers.calculate_stat(
                    f"{skill_name}AddedColdDamageMax", 0.0, context
                )
                added_lightning_min = engine.modifiers.calculate_stat(
                    f"{skill_name}AddedLightningDamageMin", 0.0, context
                )
                added_lightning_max = engine.modifiers.calculate_stat(
                    f"{skill_name}AddedLightningDamageMax", 0.0, context
                )
                added_chaos_min = engine.modifiers.calculate_stat(
                    f"{skill_name}AddedChaosDamageMin", 0.0, context
                )
                added_chaos_max = engine.modifiers.calculate_stat(
                    f"{skill_name}AddedChaosDamageMax", 0.0, context
                )

                # Get increased and more modifiers
                total_increased_all = engine.modifiers.calculate_stat(
                    "Damage", 0.0, context
                )
                total_increased_phys = engine.modifiers.calculate_stat(
                    "PhysicalDamage", 0.0, context
                )
                total_increased_fire = engine.modifiers.calculate_stat(
                    "FireDamage", 0.0, context
                )
                total_increased_cold = engine.modifiers.calculate_stat(
                    "ColdDamage", 0.0, context
                )
                total_increased_lightning = engine.modifiers.calculate_stat(
                    "LightningDamage", 0.0, context
                )
                total_increased_chaos = engine.modifiers.calculate_stat(
                    "ChaosDamage", 0.0, context
                )

                total_more_all = engine.modifiers.calculate_stat(
                    "DamageMore", 0.0, context
                )
                total_more_phys = engine.modifiers.calculate_stat(
                    "PhysicalDamageMore", 0.0, context
                )
                total_more_fire = engine.modifiers.calculate_stat(
                    "FireDamageMore", 0.0, context
                )
                total_more_cold = engine.modifiers.calculate_stat(
                    "ColdDamageMore", 0.0, context
                )
                total_more_lightning = engine.modifiers.calculate_stat(
                    "LightningDamageMore", 0.0, context
                )
                total_more_chaos = engine.modifiers.calculate_stat(
                    "ChaosDamageMore", 0.0, context
                )

                # Calculate final damage after all modifiers
                final_damage = engine.damage_calc.calculate_average_hit(
                    skill_name, context
                )
                damage_breakdown = engine.damage_calc.calculate_base_damage(
                    skill_name, context
                )
                damage_breakdown = engine.damage_calc._apply_extra_damage(
                    damage_breakdown, skill_name, context
                )
                damage_breakdown = engine.damage_calc._apply_damage_multipliers(
                    damage_breakdown, skill_name, context
                )

                print("  Added Min:")
                print(f"    Physical: {added_phys_min:.0f}")
                print(f"    Fire: {added_fire_min:.0f}")
                print(f"    Cold: {added_cold_min:.0f}")
                print(f"    Lightning: {added_lightning_min:.0f}")
                print(f"    Chaos: {added_chaos_min:.0f}")
                print("  Added Max:")
                print(f"    Physical: {added_phys_max:.0f}")
                print(f"    Fire: {added_fire_max:.0f}")
                print(f"    Cold: {added_cold_max:.0f}")
                print(f"    Lightning: {added_lightning_max:.0f}")
                print(f"    Chaos: {added_chaos_max:.0f}")
                print("  Total Increased:")
                print(f"    All Types: {total_increased_all:.0f}%")
                print(f"    Physical: {total_increased_phys:.0f}%")
                print(f"    Fire: {total_increased_fire:.0f}%")
                print(f"    Cold: {total_increased_cold:.0f}%")
                print(f"    Lightning: {total_increased_lightning:.0f}%")
                print(f"    Chaos: {total_increased_chaos:.0f}%")
                print("  Total More:")
                print(f"    All Types: {total_more_all:.0f}%")
                print(f"    Physical: {total_more_phys:.0f}%")
                print(f"    Fire: {total_more_fire:.0f}%")
                print(f"    Cold: {total_more_cold:.0f}%")
                print(f"    Lightning: {total_more_lightning:.0f}%")
                print(f"    Chaos: {total_more_chaos:.0f}%")
                print("  Skill Hit Damage:")
                # Calculate min/max from base + added
                phys_min = base_damage.physical + added_phys_min
                phys_max = base_damage.physical + added_phys_max
                fire_min = base_damage.fire + added_fire_min
                fire_max = base_damage.fire + added_fire_max
                cold_min = base_damage.cold + added_cold_min
                cold_max = base_damage.cold + added_cold_max
                lightning_min = base_damage.lightning + added_lightning_min
                lightning_max = base_damage.lightning + added_lightning_max
                chaos_min = base_damage.chaos + added_chaos_min
                chaos_max = base_damage.chaos + added_chaos_max
                total_min = phys_min + fire_min + cold_min + lightning_min + chaos_min
                total_max = phys_max + fire_max + cold_max + lightning_max + chaos_max
                print(f"    All Types: {total_min:.0f} to {total_max:.0f}")
                print(f"    Physical: {phys_min:.0f} to {phys_max:.0f}")
                print(f"    Fire: {fire_min:.0f} to {fire_max:.0f}")
                print(f"    Cold: {cold_min:.0f} to {cold_max:.0f}")
                print(f"    Lightning: {lightning_min:.0f} to {lightning_max:.0f}")
                print(f"    Chaos: {chaos_min:.0f} to {chaos_max:.0f}")
                print(f"  Skill Average Hit: {final_damage:.1f}")

                # Calculate DPS
                (
                    hit_dps,
                    dot_dps,
                    total_dps,
                ) = engine.damage_calc.calculate_total_dps_with_dot(skill_name, context)
                print(f"  Skill DPS: {total_dps:.0f}")
                print()

                # Attack/Cast Rate
                print("Attack/Cast Rate:")
                print("-" * 80)
                trigger_rate_cap = engine.modifiers.calculate_stat(
                    "TriggerRateCap", 0.0, context
                )
                if trigger_rate_cap > 0:
                    print(f"  Trigger Rate Cap: {trigger_rate_cap:.2f}")
                eff_source_rate = engine.modifiers.calculate_stat(
                    "SourceRate", 0.0, context
                )
                if eff_source_rate > 0:
                    print(f"  Eff. Source Rate: {eff_source_rate:.2f}")
                skill_trigger_rate = engine.modifiers.calculate_stat(
                    "SkillTriggerRate", 0.0, context
                )
                if skill_trigger_rate > 0:
                    print(f"  Skill Trigger Rate: {skill_trigger_rate:.2f}")
                hit_rate = engine.modifiers.calculate_stat("HitRate", 0.0, context)
                if hit_rate > 0:
                    print(f"  Hit Rate: {hit_rate:.2f}")
                print()

                # DoT Breakdown
                ignite_dps = engine.damage_calc.calculate_dot_dps(
                    skill_name, "ignite", context
                )
                poison_dps = engine.damage_calc.calculate_dot_dps(
                    skill_name, "poison", context
                )
                bleed_dps = engine.damage_calc.calculate_dot_dps(
                    skill_name, "bleed", context
                )
                decay_dps = engine.damage_calc.calculate_dot_dps(
                    skill_name, "decay", context
                )

                if ignite_dps > 0 or poison_dps > 0 or bleed_dps > 0 or decay_dps > 0:
                    print("DoT Breakdown:")
                    print("-" * 80)
                    if ignite_dps > 0:
                        print(f"  Ignite DPS: {ignite_dps:.1f}")
                    if poison_dps > 0:
                        print(f"  Poison DPS: {poison_dps:.1f}")
                    if bleed_dps > 0:
                        print(f"  Bleed DPS: {bleed_dps:.1f}")
                    if decay_dps > 0:
                        print(f"  Decay DPS: {decay_dps:.1f}")
                    print()

                # Non-Damaging Ailments
                print("Non-Damaging Ailments:")
                print("-" * 80)
                chill_effect_mod = (
                    engine.modifiers.calculate_stat("ChillEffect", 100.0, context)
                    / 100.0
                )
                chill_duration = engine.modifiers.calculate_stat(
                    "ChillDuration", 0.0, context
                )
                max_chill = engine.modifiers.calculate_stat(
                    "MaximumChill", 30.0, context
                )
                current_chill = engine.modifiers.calculate_stat(
                    "CurrentChill", 0.0, context
                )
                chance_to_freeze = engine.modifiers.calculate_stat(
                    "ChanceToFreeze", 0.0, context
                )
                freeze_duration_mod = (
                    engine.modifiers.calculate_stat("FreezeDuration", 100.0, context)
                    / 100.0
                )
                shock_effect_mod = (
                    engine.modifiers.calculate_stat("ShockEffect", 100.0, context)
                    / 100.0
                )
                chance_to_shock = engine.modifiers.calculate_stat(
                    "ChanceToShock", 0.0, context
                )
                shock_duration = engine.modifiers.calculate_stat(
                    "ShockDuration", 0.0, context
                )
                max_shock = engine.modifiers.calculate_stat(
                    "MaximumShock", 50.0, context
                )
                current_shock = engine.modifiers.calculate_stat(
                    "CurrentShock", 0.0, context
                )

                if chill_effect_mod != 1.0 or chill_duration > 0 or max_chill > 0:
                    print(f"  Chill Effect Mod: x {chill_effect_mod:.1f}")
                    if chill_duration > 0:
                        print(f"  Chill Duration: {chill_duration:.0f}s")
                    print(f"  Maximum Chill: {max_chill:.0f}%")
                    if current_chill > 0:
                        print(f"  Current Chill: {current_chill:.0f}%")
                if chance_to_freeze > 0:
                    print(f"  Chance to Freeze: {chance_to_freeze:.0f}%")
                    print(f"  Freeze Duration: x {freeze_duration_mod:.0f}")
                if shock_effect_mod != 1.0 or chance_to_shock > 0:
                    print(f"  Shock Effect Mod: x {shock_effect_mod:.1f}")
                    if chance_to_shock > 0:
                        print(f"  Chance to Shock: {chance_to_shock:.0f}%")
                    if shock_duration > 0:
                        print(f"  Shock Duration: {shock_duration:.0f}s")
                    print(f"  Maximum Shock: {max_shock:.0f}%")
                    if current_shock > 0:
                        print(f"  Current Shock: {current_shock:.0f}%")
                print()

                # Damage Against Enemy (with resistances)
                if (
                    context.get("enemy_fire_resist") is not None
                    or context.get("enemy_cold_resist") is not None
                ):
                    print("Damage Against Enemy (with Resistances):")
                    print("-" * 80)
                    enemy_damage = engine.damage_calc.calculate_damage_against_enemy(
                        skill_name, context
                    )
                    print(f"  Physical: {enemy_damage.physical:.1f}")
                    print(f"  Fire: {enemy_damage.fire:.1f}")
                    print(f"  Cold: {enemy_damage.cold:.1f}")
                    print(f"  Lightning: {enemy_damage.lightning:.1f}")
                    print(f"  Chaos: {enemy_damage.chaos:.1f}")
                    print(f"  Total: {enemy_damage.total:.1f}")
                    print()
        except (AttributeError, IndexError):
            pass

    # Print Minion Stats (if applicable)
    minion_damage = engine.modifiers.calculate_stat("MinionDamage", 0.0, context)
    minion_life = engine.modifiers.calculate_stat("MinionLife", 0.0, context)
    if minion_damage != 0.0 or minion_life != 0.0:
        print("Minion Stats:")
        print("-" * 80)

        # Calculate minion stats with default base values
        base_minion_damage = {
            "Physical": 0.0,
            "Fire": 0.0,
            "Cold": 0.0,
            "Lightning": 0.0,
            "Chaos": 0.0,
        }
        base_minion_life = 100.0
        base_minion_es = 0.0
        base_minion_attack_speed = 1.0
        base_minion_cast_speed = 1.0

        minion_stats = engine.minion_calc.calculate_all_minion_stats(
            base_damage=base_minion_damage,
            base_life=base_minion_life,
            base_es=base_minion_es,
            base_attack_speed=base_minion_attack_speed,
            base_cast_speed=base_minion_cast_speed,
            context=context,
        )

        print("  Damage:")
        print(f"    Physical: {minion_stats.damage.get('Physical', 0.0):.1f}")
        print(f"    Fire: {minion_stats.damage.get('Fire', 0.0):.1f}")
        print(f"    Cold: {minion_stats.damage.get('Cold', 0.0):.1f}")
        print(f"    Lightning: {minion_stats.damage.get('Lightning', 0.0):.1f}")
        print(f"    Chaos: {minion_stats.damage.get('Chaos', 0.0):.1f}")
        print(f"  Life: {minion_stats.life:.1f}")
        print(f"  Energy Shield: {minion_stats.energy_shield:.1f}")
        print(f"  Attack Speed: {minion_stats.attack_speed:.2f}")
        print(f"  Cast Speed: {minion_stats.cast_speed:.2f}")
        print(f"  Movement Speed: {minion_stats.movement_speed:.2f}")

        if minion_stats.resistances:
            print("  Resistances:")
            for res_type, res_value in minion_stats.resistances.items():
                print(f"    {res_type.capitalize()}: {res_value:.1f}%")
        print()

    # Print Modifier Sources Summary
    print("Modifier Sources:")
    print("-" * 80)
    print("  Modifiers are loaded from:")
    print("    - Passive Tree (nodes, keystones, jewel sockets)")
    print("    - Items (explicit and implicit modifiers)")
    print("    - Skills (gem modifiers, support gems)")
    print("    - Configuration (buffs, charges, auras, curses)")
    print("    - Party Members (shared auras, buffs, support gems)")
    print()


def main():
    """
    Entry point that loads a demonstration Path of Building build and prints its calculated report.
    
    Adds the repository parent to sys.path, constructs a PathOfBuildingAPI instance from the demo import code, and calls print_calculations(build) to render the build report to stdout.
    """
    import sys
    from pathlib import Path

    # Add parent directory to path to import from utils
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pobapi import from_import_code
    from utils.demo_pobapi import import_code

    build = from_import_code(import_code())
    print_calculations(build)


if __name__ == "__main__":
    main()