"""Script to extract gems.json from Path of Building Lua files.

This script performs a one-time extraction of gem data from PoB's Lua files
and saves it as gems.json for use by GameDataLoader.

Based on Path of Building's Data.lua logic:
- Loads skills from Data/Skills/*.lua files
- Loads gems from Data/Gems.lua
- Links gems to skills via grantedEffectId
- Processes modifiers (baseMods, qualityMods, levelMods)
- Handles special cases (Vaal gems, AltX/AltY, Support gems)
"""

import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from lupa import LuaRuntime

    LUA_AVAILABLE = True
except ImportError:
    LUA_AVAILABLE = False
    print("Warning: lupa not available. Install with: uv add lupa")
    print("Falling back to manual parsing (limited functionality)")


def sanitise_text(text: str) -> str:
    """Sanitise text (remove special characters, normalize).

    :param text: Text to sanitise.
    :return: Sanitised text.
    """
    if not text:
        return ""
    # Basic sanitisation - remove control characters
    return "".join(c for c in text if ord(c) >= 32 or c in "\n\t")


def parse_lua_file_with_lupa(file_path: Path) -> dict | list | None:
    """Parse Lua file using lupa.

    :param file_path: Path to Lua file.
    :return: Dictionary or list with parsed data or None if failed.
    """
    if not LUA_AVAILABLE:
        return None

    try:
        lua = LuaRuntime()
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
            # Execute Lua code and get return value
            result = lua.execute(content)

            if result is None:
                return None

            # Check if result is dict-like (has items method)
            if hasattr(result, "items"):
                # Convert Lua table to Python dict
                data = {}
                try:
                    for key, value in result.items():
                        # Convert Lua table keys/values to Python
                        py_key = str(key) if not isinstance(key, str) else key
                        py_value = _lua_to_python(value)
                        data[py_key] = py_value
                    return data
                except (TypeError, AttributeError) as e:
                    # If items() fails, try as list
                    print(f"Warning: Could not iterate as dict, trying as list: {e}")

            # Try as list/iterable
            if hasattr(result, "__iter__") and not isinstance(result, str):
                try:
                    return [_lua_to_python(item) for item in result]
                except (TypeError, AttributeError) as e:
                    print(f"Warning: Could not iterate as list: {e}")

            # Fallback: convert to Python type
            return _lua_to_python(result)

    except Exception as e:
        print(f"Error parsing {file_path} with lupa: {e}")
        import traceback

        traceback.print_exc()
        return None

    return None


def _lua_to_python(value) -> any:
    """Convert Lua value to Python value.

    :param value: Lua value.
    :return: Python value.
    """
    if value is None:
        return None
    if isinstance(value, str | int | float | bool):
        return value
    if isinstance(value, dict):
        # Lua table as dict
        result = {}
        for k, v in value.items():
            py_k = str(k) if not isinstance(k, str) else k
            py_v = _lua_to_python(v)
            result[py_k] = py_v
        return result
    if hasattr(value, "__iter__") and not isinstance(value, str):
        # Lua table as list/iterable
        try:
            # Check if it's actually a dict-like structure
            if hasattr(value, "items"):
                # Try to convert as dict first
                result = {}
                for k, v in value.items():
                    py_k = str(k) if not isinstance(k, str) else k
                    py_v = _lua_to_python(v)
                    result[py_k] = py_v
                return result
            # Otherwise treat as list
            return [_lua_to_python(item) for item in value]
        except (TypeError, AttributeError):
            return str(value)
    return str(value)


def parse_skills_lua(pob_path: Path) -> dict:
    """Parse all Skills/*.lua files.

    :param pob_path: Path to PoB repository.
    :return: Dictionary of skills {skillId: skillData}.
    """
    skill_types = [
        "act_str",  # Active Strength skills
        "act_dex",  # Active Dexterity skills
        "act_int",  # Active Intelligence skills
        "other",  # Other active skills
        "glove",  # Glove skills
        "minion",  # Minion skills
        "spectre",  # Spectre skills
        "sup_str",  # Support Strength gems
        "sup_dex",  # Support Dexterity gems
        "sup_int",  # Support Intelligence gems
    ]

    skills = {}
    # Try both paths: with and without "src"
    possible_skills_paths = [
        pob_path / "Data" / "Skills",
        pob_path / "src" / "Data" / "Skills",
    ]

    skills_path = None
    for path in possible_skills_paths:
        if path.exists():
            skills_path = path
            break

    if not skills_path:
        print(f"Error: Skills directory not found. Tried: {possible_skills_paths}")
        return {}

    for skill_type in skill_types:
        skills_file = skills_path / f"{skill_type}.lua"
        if not skills_file.exists():
            print(f"Warning: {skills_file} not found, skipping")
            continue

        print(f"Parsing {skills_file.name}...")
        skill_data = parse_lua_file_with_lupa(skills_file)
        if skill_data:
            # Merge into skills dict
            for skill_id, skill_info in skill_data.items():
                # Sanitise name
                if "name" in skill_info:
                    skill_info["name"] = sanitise_text(skill_info["name"])
                skill_info["id"] = skill_id
                skill_info["modSource"] = f"Skill:{skill_id}"
                skills[skill_id] = skill_info

    print(f"Loaded {len(skills)} skills")
    return skills


def parse_gems_lua(pob_path: Path) -> dict:
    """Parse Gems.lua file.

    :param pob_path: Path to PoB repository.
    :return: Dictionary of gems {gemId: gemData}.
    """
    # Try both paths: with and without "src"
    possible_gems_paths = [
        pob_path / "Data" / "Gems.lua",
        pob_path / "src" / "Data" / "Gems.lua",
    ]

    gems_file = None
    for path in possible_gems_paths:
        if path.exists():
            gems_file = path
            break

    if not gems_file:
        print(f"Error: Gems.lua not found. Tried: {possible_gems_paths}")
        return {}

    print(f"Parsing {gems_file.name}...")
    gems_raw = parse_lua_file_with_lupa(gems_file)
    if not gems_raw:
        return {}

    gems = {}
    # Handle both dict and list formats
    if isinstance(gems_raw, dict):
        gems = gems_raw
    elif isinstance(gems_raw, list):
        # Convert list to dict (if list of [key, value] pairs)
        for item in gems_raw:
            if isinstance(item, list | tuple) and len(item) == 2:
                gems[item[0]] = item[1]
            elif isinstance(item, dict) and "id" in item:
                gems[item["id"]] = item
    else:
        print(f"Warning: Unexpected gems format: {type(gems_raw)}")
        return {}

    # Sanitise names
    for gem_id, gem_data in gems.items():
        if not isinstance(gem_data, dict):
            print(f"Warning: Gem {gem_id} is not a dict, skipping")
            continue
        if "name" in gem_data:
            gem_data["name"] = sanitise_text(gem_data["name"])
        gem_data["id"] = gem_id

    print(f"Loaded {len(gems)} gems")
    return gems


def extract_base_damage_from_skill(skill: dict) -> dict[str, tuple[float, float]]:
    """Extract base damage from skill's baseMods.

    :param skill: Skill dictionary.
    :return: Dictionary of damage types to (min, max) tuples.
    """
    base_damage = {}
    base_mods = skill.get("baseMods", [])

    for mod in base_mods:
        mod_name = mod.get("name", "")
        mod_value = mod.get("value", 0)

        # Map modifier names to damage types
        damage_mapping = {
            "PhysicalDamageMin": ("Physical", 0),
            "PhysicalDamageMax": ("Physical", 1),
            "FireDamageMin": ("Fire", 0),
            "FireDamageMax": ("Fire", 1),
            "ColdDamageMin": ("Cold", 0),
            "ColdDamageMax": ("Cold", 1),
            "LightningDamageMin": ("Lightning", 0),
            "LightningDamageMax": ("Lightning", 1),
            "ChaosDamageMin": ("Chaos", 0),
            "ChaosDamageMax": ("Chaos", 1),
        }

        if mod_name in damage_mapping:
            dmg_type, is_max = damage_mapping[mod_name]
            if dmg_type not in base_damage:
                base_damage[dmg_type] = [0.0, 0.0]
            base_damage[dmg_type][is_max] = float(mod_value)

    # Convert lists to tuples
    return {k: (v[0], v[1]) for k, v in base_damage.items()}


def format_modifier(mod: dict) -> str:
    """Format modifier to stat string.

    :param mod: Modifier dictionary.
    :return: Formatted stat string.
    """
    mod_name = mod.get("name", "")
    # mod_type = mod.get("type", "")  # Not used
    mod_value = mod.get("value", 0)
    per_level = mod.get("perLevel", 0)

    # Basic formatting - can be enhanced
    if per_level:
        return f"{mod_name}: {mod_value} (per level: {per_level})"
    return f"{mod_name}: {mod_value}"


def extract_modifiers_from_skill(skill: dict) -> dict:
    """Extract modifiers from skill (qualityMods, levelMods).

    :param skill: Skill dictionary.
    :return: Dictionary with qualityStats and levelStats.
    """
    quality_stats = []
    level_stats = []

    # Process qualityMods
    for mod in skill.get("qualityMods", []):
        quality_stats.append(format_modifier(mod))

    # Process levelMods
    for mod in skill.get("levelMods", []):
        level_stats.append(format_modifier(mod))

    return {
        "qualityStats": quality_stats,
        "levelStats": level_stats,
    }


def link_gems_to_skills(gems: dict, skills: dict) -> dict:
    """Link gems to their corresponding skills.

    :param gems: Dictionary of gems.
    :param skills: Dictionary of skills.
    :return: Updated gems dictionary with linked skill data.
    """
    for gem_id, gem_data in gems.items():
        granted_effect_id = gem_data.get("grantedEffectId")
        if granted_effect_id and granted_effect_id in skills:
            skill = skills[granted_effect_id]
            gem_data["grantedEffect"] = skill

            # Extract data from skill
            base_damage = extract_base_damage_from_skill(skill)
            if base_damage:
                gem_data["baseDamage"] = {
                    k: [v[0], v[1]] for k, v in base_damage.items()
                }

            # Extract modifiers
            modifiers = extract_modifiers_from_skill(skill)
            gem_data["qualityStats"] = modifiers.get("qualityStats", [])
            gem_data["levelStats"] = modifiers.get("levelStats", [])

            # Extract other skill properties
            gem_data["castTime"] = skill.get("castTime")
            gem_data["attackTime"] = skill.get("attackTime")
            gem_data["isSpell"] = skill.get("isSpell", False)
            gem_data["isAttack"] = skill.get("isAttack", False)
            gem_data["isTotem"] = skill.get("isTotem", False)
            gem_data["isTrap"] = skill.get("isTrap", False)
            gem_data["isMine"] = skill.get("isMine", False)

            # Extract damage effectiveness from levels table
            levels = skill.get("levels", [])
            if levels and len(levels) > 0:
                # levels format: {level, manaCost, damageEffectiveness, ...}
                level_data = levels[0] if isinstance(levels[0], list) else levels[0]
                if isinstance(level_data, list) and len(level_data) > 2:
                    gem_data["damageEffectiveness"] = float(level_data[2])
                if isinstance(level_data, list) and len(level_data) > 1:
                    gem_data["manaCost"] = float(level_data[1])

    return gems


def process_special_gems(gems: dict) -> dict:
    """Process special gem types (Vaal, AltX/AltY, Support).

    :param gems: Dictionary of gems.
    :return: Updated gems dictionary.
    """
    for gem_id, gem_data in gems.items():
        # Vaal gems
        if "Vaal" in gem_id or gem_data.get("vaalGem", False):
            gem_data["isVaal"] = True
            if "secondaryGrantedEffectId" in gem_data:
                # Process secondary effect
                pass

        # Support gems
        granted_effect = gem_data.get("grantedEffect", {})
        if granted_effect.get("support", False):
            gem_data["isSupport"] = True
            gem_name = gem_data.get("name", "")
            if not gem_name.endswith(" Support"):
                gem_data["name"] = f"{gem_name} Support"

        # Alternative versions (AltX, AltY)
        if "AltX" in gem_id or "AltY" in gem_id:
            # Mark as alternative version
            gem_data["isAlternative"] = True

    return gems


def convert_tags_to_list(tags: dict | list) -> list[str]:
    """Convert tags from Lua format to list.

    :param tags: Tags as dict (Lua) or list.
    :return: List of tag names.
    """
    if isinstance(tags, list):
        return [str(tag) for tag in tags]
    if isinstance(tags, dict):
        # Lua format: {tag1 = true, tag2 = true, ...}
        return [str(k) for k, v in tags.items() if v]
    return []


def generate_gems_json(gems: dict, output_path: Path) -> None:
    """Generate gems.json from processed gems.

    :param gems: Dictionary of processed gems.
    :param output_path: Path to output JSON file.
    """
    gems_json = {"gems": {}}

    for gem_id, gem_data in gems.items():
        # Use name as key (fallback to gem_id)
        gem_name = gem_data.get("name", gem_id)

        # Convert tags
        tags = gem_data.get("tags", {})
        if tags:
            gem_data["tags"] = convert_tags_to_list(tags)

        # Build gem entry
        gem_entry = {
            "name": gem_data.get("name"),
            "gameId": gem_data.get("gameId"),
            "variantId": gem_data.get("variantId"),
            "grantedEffectId": gem_data.get("grantedEffectId"),
            "secondaryGrantedEffectId": gem_data.get("secondaryGrantedEffectId"),
            "reqStr": gem_data.get("reqStr", 0),
            "reqDex": gem_data.get("reqDex", 0),
            "reqInt": gem_data.get("reqInt", 0),
            "tags": gem_data.get("tags", []),
            "tagString": gem_data.get("tagString"),
            "naturalMaxLevel": gem_data.get("naturalMaxLevel", 20),
            "baseTypeName": gem_data.get("baseTypeName"),
            "isVaal": gem_data.get("isVaal", False),
            "isSupport": gem_data.get("isSupport", False),
            # Skill-derived data
            "baseDamage": gem_data.get("baseDamage", {}),
            "damageEffectiveness": gem_data.get("damageEffectiveness", 100.0),
            "castTime": gem_data.get("castTime"),
            "attackTime": gem_data.get("attackTime"),
            "manaCost": gem_data.get("manaCost"),
            "qualityStats": gem_data.get("qualityStats", []),
            "levelStats": gem_data.get("levelStats", []),
            "isAttack": gem_data.get("isAttack", False),
            "isSpell": gem_data.get("isSpell", False),
            "isTotem": gem_data.get("isTotem", False),
            "isTrap": gem_data.get("isTrap", False),
            "isMine": gem_data.get("isMine", False),
        }

        gems_json["gems"][gem_name] = gem_entry

    # Save to JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(gems_json, f, indent=2, ensure_ascii=False)

    print(f"\nSaved {len(gems_json['gems'])} gems to {output_path}")


def main():
    """Main function to extract gems from PoB."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract gems.json from Path of Building Lua files"
    )
    parser.add_argument(
        "--pob-path",
        type=str,
        help="Path to Path of Building repository",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output path for gems.json (default: data/gems.json)",
    )

    args = parser.parse_args()

    # Find PoB repository
    pob_path = args.pob_path
    if not pob_path:
        possible_paths = [
            Path.home() / "PathOfBuilding",
            Path.home() / "PathOfBuilding-Community",
            Path.cwd() / "PathOfBuilding",
            # Also check common installation paths
            Path("D:/Programs/Path of Building Community"),
            Path("C:/Program Files/Path of Building Community"),
        ]
        for path in possible_paths:
            if path.exists():
                # Check if Data directory exists (with or without src)
                if (path / "Data").exists() or (path / "src" / "Data").exists():
                    pob_path = str(path)
                    break

    if not pob_path:
        print("Error: Path of Building repository not found.")
        print("Please clone it or specify --pob-path:")
        print("  git clone https://github.com/PathOfBuildingCommunity/PathOfBuilding")
        return 1

    pob_path = Path(pob_path)
    print(f"Using PoB repository at: {pob_path}")

    if not LUA_AVAILABLE:
        print("\nError: lupa is required for parsing Lua files.")
        print("Install with: uv add lupa")
        return 1

    # Parse skills
    print("\n" + "=" * 80)
    print("Parsing Skills...")
    print("=" * 80)
    skills = parse_skills_lua(pob_path)

    # Parse gems
    print("\n" + "=" * 80)
    print("Parsing Gems...")
    print("=" * 80)
    gems = parse_gems_lua(pob_path)

    if not gems:
        print("Error: No gems loaded")
        return 1

    # Link gems to skills
    print("\n" + "=" * 80)
    print("Linking Gems to Skills...")
    print("=" * 80)
    gems = link_gems_to_skills(gems, skills)

    # Process special gems
    print("\n" + "=" * 80)
    print("Processing Special Gems...")
    print("=" * 80)
    gems = process_special_gems(gems)

    # Generate JSON
    output_path = args.output
    if not output_path:
        output_path = Path(__file__).parent.parent / "data" / "gems.json"
    else:
        output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print("\n" + "=" * 80)
    print("Generating gems.json...")
    print("=" * 80)
    generate_gems_json(gems, output_path)

    print("\n" + "=" * 80)
    print("Done!")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    sys.exit(main())
