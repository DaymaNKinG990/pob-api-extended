# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
# ]
# ///
"""Script to scrape unique items from poewiki.net.

This script collects all unique items from poewiki.net and generates
a JSON file with their data for use in GameDataLoader.

Note: This script requires beautifulsoup4:
    uv add beautifulsoup4 --script utils/scrape_unique_items.py

Usage:
    python utils/scrape_unique_items.py
"""

import json
import re
import time
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:
    print("Error: requests is required. Install with: uv add requests")
    exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: beautifulsoup4 is required. Install with: uv add beautifulsoup4")
    exit(1)

# Categories of unique items on poewiki.net
UNIQUE_CATEGORIES = [
    # Weapons
    "List_of_unique_weapons",
    "List_of_unique_axes",
    "List_of_unique_bows",
    "List_of_unique_claws",
    "List_of_unique_daggers",
    "List_of_unique_maces",
    "List_of_unique_sceptres",
    "List_of_unique_staves",
    "List_of_unique_swords",
    "List_of_unique_wands",
    # Armour
    "List_of_unique_armour",
    "List_of_unique_body_armours",
    "List_of_unique_boots",
    "List_of_unique_gloves",
    "List_of_unique_helmets",
    "List_of_unique_shields",
    # Jewellery
    "List_of_unique_jewellery",
    "List_of_unique_amulets",
    "List_of_unique_belts",
    "List_of_unique_rings",
    # Flasks
    "List_of_unique_flasks",
    "List_of_unique_life_flasks",
    "List_of_unique_mana_flasks",
    "List_of_unique_hybrid_flasks",
    "List_of_unique_utility_flasks",
    # Jewels
    "List_of_unique_jewels",
    # Maps
    "List_of_unique_maps",
    # Other
    "List_of_unique_tinctures",
    "List_of_unique_relics",
]

BASE_URL = "https://www.poewiki.net/wiki/"


def get_page_content(url: str) -> str | None:
    """Fetch page content from poewiki.net.

    :param url: URL to fetch.
    :return: HTML content or None if failed.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_unique_item_links(html: str) -> list[str]:
    """Extract links to unique item pages from a list page.

    :param html: HTML content of the list page.
    :return: List of unique item page names.
    """
    soup = BeautifulSoup(html, "html.parser")
    links: list[str] = []

    # Find all links in the page
    for link in soup.find_all("a", href=True):
        href = link.get("href", "")
        # Check if it's a link to a unique item page
        # Unique items usually don't have "List_of" or "Category:" in their URLs
        if (
            href.startswith("/wiki/")
            and "List_of" not in href
            and "Category:" not in href
            and "Template:" not in href
            and "File:" not in href
            and "User:" not in href
            and "Talk:" not in href
            and "Special:" not in href
            and "Help:" not in href
        ):
            page_name = href.replace("/wiki/", "")
            # Skip if it's a redirect or special page
            if page_name and not page_name.startswith("#"):
                links.append(page_name)

    return list(set(links))  # Remove duplicates


def extract_unique_item_data(html: str, item_name: str) -> dict[str, Any] | None:
    """Extract unique item data from its page.

    :param html: HTML content of the unique item page.
    :param item_name: Name of the unique item.
    :return: Dictionary with item data or None if failed.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Find the item stats table
    item_data: dict[str, Any] = {
        "name": item_name,
        "base_type": "",
        "implicit_mods": [],
        "explicit_mods": [],
        "special_effects": [],
    }

    # Look for item infobox (poewiki uses specific classes)
    infobox = soup.find("div", class_=re.compile(r"item.*box|infobox", re.I))
    if not infobox:
        # Try finding any table with item stats
        infobox = soup.find("table", class_=re.compile(r"item|stat", re.I))

    if infobox:
        # Extract base type from infobox
        base_type_elem = infobox.find(string=re.compile(r"Base.*Type|Type:", re.I))
        if base_type_elem:
            parent = base_type_elem.find_parent()
            if parent:
                next_sibling = parent.find_next_sibling()
                if next_sibling:
                    item_data["base_type"] = next_sibling.get_text(strip=True)

        # Extract all text lines that look like modifiers
        text_content = infobox.get_text("\n", strip=True)
        lines = [line.strip() for line in text_content.split("\n") if line.strip()]

        for line in lines:
            # Skip headers and labels
            if any(
                skip in line.lower()
                for skip in [
                    "rarity:",
                    "unique item",
                    "base type",
                    "type:",
                    "requires level",
                    "level req",
                ]
            ):
                continue

            # Check if it looks like a modifier
            if any(
                keyword in line.lower()
                for keyword in [
                    "%",
                    "+",
                    "-",
                    " to ",
                    "increased",
                    "more",
                    "reduced",
                    "less",
                    "converted",
                    "per ",
                    "chance",
                ]
            ):
                # Check if it's an implicit (usually first few lines)
                if len(item_data["explicit_mods"]) == 0 and "implicit" in line.lower():
                    item_data["implicit_mods"].append(line)
                else:
                    item_data["explicit_mods"].append(line)

    # Look for flavor text / description
    # poewiki usually has flavor text in italics or specific divs
    flavor_texts = soup.find_all(["i", "em"], string=re.compile(r".+"))
    for flavor in flavor_texts:
        text = flavor.get_text(strip=True)
        # Filter out very short texts and common phrases
        if len(text) > 20 and text not in item_data["special_effects"]:
            item_data["special_effects"].append(text)

    # Also check for quote blocks
    quote_blocks = soup.find_all("blockquote")
    for quote in quote_blocks:
        text = quote.get_text(strip=True)
        if text and len(text) > 10:
            item_data["special_effects"].append(text)

    return item_data


def scrape_all_unique_items(
    output_file: str = "data/uniques_scraped.json", resume: bool = True
) -> None:
    """Scrape all unique items from poewiki.net.

    :param output_file: Output JSON file path.
    :param resume: Whether to resume from existing file if it exists.
    """
    all_unique_items: dict[str, dict[str, Any]] = {}
    all_links: set[str] = set()

    # Try to resume from existing file
    if resume and Path(output_file).exists():
        try:
            with open(output_file, encoding="utf-8") as f:
                existing_data = json.load(f)
                if "uniques" in existing_data:
                    all_unique_items = existing_data["uniques"]
                    print(f"Resuming: Found {len(all_unique_items)} existing items")
        except Exception as e:
            print(f"Could not load existing file: {e}")

    print("Collecting unique item links from category pages...")

    # First, collect all links from category pages
    for category in UNIQUE_CATEGORIES:
        url = f"{BASE_URL}{category}"
        print(f"Fetching {category}...")
        html = get_page_content(url)
        if html:
            links = extract_unique_item_links(html)
            all_links.update(links)
            print(f"  Found {len(links)} links")
        time.sleep(1)  # Be polite to the server

    print(f"\nTotal unique item links collected: {len(all_links)}")

    # Filter out already scraped items
    items_to_scrape = sorted(set(all_links) - set(all_unique_items.keys()))
    skipped = len(all_unique_items)
    print(
        f"Items to scrape: {len(items_to_scrape)} (skipping {skipped} already scraped)"
    )

    if not items_to_scrape:
        print("All items already scraped!")
        return

    # Now scrape each unique item page
    print("\nScraping unique item pages...")
    for i, item_name in enumerate(items_to_scrape, 1):
        url = f"{BASE_URL}{item_name}"
        print(f"[{i}/{len(items_to_scrape)}] Fetching {item_name}...")

        html = get_page_content(url)
        if html:
            item_data = extract_unique_item_data(html, item_name)
            if item_data:
                all_unique_items[item_name] = item_data
                print("  [OK] Extracted data")
            else:
                print("  [FAIL] Failed to extract data")
        else:
            print("  [FAIL] Failed to fetch page")

        time.sleep(1)  # Be polite to the server

        # Save progress every 10 items
        if i % 10 == 0:
            save_progress(all_unique_items, output_file)
            print(f"  Progress saved ({i}/{len(items_to_scrape)})")

    # Final save
    save_progress(all_unique_items, output_file)
    count = len(all_unique_items)
    print(f"\n[OK] Scraping complete! Saved {count} unique items to {output_file}")


def save_progress(data: dict[str, Any], output_file: str) -> None:
    """Save progress to JSON file.

    :param data: Data to save.
    :param output_file: Output file path.
    """
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Format for GameDataLoader
    formatted_data = {"uniques": data}

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    import sys

    output_file = sys.argv[1] if len(sys.argv) > 1 else "data/uniques_scraped.json"
    print("Starting scrape of unique items from poewiki.net")
    print(f"Output file: {output_file}")
    print("Note: This will take a long time (~20 minutes for 1,192 items)")
    print("Progress is saved every 10 items, so you can safely interrupt and resume.\n")

    scrape_all_unique_items(output_file=output_file)
