"""Script to fetch nodes.json and gems.json from Path of Building.

This script extracts game data from Path of Building's Lua files
or downloads from community sources.

Based on analysis of Path of Building's Data.lua module:
- Gems are loaded from Data/Gems.lua and Data/Skills/*.lua files
- Nodes are loaded from PassiveSkills.dat or tree JSON files
- Data is structured in Lua tables and needs to be converted to JSON
"""

import json
import os
import re
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def parse_lua_table_simple(lua_content: str) -> dict | None:
    """Simple Lua table parser (basic implementation).

    This is a simplified parser for basic Lua table structures.
    For full parsing, consider using a proper Lua parser library.

    :param lua_content: Lua file content as string.
    :return: Dictionary representation or None if failed.
    """
    # This is a placeholder - full implementation would require
    # a proper Lua parser (e.g., lupa, lua-parser, or manual regex parsing)
    # For now, return None
    return None


def fetch_nodes_from_pob_repo(pob_path: str | None = None) -> dict | None:
    """Fetch passive tree nodes from PoB repository.

    Attempts to parse nodes from PoB's Lua files or tree JSON.

    :param pob_path: Path to Path of Building repository (optional).
    :return: Dictionary of nodes or None if failed.
    """
    if not pob_path:
        # Try to find PoB repository in common locations
        possible_paths = [
            Path.home() / "PathOfBuilding",
            Path.home() / "PathOfBuilding-Community",
            Path.cwd() / "PathOfBuilding",
        ]
        for path in possible_paths:
            if path.exists() and (path / "src" / "Data").exists():
                pob_path = str(path)
                break

    if not pob_path:
        print("Path of Building repository not found.")
        print("Please clone it manually or specify path:")
        print("  git clone https://github.com/PathOfBuildingCommunity/PathOfBuilding")
        return None

    pob_data_path = Path(pob_path) / "src" / "Data"

    # Check for PassiveSkills.lua (if exists)
    passive_skills_file = pob_data_path / "PassiveSkills.lua"
    if passive_skills_file.exists():
        try:
            with open(passive_skills_file, encoding="utf-8") as f:
                # content = f.read()  # Not used yet
                # Parse Lua table (would need proper parser)
                # For now, return None
                _ = f.read()  # Read but not used
                return None
        except OSError:
            pass

    # Alternative: Try to find tree JSON files
    tree_json_paths = [
        pob_data_path.parent.parent / "TreeData" / "*.json",
        pob_data_path / "Tree" / "*.json",
    ]

    for pattern in tree_json_paths:
        import glob

        for json_file in glob.glob(str(pattern)):
            try:
                with open(json_file, encoding="utf-8") as f:
                    tree_data = json.load(f)
                    # Extract nodes from tree JSON
                    if "nodes" in tree_data:
                        return tree_data["nodes"]
            except (OSError, json.JSONDecodeError):
                continue

    return None


def fetch_gems_from_pob_repo(pob_path: str | None = None) -> dict | None:
    """Fetch skill gems from PoB repository.

    Based on Data.lua logic:
    1. Loads skills from Data/Skills/*.lua files
    2. Loads gems from Data/Gems.lua
    3. Links gems to skills via grantedEffectId

    :param pob_path: Path to Path of Building repository (optional).
    :return: Dictionary of gems or None if failed.
    """
    if not pob_path:
        # Try to find PoB repository
        possible_paths = [
            Path.home() / "PathOfBuilding",
            Path.home() / "PathOfBuilding-Community",
            Path.cwd() / "PathOfBuilding",
        ]
        for path in possible_paths:
            if path.exists() and (path / "src" / "Data").exists():
                pob_path = str(path)
                break

    if not pob_path:
        print("Path of Building repository not found.")
        return None

    pob_data_path = Path(pob_path) / "src" / "Data"

    # Load Gems.lua
    gems_file = pob_data_path / "Gems.lua"
    if not gems_file.exists():
        print(f"Gems.lua not found at {gems_file}")
        return None

    try:
        with open(gems_file, encoding="utf-8") as f:
            # gems_content = f.read()  # Not used yet
            # Parse Lua table (would need proper parser)
            # Structure: return { ["gemId"] = { name, gameId,
            # grantedEffectId, ... }, ... }
            _ = f.read()  # Read but not used
            # For now, return None - requires Lua parser
            return None
    except OSError as e:
        print(f"Error reading Gems.lua: {e}")
        return None


def extract_gems_from_lua_content(content: str) -> dict:
    """Extract gems from Lua file content using regex (basic).

    This is a basic implementation using regex. For full parsing,
    use a proper Lua parser.

    :param content: Lua file content.
    :return: Dictionary of gems.
    """
    gems = {}

    # Basic regex pattern for Lua table entries
    # Pattern: ["key"] = { field1 = value1, field2 = value2, ... }
    pattern = r'\["([^"]+)"\]\s*=\s*\{([^}]+)\}'

    matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)

    for match in matches:
        gem_id = match.group(1)
        # gem_data_str = match.group(2)  # Not used yet

        # Extract fields (simplified)
        gem_data = {}
        # Parse fields from gem_data_str
        # This is simplified - full implementation would need proper parsing

        gems[gem_id] = gem_data

    return gems


def parse_pob_lua_file(file_path: str, data_type: str) -> dict | None:
    """Parse PoB Lua file to extract data.

    :param file_path: Path to Lua file.
    :param data_type: Type of data ("nodes" or "gems").
    :return: Dictionary of data or None if failed.
    """
    if not os.path.exists(file_path):
        return None

    try:
        with open(file_path, encoding="utf-8") as f:
            # content = f.read()  # Not used yet
            _ = f.read()  # Read but not used

        # Basic Lua table parsing (simplified)
        # Actual implementation would need a proper Lua parser
        # For now, return None
        return None
    except OSError:
        return None


def main():
    """Main function to fetch and save data files."""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    print("Fetching nodes.json...")
    nodes = fetch_nodes_from_pob_repo()
    if nodes:
        nodes_path = data_dir / "nodes.json"
        with open(nodes_path, "w", encoding="utf-8") as f:
            json.dump({"nodes": nodes}, f, indent=2)
        print(f"Saved {len(nodes)} nodes to {nodes_path}")
    else:
        print("Failed to fetch nodes.json")
        print("Note: You can manually extract nodes from PoB's Lua files:")
        print("  - src/Data/PassiveSkills.lua")
        print("  - Or use PoB's export functionality")

    print("\nFetching gems.json...")
    gems = fetch_gems_from_pob_repo()
    if gems:
        gems_path = data_dir / "gems.json"
        with open(gems_path, "w", encoding="utf-8") as f:
            json.dump({"gems": gems}, f, indent=2)
        print(f"Saved {len(gems)} gems to {gems_path}")
    else:
        print("Failed to fetch gems.json")
        print("Note: You can manually extract gems from PoB's Lua files:")
        print("  - src/Data/Skills.lua")
        print("  - Or use PoB's export functionality")

    print("\n" + "=" * 80)
    print("ИНСТРУКЦИИ ПО ИЗВЛЕЧЕНИЮ ДАННЫХ")
    print("=" * 80)
    print("\n1. Клонировать репозиторий Path of Building:")
    print("   git clone https://github.com/PathOfBuildingCommunity/PathOfBuilding")
    print("\n2. Для gems.json:")
    print("   - Файл: src/Data/Gems.lua")
    print("   - Структура: Lua таблица с данными о гемах")
    print("   - Формат: data.gems[gemId] = { name, gameId, grantedEffectId, ... }")
    print("   - Требуется: Lua парсер для конвертации в JSON")
    print("\n3. Для nodes.json:")
    print("   - Источники:")
    print("     * src/Data/PassiveSkills.lua (если существует)")
    print("     * Парсинг из PassiveSkills.dat файла игры")
    print("     * Tree JSON файлы (если доступны)")
    print("   - Структура: Lua таблица или JSON с данными узлов")
    print("\n4. Альтернативные источники:")
    print("   - poedb.tw - база данных Path of Exile")
    print("   - Официальный API Path of Exile (если доступен)")
    print("   - Community projects с готовыми JSON файлами")
    print("\n5. Конвертация:")
    print("   - Использовать Lua парсер (lupa, lua-parser)")
    print("   - Или ручной парсинг через regex (упрощенный)")
    print("   - Сохранить в формате JSON, совместимом с GameDataLoader")
    print("\nПодробности см. в docs/POB_DATA_EXTRACTION_REPORT.md")


if __name__ == "__main__":
    main()
