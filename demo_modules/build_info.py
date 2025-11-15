"""Module for displaying basic build information."""

from pobapi import PathOfBuildingAPI


def print_build_info(build: PathOfBuildingAPI) -> None:
    """Print basic build information.

    :param build: PathOfBuildingAPI instance.
    """
    print("=" * 80)
    print("  1. Basic Build Information")
    print("=" * 80)
    print()
    print(f"Class: {build.class_name}")
    print(f"Ascendancy: {build.ascendancy_name}")
    print(f"Level: {build.level}")
    print(f"Bandit: {build.bandit}")
    print(f"Second Weapon Set: {build.second_weapon_set}")
    if build.notes:
        print("\nNotes:")
        # Notes are already cleaned from formatting codes by the API
        for line in build.notes.split("\n"):
            print(f"  {line}")


def main():
    """Main function."""
    import sys
    from pathlib import Path

    # Add parent directory to path to import from utils
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pobapi import from_import_code
    from utils.demo_pobapi import import_code

    build = from_import_code(import_code())
    print_build_info(build)


if __name__ == "__main__":
    main()
