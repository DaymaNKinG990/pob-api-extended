"""Check progress of unique items scraping."""

import json
from pathlib import Path


def check_progress(file_path: str = "data/uniques_scraped.json") -> None:
    """Check scraping progress.

    :param file_path: Path to scraped data file.
    """
    path = Path(file_path)

    if not path.exists():
        print(f"File {file_path} does not exist yet.")
        print("Scraping has not started or file is being created.")
        return

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        if "uniques" in data:
            count = len(data["uniques"])
            print(f"Progress: {count} unique items scraped")
            print(f"File: {file_path}")
            print(f"File size: {path.stat().st_size / 1024:.2f} KB")

            # Show some examples
            if count > 0:
                print("\nSample items:")
                for i, (name, item_data) in enumerate(
                    list(data["uniques"].items())[:5]
                ):
                    base_type = item_data.get("base_type", "Unknown")
                    mods_count = len(item_data.get("explicit_mods", []))
                    print(f"  {i + 1}. {name} ({base_type}) - {mods_count} modifiers")
        else:
            print("File exists but has no 'uniques' key")
    except json.JSONDecodeError:
        print(f"File {file_path} exists but is not valid JSON (might be incomplete)")
    except Exception as e:
        print(f"Error reading file: {e}")


if __name__ == "__main__":
    check_progress()
