"""Module for displaying basic build information."""

from pobapi import PathOfBuildingAPI


def print_build_info(build: PathOfBuildingAPI) -> None:
    """
    Display basic information from a PathOfBuildingAPI build.

    Parameters:
        build (PathOfBuildingAPI): Build whose `class_name`,
            `ascendancy_name`, `level`, `bandit`, `second_weapon_set`, and
            optional `notes` will be printed. If `notes` is present, each
            line will be printed on its own indented line.
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
    """
    Prepare the environment, construct a PathOfBuildingAPI build from
    bundled demo code, and print its basic information.

    This adds the repository parent directory to sys.path to enable
    importing the demo helper, decodes the demo build with
    `from_import_code(import_code())`, and calls `print_build_info` to
    display the build's details.
    """
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
