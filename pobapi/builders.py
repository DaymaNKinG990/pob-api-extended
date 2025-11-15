"""Builder pattern for complex objects."""

from typing import Any

from pobapi import config, constants, models, stats
from pobapi.parsers import (
    ItemsParser,
)

__all__ = ["StatsBuilder", "ConfigBuilder", "ItemSetBuilder"]


class StatsBuilder:
    """Builder for Stats objects."""

    @staticmethod
    def build(xml_root) -> stats.Stats:
        """Build Stats object from XML.

        :param xml_root: XML root element.
        :return: Stats instance.
        """
        build_element = xml_root.find("Build")
        if build_element is None:
            return stats.Stats()

        kwargs: dict[str, float] = {}
        for i in build_element.findall("PlayerStat"):
            stat_key = constants.STATS_MAP.get(i.get("stat"))
            if stat_key:
                kwargs[stat_key] = float(i.get("value"))
        return stats.Stats(**kwargs)  # type: ignore[arg-type]


class ConfigBuilder:
    """Builder for Config objects."""

    @staticmethod
    def build(xml_root, character_level: int) -> config.Config:
        """Build Config object from XML.

        :param xml_root: XML root element.
        :param character_level: Character level.
        :return: Config instance.
        """
        config_element = xml_root.find("Config")
        if config_element is None:
            return config.Config(character_level=character_level)

        def _convert_fields(item):
            if item.get("boolean"):
                return True
            elif item.get("number"):
                return int(item.get("number"))
            elif item.get("string"):
                return item.get("string").capitalize()
            return None

        kwargs: dict[str, Any] = {}
        for i in config_element.findall("Input"):
            config_key = constants.CONFIG_MAP.get(i.get("name"))
            if config_key:
                kwargs[config_key] = _convert_fields(i)
        kwargs["character_level"] = character_level
        return config.Config(**kwargs)


class ItemSetBuilder:
    """Builder for Item Set objects."""

    @staticmethod
    def build_all(xml_root) -> list[models.Set]:
        """Build all item sets from XML.

        :param xml_root: XML root element.
        :return: List of Set instances.
        """
        return [
            ItemSetBuilder._build_single(item_set_data)
            for item_set_data in ItemsParser.parse_item_sets(xml_root)
        ]

    @staticmethod
    def _build_single(item_set_data: dict) -> models.Set:
        """Build single Set instance.

        :param item_set_data: Dictionary with item set data.
        :return: Set instance.
        """
        # Initialize all Set fields with None as default
        set_kwargs = {
            "weapon1": None,
            "weapon1_as1": None,
            "weapon1_as2": None,
            "weapon1_swap": None,
            "weapon1_swap_as1": None,
            "weapon1_swap_as2": None,
            "weapon2": None,
            "weapon2_as1": None,
            "weapon2_as2": None,
            "weapon2_swap": None,
            "weapon2_swap_as1": None,
            "weapon2_swap_as2": None,
            "helmet": None,
            "helmet_as1": None,
            "helmet_as2": None,
            "body_armour": None,
            "body_armour_as1": None,
            "body_armour_as2": None,
            "gloves": None,
            "gloves_as1": None,
            "gloves_as2": None,
            "boots": None,
            "boots_as1": None,
            "boots_as2": None,
            "amulet": None,
            "ring1": None,
            "ring2": None,
            "belt": None,
            "belt_as1": None,
            "belt_as2": None,
            "flask1": None,
            "flask2": None,
            "flask3": None,
            "flask4": None,
            "flask5": None,
        }
        # Update with actual data from XML
        set_kwargs.update(item_set_data)
        return models.Set(**set_kwargs)
