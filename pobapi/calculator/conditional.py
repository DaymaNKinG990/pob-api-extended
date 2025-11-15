"""Conditional modifier handling for Path of Building.

This module handles conditional modifiers that depend on game state,
such as "on full life", "on low life", "enemy is shocked", etc.
"""

from typing import Any

__all__ = ["ConditionEvaluator"]


class ConditionEvaluator:
    """Evaluates conditions for conditional modifiers.

    This class checks if conditions are met based on the current game state.
    """

    @staticmethod
    def evaluate_condition(condition: str, context: dict[str, Any]) -> bool:
        """Evaluate a single condition.

        :param condition: Condition name (e.g., "on_full_life", "on_low_life").
        :param context: Current calculation context.
        :return: True if condition is met.
        """
        # Get current life/mana/ES values
        current_life = context.get("current_life")
        max_life = context.get("max_life") or context.get("life")
        current_mana = context.get("current_mana")
        max_mana = context.get("max_mana") or context.get("mana")
        current_es = context.get("current_energy_shield")
        max_es = context.get("max_energy_shield") or context.get("energy_shield")

        # Life-based conditions
        if condition == "on_full_life" or condition == "OnFullLife":
            if max_life and current_life is not None:
                return bool(current_life >= max_life * 0.99)  # 99% threshold
            # If not specified, check flag
            return bool(context.get("on_full_life", False))

        if condition == "on_low_life" or condition == "OnLowLife":
            if max_life and current_life is not None:
                return bool(current_life <= max_life * 0.35)  # 35% threshold
            # If not specified, check flag
            return bool(context.get("on_low_life", False))

        # Mana-based conditions
        if condition == "on_full_mana" or condition == "OnFullMana":
            if max_mana and current_mana is not None:
                return bool(current_mana >= max_mana * 0.99)
            return bool(context.get("on_full_mana", False))

        if condition == "on_low_mana" or condition == "OnLowMana":
            if max_mana and current_mana is not None:
                return bool(current_mana <= max_mana * 0.35)
            return bool(context.get("on_low_mana", False))

        # Energy Shield conditions
        if condition == "on_full_energy_shield" or condition == "OnFullEnergyShield":
            if max_es and current_es is not None:
                return bool(current_es >= max_es * 0.99)
            return bool(context.get("on_full_energy_shield", False))

        if condition == "on_low_energy_shield" or condition == "OnLowEnergyShield":
            if max_es and current_es is not None:
                return bool(current_es <= max_es * 0.35)
            return bool(context.get("on_low_energy_shield", False))

        # Enemy conditions
        if condition == "enemy_is_shocked":
            return bool(context.get("enemy_is_shocked", False))

        if condition == "enemy_is_frozen":
            return bool(context.get("enemy_is_frozen", False))

        if condition == "enemy_is_ignited":
            return bool(context.get("enemy_is_ignited", False))

        if condition == "enemy_is_chilled":
            return bool(context.get("enemy_is_chilled", False))

        if condition == "enemy_is_poisoned":
            return bool(context.get("enemy_is_poisoned", False))

        # Distance conditions
        if condition == "projectile_distance":
            distance = context.get("projectile_distance", "medium")
            required = context.get("required_distance", "close")
            if required == "close":
                return bool(distance in ("close", "medium"))
            elif required == "far":
                return bool(distance == "far")
            return bool(distance == required)

        # Default: check if condition is set in context
        return bool(context.get(condition, False))

    @staticmethod
    def evaluate_all_conditions(
        conditions: dict[str, Any], context: dict[str, Any]
    ) -> bool:
        """Evaluate all conditions in a dictionary.

        :param conditions: Dictionary of conditions to check.
        :param context: Current calculation context.
        :return: True if all conditions are met.
        """
        for condition, required_value in conditions.items():
            if not ConditionEvaluator.evaluate_condition(condition, context):
                # If condition has a required value, check it
                if required_value is not True:
                    return False
        return True
