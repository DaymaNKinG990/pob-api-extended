#!/usr/bin/env python3
"""Check all PlayerStat elements in XML and compare with STATS_MAP."""

from pobapi import constants, from_import_code

code = open("data/import_code.txt").read().strip()
build = from_import_code(code)

xml = build.xml
build_elem = xml.find("Build")
player_stats = build_elem.findall("PlayerStat")

print("=" * 80)
print("All PlayerStat elements in XML")
print("=" * 80)
print(f"\nTotal PlayerStat elements: {len(player_stats)}\n")

# Group by stat name
stats_in_xml = {}
for ps in player_stats:
    stat_name = ps.get("stat")
    stat_value = ps.get("value")
    if stat_name not in stats_in_xml:
        stats_in_xml[stat_name] = []
    stats_in_xml[stat_name].append(stat_value)

print("Stats in XML (grouped by name):")
for stat_name in sorted(stats_in_xml.keys()):
    values = stats_in_xml[stat_name]
    mapped = constants.STATS_MAP.get(stat_name, "NOT MAPPED")
    print(f"  {stat_name}: {values[0] if len(values) == 1 else values} -> {mapped}")

print("\n" + "=" * 80)
print("Stats NOT in STATS_MAP:")
print("=" * 80)
unmapped = [s for s in stats_in_xml.keys() if s not in constants.STATS_MAP]
if unmapped:
    for stat_name in sorted(unmapped):
        values = stats_in_xml[stat_name]
        print(f"  {stat_name}: {values[0] if len(values) == 1 else values}")
else:
    print("  All stats are mapped!")

print("\n" + "=" * 80)
print("Stats in STATS_MAP but NOT in XML:")
print("=" * 80)
xml_stat_names = set(stats_in_xml.keys())
map_stat_names = set(constants.STATS_MAP.keys())
unused_in_map = map_stat_names - xml_stat_names
if unused_in_map:
    for stat_name in sorted(unused_in_map):
        mapped_to = constants.STATS_MAP[stat_name]
        print(f"  {stat_name} -> {mapped_to}")
else:
    print("  All mapped stats are present in XML!")
