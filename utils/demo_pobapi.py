#!/usr/bin/env python3
"""Demo script to showcase pobapi capabilities with real import code."""

import sys
from contextlib import redirect_stdout
from datetime import datetime
from pathlib import Path

# Add parent directory to path to import demo_modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from demo_modules import (  # noqa: E402
    create_simple_build,
    print_active_skill,
    print_active_tree,
    print_build_info,
    print_calculations,
    print_config,
    print_item_sets,
    print_items,
    print_keystones,
    print_skill_gems,
    print_skill_groups,
    print_stats,
    print_trees,
)
from pobapi import from_import_code  # noqa: E402


def import_code():
    """Import code from user - read from file."""
    try:
        with open("data/import_code.txt", encoding="utf-8") as f:
            import_code_value = f.read().strip()
    except FileNotFoundError:
        print(
            "Error: data/import_code.txt not found. Please provide a valid import code."
        )
        import_code_value = ""
    return import_code_value


def print_section(title: str):
    """Print a formatted section header."""
    print(f"\n{'=' * 80}")
    print(f"  {title}")
    print(f"{'=' * 80}\n")


def main(output_file: str | None = None, use_created_build: bool = False):
    """Main demo function.

    :param output_file: Optional path to output file. If None, prints to stdout.
    :param use_created_build: If True, create a simple build programmatically
        instead of loading from import code.
    """
    # Determine output destination
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        file_handle = open(output_path, "w", encoding="utf-8")
        stdout_redirect = redirect_stdout(file_handle)
    else:
        file_handle = None
        stdout_redirect = None

    try:
        if stdout_redirect:
            stdout_redirect.__enter__()

        print_section("Path of Building API Demo")

        # Load or create build
        if use_created_build:
            print("Creating simple build programmatically...")
            build = create_simple_build()
            print("Build created successfully!\n")
        else:
            print("Loading build from import code...")
            build = from_import_code(import_code())
            print("Build loaded successfully!\n")

        # Display all information using modular functions
        print_build_info(build)
        print()
        print_stats(build)
        print()
        print_config(build)
        print()
        print_skill_groups(build)
        print()
        print_active_skill(build)
        print()
        print_skill_gems(build)
        print()
        print_items(build)
        print()
        print_item_sets(build)
        print()
        print_trees(build)
        print()
        active_tree = print_active_tree(build)
        print()
        print_keystones(build)
        print()
        print_calculations(build)
        print()

        # Summary
        print_section("Summary")
        print(f"Successfully parsed build for {build.class_name} (Level {build.level})")
        print(f"Extracted {len(build.skill_groups)} skill groups")
        print(f"Extracted {len(build.items)} items")
        print(f"Extracted {len(build.trees)} skill trees")
        if active_tree:
            print(f"Allocated {len(active_tree.nodes)} passive nodes")
        else:
            print("Could not determine allocated passive nodes")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
    finally:
        if stdout_redirect:
            stdout_redirect.__exit__(None, None, None)
        if file_handle:
            file_handle.close()
            if output_file:
                print(f"\nOutput saved to: {output_file}", file=sys.stderr)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Demo script for pobapi")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Output file path (default: output to stdout)",
    )
    parser.add_argument(
        "--auto-output",
        action="store_true",
        help="Automatically save to output/build_info_<timestamp>.txt",
    )
    parser.add_argument(
        "--create-build",
        action="store_true",
        help=(
            "Create a simple build programmatically instead of loading from import code"
        ),
    )

    args = parser.parse_args()

    # Auto-generate output filename if requested
    if args.auto_output:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"output/build_info_{timestamp}.txt"
    else:
        output_file = args.output

    main(output_file=output_file, use_created_build=args.create_build)
