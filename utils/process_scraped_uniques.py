"""Process scraped unique items data.

This script processes the scraped unique items data:
- Decodes URL-encoded names
- Improves base_type extraction
- Cleans up modifiers
- Validates data
"""

import json
import re
from pathlib import Path
from urllib.parse import unquote


def process_scraped_uniques(
    input_file: str = "data/uniques_scraped.json",
    output_file: str = "data/uniques_processed.json",
) -> None:
    """Process scraped unique items data.

    :param input_file: Input file with scraped data.
    :param output_file: Output file with processed data.
    """
    print(f"Processing unique items from {input_file}...")

    with open(input_file, encoding="utf-8") as f:
        data = json.load(f)

    processed_uniques: dict[str, dict[str, any]] = {}

    for item_name_encoded, item_data in data["uniques"].items():
        # Decode URL-encoded name
        item_name = unquote(item_name_encoded).replace("_", " ")

        # Create processed item data
        processed_item: dict[str, any] = {
            "name": item_name,
            "base_type": item_data.get("base_type", "").strip(),
            "implicit_mods": [],
            "explicit_mods": [],
            "special_effects": item_data.get("special_effects", []),
        }

        # Clean up implicit mods
        for mod in item_data.get("implicit_mods", []):
            mod_clean = mod.strip()
            if mod_clean and len(mod_clean) > 2:
                processed_item["implicit_mods"].append(mod_clean)

        # Clean up explicit mods
        for mod in item_data.get("explicit_mods", []):
            mod_clean = mod.strip()
            # Filter out incomplete modifiers
            if (
                mod_clean
                and len(mod_clean) > 3
                and not mod_clean.endswith(":")
                and not mod_clean.startswith("(")
                or "%" in mod_clean
                or "+" in mod_clean
                or "-" in mod_clean
            ):
                processed_item["explicit_mods"].append(mod_clean)

        # Try to extract base_type from modifiers if missing
        if not processed_item["base_type"]:
            # Look for base type in modifiers or special effects
            all_text = " ".join(
                processed_item["explicit_mods"] + processed_item["special_effects"]
            )
            # Common base type patterns
            base_patterns = [
                # "Requires Level X, Y Str, Z Int" -> base type might be nearby
                r"Requires Level \d+.*?(\w+ \w+)",
                r"(\w+ \w+ \w+)",  # Three word base types
            ]
            for pattern in base_patterns:
                match = re.search(pattern, all_text, re.IGNORECASE)
                if match:
                    potential_base = match.group(1)
                    # Filter out common non-base-type phrases
                    if not any(
                        skip in potential_base.lower()
                        for skip in [
                            "requires level",
                            "to maximum",
                            "increased",
                            "reduced",
                            "chance to",
                        ]
                    ):
                        processed_item["base_type"] = potential_base
                        break

        # Use decoded name as key
        processed_uniques[item_name] = processed_item

    # Save processed data
    output_data = {"uniques": processed_uniques}

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print("\n[OK] Processing complete!")
    print(f"  Input: {len(data['uniques'])} items")
    print(f"  Output: {len(processed_uniques)} items")
    items_with_base = sum(1 for v in processed_uniques.values() if v.get("base_type"))
    print(f"  Items with base_type: {items_with_base}")
    items_with_mods = sum(
        1 for v in processed_uniques.values() if v.get("explicit_mods")
    )
    print(f"  Items with modifiers: {items_with_mods}")
    print(f"  Saved to: {output_file}")


if __name__ == "__main__":
    import sys

    input_file = sys.argv[1] if len(sys.argv) > 1 else "data/uniques_scraped.json"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "data/uniques_processed.json"

    process_scraped_uniques(input_file, output_file)
