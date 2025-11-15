"""Damage calculation system for Path of Building.

This module handles all damage-related calculations including:
- Base damage from skills and weapons
- Damage conversion
- Critical strike calculations
- Damage over time (DoT)
- Penetration and resistance calculations
"""

from dataclasses import dataclass
from typing import Any

from pobapi.calculator.modifiers import ModifierSystem

__all__ = ["DamageType", "DamageBreakdown", "DamageCalculator"]


class DamageType:
    """Damage type constants."""

    PHYSICAL = "Physical"
    FIRE = "Fire"
    COLD = "Cold"
    LIGHTNING = "Lightning"
    CHAOS = "Chaos"
    ELEMENTAL = "Elemental"  # Fire + Cold + Lightning


@dataclass
class DamageBreakdown:
    """Breakdown of damage by type.

    :param physical: Physical damage.
    :param fire: Fire damage.
    :param cold: Cold damage.
    :param lightning: Lightning damage.
    :param chaos: Chaos damage.
    """

    physical: float = 0.0
    fire: float = 0.0
    cold: float = 0.0
    lightning: float = 0.0
    chaos: float = 0.0

    @property
    def total(self) -> float:
        """Get total damage across all types."""
        return self.physical + self.fire + self.cold + self.lightning + self.chaos

    @property
    def elemental(self) -> float:
        """Get total elemental damage."""
        return self.fire + self.cold + self.lightning


class DamageCalculator:
    """Calculator for damage-related stats.

    This class replicates Path of Building's damage calculation system.
    """

    def __init__(self, modifier_system: ModifierSystem):
        """Initialize damage calculator.

        :param modifier_system: Modifier system to use for calculations.
        """
        self.modifiers = modifier_system

    def calculate_base_damage(
        self, skill_name: str, context: dict[str, Any] | None = None
    ) -> DamageBreakdown:
        """Calculate base damage for a skill.

        :param skill_name: Name of the skill.
        :param context: Current calculation context.
        :return: Damage breakdown by type.
        """
        if context is None:
            context = {}

        breakdown = DamageBreakdown()

        # Get base damage from skill
        breakdown.physical = self.modifiers.calculate_stat(
            f"{skill_name}BasePhysicalDamage", 0.0, context
        )
        breakdown.fire = self.modifiers.calculate_stat(
            f"{skill_name}BaseFireDamage", 0.0, context
        )
        breakdown.cold = self.modifiers.calculate_stat(
            f"{skill_name}BaseColdDamage", 0.0, context
        )
        breakdown.lightning = self.modifiers.calculate_stat(
            f"{skill_name}BaseLightningDamage", 0.0, context
        )
        breakdown.chaos = self.modifiers.calculate_stat(
            f"{skill_name}BaseChaosDamage", 0.0, context
        )

        # Apply damage conversion
        breakdown = self._apply_damage_conversion(breakdown, skill_name, context)

        return breakdown

    def _apply_damage_conversion(
        self,
        damage: DamageBreakdown,
        skill_name: str,
        context: dict[str, Any],
    ) -> DamageBreakdown:
        """Apply damage conversion (e.g., physical to fire).

        :param damage: Current damage breakdown.
        :param skill_name: Name of the skill.
        :param context: Current calculation context.
        :return: Damage breakdown after conversion.
        """
        # Get conversion percentages
        phys_to_fire = (
            self.modifiers.calculate_stat(f"{skill_name}PhysicalToFire", 0.0, context)
            / 100.0
        )
        phys_to_cold = (
            self.modifiers.calculate_stat(f"{skill_name}PhysicalToCold", 0.0, context)
            / 100.0
        )
        phys_to_lightning = (
            self.modifiers.calculate_stat(
                f"{skill_name}PhysicalToLightning", 0.0, context
            )
            / 100.0
        )
        phys_to_chaos = (
            self.modifiers.calculate_stat(f"{skill_name}PhysicalToChaos", 0.0, context)
            / 100.0
        )

        # Apply conversion
        converted_phys = damage.physical * (
            phys_to_fire + phys_to_cold + phys_to_lightning + phys_to_chaos
        )
        damage.fire += damage.physical * phys_to_fire
        damage.cold += damage.physical * phys_to_cold
        damage.lightning += damage.physical * phys_to_lightning
        damage.chaos += damage.physical * phys_to_chaos
        damage.physical -= converted_phys

        return damage

    def _apply_extra_damage(
        self,
        damage: DamageBreakdown,
        skill_name: str,
        context: dict[str, Any],
    ) -> DamageBreakdown:
        """Apply "extra damage" modifiers (e.g., X% of Physical as Extra Fire).

        :param damage: Current damage breakdown.
        :param skill_name: Name of the skill.
        :param context: Current calculation context.
        :return: Damage breakdown after extra damage.
        """
        # Get "extra damage" modifiers
        phys_as_extra_fire = (
            self.modifiers.calculate_stat("PhysicalAsExtraFire", 0.0, context) / 100.0
        )
        phys_as_extra_cold = (
            self.modifiers.calculate_stat("PhysicalAsExtraCold", 0.0, context) / 100.0
        )
        phys_as_extra_lightning = (
            self.modifiers.calculate_stat("PhysicalAsExtraLightning", 0.0, context)
            / 100.0
        )
        phys_as_extra_chaos = (
            self.modifiers.calculate_stat("PhysicalAsExtraChaos", 0.0, context) / 100.0
        )

        # Apply extra damage (adds to existing damage, doesn't convert)
        damage.fire += damage.physical * phys_as_extra_fire
        damage.cold += damage.physical * phys_as_extra_cold
        damage.lightning += damage.physical * phys_as_extra_lightning
        damage.chaos += damage.physical * phys_as_extra_chaos

        return damage

    def _apply_damage_multipliers(
        self,
        damage: DamageBreakdown,
        skill_name: str,
        context: dict[str, Any],
    ) -> DamageBreakdown:
        """Apply damage multipliers to each damage type.

        :param damage: Current damage breakdown.
        :param skill_name: Name of the skill.
        :param context: Current calculation context.
        :return: Damage breakdown after multipliers.
        """
        # Get damage multipliers for each type
        physical_mult = (
            self.modifiers.calculate_stat("PhysicalDamage", 100.0, context) / 100.0
        )
        fire_mult = self.modifiers.calculate_stat("FireDamage", 100.0, context) / 100.0
        cold_mult = self.modifiers.calculate_stat("ColdDamage", 100.0, context) / 100.0
        lightning_mult = (
            self.modifiers.calculate_stat("LightningDamage", 100.0, context) / 100.0
        )
        chaos_mult = (
            self.modifiers.calculate_stat("ChaosDamage", 100.0, context) / 100.0
        )

        # Apply generic damage multiplier
        generic_mult = (
            self.modifiers.calculate_stat(f"{skill_name}Damage", 100.0, context) / 100.0
        )

        # Apply multipliers
        damage.physical *= physical_mult * generic_mult
        damage.fire *= fire_mult * generic_mult
        damage.cold *= cold_mult * generic_mult
        damage.lightning *= lightning_mult * generic_mult
        damage.chaos *= chaos_mult * generic_mult

        return damage

    def calculate_average_hit(
        self, skill_name: str, context: dict[str, Any] | None = None
    ) -> float:
        """Calculate average hit damage.

        :param skill_name: Name of the skill.
        :param context: Current calculation context.
        :return: Average hit damage.
        """
        if context is None:
            context = {}

        base_damage = self.calculate_base_damage(skill_name, context)

        # Apply "extra damage" modifiers
        base_damage = self._apply_extra_damage(base_damage, skill_name, context)

        # Apply damage multipliers
        base_damage = self._apply_damage_multipliers(base_damage, skill_name, context)

        return base_damage.total

    def calculate_dps(
        self, skill_name: str, context: dict[str, Any] | None = None
    ) -> float:
        """Calculate damage per second.

        :param skill_name: Name of the skill.
        :param context: Current calculation context.
        :return: Damage per second.
        """
        if context is None:
            context = {}

        average_hit = self.calculate_average_hit(skill_name, context)

        # Get attack/cast speed
        if self.modifiers.get_modifiers(f"{skill_name}IsAttack", context):
            speed = self.modifiers.calculate_stat("AttackSpeed", 1.0, context)
        else:
            speed = self.modifiers.calculate_stat("CastSpeed", 1.0, context)

        # Get hit chance
        hit_chance = self.modifiers.calculate_stat("HitChance", 100.0, context) / 100.0

        # Get crit chance and multiplier
        crit_chance = self.modifiers.calculate_stat("CritChance", 0.0, context) / 100.0
        crit_mult = (
            self.modifiers.calculate_stat("CritMultiplier", 150.0, context) / 100.0
        )

        # Cap crit chance at 100%
        crit_chance = min(crit_chance, 1.0)

        # Calculate DPS with crits
        # Average damage = (1 - crit_chance) * base_damage
        #                  + crit_chance * base_damage * crit_mult
        # This simplifies to: base_damage * (1 + crit_chance * (crit_mult - 1))
        average_damage = average_hit * (1.0 + crit_chance * (crit_mult - 1.0))

        # DPS = Average Damage * Speed * Hit Chance
        dps = average_damage * speed * hit_chance

        return dps

    def calculate_dot_dps(
        self, skill_name: str, dot_type: str, context: dict[str, Any] | None = None
    ) -> float:
        """Calculate damage over time DPS.

        :param skill_name: Name of the skill.
        :param dot_type: Type of DoT ("ignite", "poison", "bleed", "decay").
        :param context: Current calculation context.
        :return: DoT DPS.
        """
        if context is None:
            context = {}

        # Get base damage for DoT calculation
        base_damage = self.calculate_base_damage(skill_name, context)

        # Get DoT-specific modifiers
        dot_stat = f"{dot_type.capitalize()}DPS"
        dot_dps = self.modifiers.calculate_stat(dot_stat, 0.0, context)

        # If no direct DoT DPS modifier, calculate from base damage
        if dot_dps == 0.0:
            # Different DoT types scale from different damage types
            if dot_type == "ignite":
                # Ignite scales from fire and physical damage
                base_for_dot = base_damage.fire + base_damage.physical * 0.5
            elif dot_type == "poison":
                # Poison scales from physical and chaos damage
                base_for_dot = base_damage.physical + base_damage.chaos
            elif dot_type == "bleed":
                # Bleed scales from physical damage
                base_for_dot = base_damage.physical
            elif dot_type == "decay":
                # Decay is chaos damage over time
                base_for_dot = base_damage.chaos
            else:
                base_for_dot = 0.0

            # Apply DoT multipliers
            dot_mult = (
                self.modifiers.calculate_stat(
                    f"{dot_type.capitalize()}Damage", 100.0, context
                )
                / 100.0
            )
            dot_dps = base_for_dot * dot_mult

        return dot_dps

    def calculate_damage_against_enemy(
        self,
        skill_name: str,
        context: dict[str, Any] | None = None,
    ) -> DamageBreakdown:
        """Calculate damage against enemy with resistances and penetration.

        :param skill_name: Name of the skill.
        :param context: Current calculation context (should include enemy resistances).
        :return: Damage breakdown after enemy resistances.
        """
        if context is None:
            context = {}

        # Get base damage
        base_damage = self.calculate_base_damage(skill_name, context)
        base_damage = self._apply_extra_damage(base_damage, skill_name, context)
        base_damage = self._apply_damage_multipliers(base_damage, skill_name, context)

        # Use PenetrationCalculator for accurate resistance calculations
        from pobapi.calculator.penetration import PenetrationCalculator

        pen_calc = PenetrationCalculator(self.modifiers)

        # Get enemy resistances (from context or config)
        enemy_fire_res = context.get("enemy_fire_resist", 0.0)
        enemy_cold_res = context.get("enemy_cold_resist", 0.0)
        enemy_lightning_res = context.get("enemy_lightning_resist", 0.0)
        enemy_chaos_res = context.get("enemy_chaos_resist", 0.0)

        # Calculate effective resistances (includes reduction and penetration)
        effective_fire_res = pen_calc.calculate_fire_resistance(enemy_fire_res, context)
        effective_cold_res = pen_calc.calculate_cold_resistance(enemy_cold_res, context)
        effective_lightning_res = pen_calc.calculate_lightning_resistance(
            enemy_lightning_res, context
        )
        effective_chaos_res = pen_calc.calculate_chaos_resistance(
            enemy_chaos_res, context
        )

        # Apply resistance reduction (damage taken = damage * (1 - resistance))
        base_damage.fire *= 1.0 - effective_fire_res
        base_damage.cold *= 1.0 - effective_cold_res
        base_damage.lightning *= 1.0 - effective_lightning_res
        base_damage.chaos *= 1.0 - effective_chaos_res

        return base_damage

    def calculate_total_dps_with_dot(
        self, skill_name: str, context: dict[str, Any] | None = None
    ) -> tuple[float, float, float]:
        """Calculate total DPS including DoT effects.

        :param skill_name: Name of the skill.
        :param context: Current calculation context.
        :return: Tuple of (hit_dps, dot_dps, total_dps).
        """
        if context is None:
            context = {}

        hit_dps = self.calculate_dps(skill_name, context)

        # Calculate all DoT types
        ignite_dps = self.calculate_dot_dps(skill_name, "ignite", context)
        poison_dps = self.calculate_dot_dps(skill_name, "poison", context)
        bleed_dps = self.calculate_dot_dps(skill_name, "bleed", context)
        decay_dps = self.calculate_dot_dps(skill_name, "decay", context)

        total_dot = ignite_dps + poison_dps + bleed_dps + decay_dps
        total_dps = hit_dps + total_dot

        return hit_dps, total_dot, total_dps
