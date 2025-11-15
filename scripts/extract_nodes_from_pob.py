"""Script to extract nodes.json from Path of Building and Path of Exile data.

This script performs a one-time extraction of passive tree node data from:
1. PassiveSkills.dat file (from Path of Exile game directory)
2. Tree JSON files (from PoB or community sources)

Based on DAT_PARSING_LOGIC.md:
- PassiveSkills.dat structure with StatsZip virtual field
- Tree JSON for geometry (x, y, connections)
"""

import json
import struct
import sys
from enum import Enum
from pathlib import Path
from typing import Any

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


# DAT file constants
DAT_FILE_MAGIC_NUMBER = b"\xbb\xbb\xbb\xbb\xbb\xbb\xbb\xbb"
_TABLE_OFFSET = 4  # Header is 4 bytes (row count)


class CastType(Enum):
    """Types for casting DAT values."""

    VALUE = "value"
    POINTER = "pointer"
    POINTER_LIST = "pointer_list"
    STRING = "string"


# NULL values in DAT files
NULL_VALUES_32 = [0xFEFEFEFE, 0xFFFFFFFF, 0x1010102]
NULL_VALUES_64 = [0xFEFEFEFEFEFEFEFE]


def sanitise_text(text: str) -> str:
    """Sanitise text (remove special characters, normalize).

    :param text: Text to sanitise.
    :return: Sanitised text.
    """
    if not text:
        return ""
    # Basic sanitisation - remove control characters
    return "".join(c for c in text if ord(c) >= 32 or c in "\n\t")


def read_string_utf16(file_raw: bytes, offset: int) -> tuple[str, int]:
    """Read UTF-16 string from DAT file.

    Strings in DAT files are UTF-16 and terminated by 4 null bytes.

    :param file_raw: Raw file bytes.
    :param offset: Offset to start reading from.
    :return: Tuple of (string, new_offset).
    """
    # Find terminator (4 null bytes)
    terminator_pos = file_raw.find(b"\x00\x00\x00\x00", offset)
    if terminator_pos == -1:
        # No terminator found, read to end
        terminator_pos = len(file_raw)

    # Extract string bytes
    string_bytes = file_raw[offset:terminator_pos]

    # Decode UTF-16
    if len(string_bytes) == 0:
        return "", terminator_pos + 4

    try:
        string = string_bytes.decode("utf-16-le")
    except UnicodeDecodeError:
        # Fallback: try to decode as-is
        string = string_bytes.decode("utf-8", errors="ignore")

    return string, terminator_pos + 4


def read_pointer_list(
    file_raw: bytes, data_offset: int, offset: int, element_size: int = 4
) -> tuple[list[int], int]:
    """Read pointer list from DAT file.

    Structure: [size (4 bytes), pointer (4 bytes), elements...]

    :param file_raw: Raw file bytes.
    :param data_offset: Offset to data section.
    :param offset: Offset to list header.
    :param element_size: Size of each element (default: 4 for int).
    :return: Tuple of (list of values, new_offset).
    """
    # Read size and pointer
    list_size, list_pointer = struct.unpack("<II", file_raw[offset : offset + 8])

    if list_size == 0:
        return [], offset + 8

    # Calculate actual data offset
    data_offset_actual = list_pointer + data_offset

    # Read elements
    elements = []
    for i in range(list_size):
        element_offset = data_offset_actual + i * element_size
        if element_size == 4:
            value = struct.unpack("<I", file_raw[element_offset : element_offset + 4])[
                0
            ]
            # Check for null
            if value in NULL_VALUES_32:
                value = None
            elements.append(value)
        elif element_size == 8:
            value = struct.unpack("<Q", file_raw[element_offset : element_offset + 8])[
                0
            ]
            if value in NULL_VALUES_64:
                value = None
            elements.append(value)

    return elements, offset + 8


def parse_passive_skills_dat_simple(
    dat_path: Path, stats_lookup: dict | None = None
) -> dict:
    """Parse PassiveSkills.dat using simplified approach.

    This is a simplified parser based on DAT_PARSING_LOGIC.md.
    For full parsing, we would need the complete specification.

    Structure based on DAT_PARSING_LOGIC.md:
    - Header: 4 bytes (row count)
    - Table section: fixed-size records
    - Magic number: 0xBBBBBBBBBBBBBBBB
    - Data section: variable-size data (strings, lists, etc.)

    :param dat_path: Path to PassiveSkills.dat file.
    :param stats_lookup: Optional lookup table for stat IDs to descriptions.
    :return: Dictionary of nodes {node_id: node_data}.
    """
    if not dat_path.exists():
        print(f"Error: {dat_path} not found")
        return {}

    with open(dat_path, "rb") as f:
        file_raw = f.read()

    # Find magic number (separator between table and data sections)
    data_offset = file_raw.find(DAT_FILE_MAGIC_NUMBER)
    if data_offset == -1:
        print("Error: Magic number not found in DAT file")
        return {}

    # Read row count from header
    table_rows = struct.unpack("<I", file_raw[0:4])[0]

    # Calculate table record length
    table_length = data_offset - _TABLE_OFFSET
    if table_rows == 0:
        print("Error: No rows in DAT file")
        return {}

    table_record_length = table_length // table_rows

    print("Parsing PassiveSkills.dat:")
    print(f"  Rows: {table_rows}")
    print(f"  Table record length: {table_record_length} bytes")
    print(f"  Data offset: {data_offset}")

    # NOTE: Full DAT parsing requires complete specification
    # Based on DAT_PARSING_LOGIC.md, we need:
    # 1. Field specification with types (int, ref|string, ref|list|ulong, etc.)
    # 2. Field offsets in table record
    # 3. Stats.dat for stat key lookups

    # Simplified approach: Try to extract basic fields if we know approximate structure
    # This is a placeholder - full implementation needs specification

    nodes = {}

    # Known approximate structure (based on common DAT patterns):
    # - Id: uint32 at offset 0
    # - PassiveSkillGraphId: uint32 at offset 4
    # - Name: ref|string (pointer at offset 8)
    # - StatsKeys: ref|list|ulong (size+pointer at offset 12)
    # - Stat1Value...Stat5Value: int32 at offsets 20, 24, 28, 32, 36
    # ... (many more fields)

    # For now, we can only parse if we have the exact specification
    # This is a framework that can be extended when specification is available

    print("Warning: Full DAT parsing requires specification file.")
    print("This is a placeholder - full implementation needs:")
    print("  1. Complete field specification for PassiveSkills.dat")
    print("  2. Field types and offsets")
    print("  3. Stats.dat for stat key lookups")
    print("\nFor now, using tree JSON only (geometry without stats from DAT)")

    return nodes


def parse_tree_json(json_path: Path) -> dict:
    """Parse tree JSON file.

    Tree JSON files contain geometry and connections for passive tree nodes.

    :param json_path: Path to tree JSON file.
    :return: Dictionary of node geometry {node_id: {x, y, connections}}.
    """
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return {}

    try:
        with open(json_path, encoding="utf-8") as f:
            tree_data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error reading tree JSON: {e}")
        return {}

    # Extract nodes from various possible structures
    nodes = {}

    # Try different possible structures
    if "nodes" in tree_data:
        nodes_data = tree_data["nodes"]
    elif "tree" in tree_data and "nodes" in tree_data["tree"]:
        nodes_data = tree_data["tree"]["nodes"]
    elif isinstance(tree_data, dict):
        # Assume top-level keys are node IDs
        nodes_data = tree_data
    else:
        print("Warning: Unknown tree JSON structure")
        return {}

    # Extract geometry for each node
    for node_id_str, node_info in nodes_data.items():
        try:
            node_id = int(node_id_str)
        except (ValueError, TypeError):
            continue

        node_geom = {
            "x": node_info.get("x") if isinstance(node_info, dict) else None,
            "y": node_info.get("y") if isinstance(node_info, dict) else None,
            "connections": node_info.get("connections", [])
            if isinstance(node_info, dict)
            else [],
        }
        nodes[node_id] = node_geom

    print(f"Loaded geometry for {len(nodes)} nodes from tree JSON")
    return nodes


def format_stat_from_key_value(
    stat_key: Any, stat_value: int | float, stats_lookup: dict | None = None
) -> str:
    """Format stat key and value into modifier string.

    Based on DAT_PARSING_LOGIC.md, StatsZip provides pairs of (stat_key, stat_value).
    Stat keys are references to Stats.dat, which contains descriptions.

    :param stat_key: Stat key (can be ID, string, or dict with Id/Description).
    :param stat_value: Stat value.
    :param stats_lookup: Optional lookup table {stat_id: stat_description}.
    :return: Formatted stat string (e.g., "+10 to Strength").
    """
    # Try to extract stat ID and description
    stat_id = None
    stat_desc = None

    if isinstance(stat_key, dict):
        stat_id = stat_key.get("Id") or stat_key.get("id")
        stat_desc = stat_key.get("Description") or stat_key.get("description")
    elif isinstance(stat_key, int | str):
        stat_id = stat_key
        # Try lookup table
        if stats_lookup and stat_id in stats_lookup:
            stat_desc = stats_lookup[stat_id]

    # Use description if available, otherwise use ID
    if stat_desc:
        stat_name = stat_desc
    elif stat_id:
        stat_name = str(stat_id)
    else:
        stat_name = str(stat_key)

    # Format based on value
    value = float(stat_value)

    # Basic formatting - this should be enhanced with Stats.dat lookup
    # Common patterns from Path of Exile:
    # - "+X to Y" for flat values
    # - "X% increased Y" for percentage increases
    # - "X% more Y" for more multipliers

    # For now, use generic format
    # Full implementation would parse stat description format from Stats.dat
    if value >= 0:
        return f"+{int(value)} to {stat_name}"
    else:
        return f"{int(value)} to {stat_name}"


def process_statszip_to_stats(
    stat_keys: list[Any],
    stat_values: list[int | float],
    stats_lookup: dict | None = None,
) -> list[str]:
    """Process StatsZip virtual field into stat strings.

    Based on DAT_PARSING_LOGIC.md, StatsZip combines StatsKeys and StatValues
    into pairs (stat_key, stat_value).

    :param stat_keys: List of stat keys (from StatsKeys).
    :param stat_values: List of stat values (from StatValues).
    :param stats_lookup: Optional lookup table for stat descriptions.
    :return: List of formatted stat strings.
    """
    stats = []

    # Zip stat keys and values together (like StatsZip virtual field)
    for stat_key, stat_value in zip(stat_keys, stat_values, strict=False):
        if stat_value is None or stat_value == 0:
            continue

        stat_string = format_stat_from_key_value(stat_key, stat_value, stats_lookup)
        stats.append(stat_string)

    return stats


def merge_node_data(
    passive_skills_data: dict, tree_data: dict, stats_lookup: dict | None = None
) -> dict:
    """Merge data from PassiveSkills.dat and tree JSON.

    :param passive_skills_data: Data from PassiveSkills.dat.
    :param tree_data: Geometry data from tree JSON.
    :param stats_lookup: Optional lookup table for stat descriptions.
    :return: Merged nodes dictionary.
    """
    nodes = {}

    # Process passive skills data
    for node_id, passive_data in passive_skills_data.items():
        # Process StatsZip if we have stat_keys and stat_values
        if "statKeys" in passive_data and "statValues" in passive_data:
            stat_keys = passive_data.get("statKeys", [])
            stat_values = passive_data.get("statValues", [])
            if stat_keys and stat_values:
                # Convert StatsZip to stat strings
                stats = process_statszip_to_stats(stat_keys, stat_values, stats_lookup)
                passive_data["stats"] = stats

        # Add geometry from tree JSON
        if node_id in tree_data:
            passive_data["x"] = tree_data[node_id].get("x")
            passive_data["y"] = tree_data[node_id].get("y")
            passive_data["connections"] = tree_data[node_id].get("connections", [])

        nodes[node_id] = passive_data

    # Add nodes from tree JSON that might not be in passive skills
    for node_id, tree_info in tree_data.items():
        if node_id not in nodes:
            # Create minimal node from tree data
            nodes[node_id] = {
                "id": node_id,
                "name": f"Node {node_id}",
                "stats": [],
                "x": tree_info.get("x"),
                "y": tree_info.get("y"),
                "connections": tree_info.get("connections", []),
            }

    return nodes


def generate_nodes_json(nodes: dict, output_path: Path) -> None:
    """Generate nodes.json from processed nodes.

    :param nodes: Dictionary of processed nodes.
    :param output_path: Path to output JSON file.
    """
    nodes_json = {"nodes": {}}

    for node_id, node_data in nodes.items():
        # Ensure node_id is in data
        if "id" not in node_data:
            node_data["id"] = node_id

        nodes_json["nodes"][str(node_id)] = node_data

    # Save to JSON
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(nodes_json, f, indent=2, ensure_ascii=False)

    print(f"\nSaved {len(nodes_json['nodes'])} nodes to {output_path}")


def find_passive_skills_dat() -> Path | None:
    """Find PassiveSkills.dat in common locations.

    :return: Path to file or None if not found.
    """
    # Common Path of Exile installation paths
    possible_paths = [
        Path("C:/Program Files (x86)/Grinding Gear Games/Path of Exile"),
        Path("C:/Program Files/Grinding Gear Games/Path of Exile"),
        Path("D:/Program Files (x86)/Grinding Gear Games/Path of Exile"),
        Path("D:/Program Files/Grinding Gear Games/Path of Exile"),
        Path.home() / "Documents" / "Path of Exile",
    ]

    # Look for PassiveSkills.dat in Content.ggpk or extracted files
    for base_path in possible_paths:
        # Try extracted Data directory
        dat_path = base_path / "Data" / "PassiveSkills.dat"
        if dat_path.exists():
            return dat_path

        # Try in Metadata/PassiveSkills.dat
        dat_path = base_path / "Metadata" / "PassiveSkills.dat"
        if dat_path.exists():
            return dat_path

    return None


def find_tree_json(pob_path: Path | None = None) -> Path | None:
    """Find tree JSON file.

    :param pob_path: Optional Path of Building repository path.
    :return: Path to tree JSON or None if not found.
    """
    # Try PoB repository first
    if pob_path:
        possible_paths = [
            pob_path / "TreeData" / "*.json",
            pob_path / "Data" / "Tree" / "*.json",
            pob_path / "src" / "TreeData" / "*.json",
        ]

        import glob

        for pattern in possible_paths:
            for json_file in glob.glob(str(pattern)):
                return Path(json_file)

    # Try community sources or other locations
    # This would need to be implemented based on available sources

    return None


def main():
    """Main function to extract nodes from various sources."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract nodes.json from PassiveSkills.dat and tree JSON"
    )
    parser.add_argument(
        "--dat-path",
        type=str,
        help="Path to PassiveSkills.dat file",
    )
    parser.add_argument(
        "--tree-json",
        type=str,
        help="Path to tree JSON file",
    )
    parser.add_argument(
        "--pob-path",
        type=str,
        help="Path to Path of Building repository (for finding tree JSON)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output path for nodes.json (default: data/nodes.json)",
    )

    args = parser.parse_args()

    print("=" * 80)
    print("Extracting nodes.json")
    print("=" * 80)

    # Find or use provided DAT file
    dat_path = None
    if args.dat_path:
        dat_path = Path(args.dat_path)
    else:
        print("\nSearching for PassiveSkills.dat...")
        dat_path = find_passive_skills_dat()

    passive_skills_data = {}
    if dat_path and dat_path.exists():
        print(f"\nFound PassiveSkills.dat at: {dat_path}")
        print("Note: Full DAT parsing requires specification file.")
        print("Currently using placeholder - will need full implementation.")
        # passive_skills_data = parse_passive_skills_dat_simple(dat_path)
    else:
        print("\nPassiveSkills.dat not found.")
        print("You can:")
        print("  1. Extract it from Path of Exile Content.ggpk")
        print("  2. Download from community sources")
        print("  3. Use tree JSON only (geometry only, no stats)")

    # Find or use provided tree JSON
    tree_json_path = None
    if args.tree_json:
        tree_json_path = Path(args.tree_json)
    else:
        pob_path = Path(args.pob_path) if args.pob_path else None
        tree_json_path = find_tree_json(pob_path)

    tree_data = {}
    if tree_json_path and tree_json_path.exists():
        print(f"\nFound tree JSON at: {tree_json_path}")
        tree_data = parse_tree_json(tree_json_path)
    else:
        print("\nTree JSON not found.")
        print("You can:")
        print("  1. Download from PoB repository")
        print("  2. Use community tree JSON files")

    # Merge data
    if passive_skills_data or tree_data:
        print("\n" + "=" * 80)
        print("Merging data...")
        print("=" * 80)
        stats_lookup = None  # Optional lookup table for stat descriptions
        nodes = merge_node_data(passive_skills_data, tree_data, stats_lookup)
    else:
        print("\nError: No data sources found")
        print("Please provide at least one of:")
        print("  --dat-path /path/to/PassiveSkills.dat")
        print("  --tree-json /path/to/tree.json")
        return 1

    # Generate JSON
    output_path = args.output
    if not output_path:
        output_path = Path(__file__).parent.parent / "data" / "nodes.json"
    else:
        output_path = Path(output_path)

    print("\n" + "=" * 80)
    print("Generating nodes.json...")
    print("=" * 80)
    generate_nodes_json(nodes, output_path)

    print("\n" + "=" * 80)
    print("Done!")
    print("=" * 80)
    print("\nNote: Full implementation requires:")
    print("  1. Complete PassiveSkills.dat specification")
    print("  2. Stats.dat for stat key lookups")
    print("  3. Full DAT parser implementation")

    return 0


if __name__ == "__main__":
    sys.exit(main())
