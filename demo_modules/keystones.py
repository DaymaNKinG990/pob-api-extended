"""Module for displaying keystones."""

from pobapi import PathOfBuildingAPI


def print_keystones(build: PathOfBuildingAPI) -> None:
    """
    Print a formatted list of active keystones for the given PathOfBuildingAPI build.

    Prints each active keystone as "Display Name (field_name)". If no
    keystones are active, prints a diagnostic note including the number of
    keystones checked and possible reasons for none being active.

    Parameters:
        build (PathOfBuildingAPI): PoB build object from which keystone
            information will be read.
    """
    print("=" * 80)
    print("  10. Keystones")
    print("=" * 80)
    print()
    try:
        keystones = build.keystones
        # Get all keystone fields and their values
        import dataclasses

        keystone_fields = dataclasses.fields(keystones)
        active_keystones = []
        all_keystones = []

        for field in keystone_fields:
            value = getattr(keystones, field.name)
            all_keystones.append((field.name, value))
            if value:
                active_keystones.append(field.name)

        if active_keystones:
            print(f"Active keystones ({len(active_keystones)}):")
            for ks in active_keystones:
                # Format name: convert snake_case to Title Case
                display_name = ks.replace("_", " ").title()
                print(f"  - {display_name} ({ks})")
        else:
            print("Active keystones: None")
            print(f"\nNote: Checked {len(all_keystones)} keystones, none are active.")
            print("This could mean:")
            print("  1. The build has no keystones allocated")
            print("  2. Keystone IDs in constants may be outdated")
            print("  3. Keystones might be stored differently in this PoB version")
    except (AttributeError, IndexError) as e:
        print(f"Could not determine keystones: {e}")
        import traceback

        traceback.print_exc()


def main():
    """
    Demonstration entry point that constructs a PathOfBuildingAPI build
    from bundled demo code and prints its keystones.

    This sets up the import path for local utilities, uses the demo
    import_code to create a build via pobapi.from_import_code, and
    invokes print_keystones on the resulting build.
    """
    import sys
    from pathlib import Path

    # Add parent directory to path to import from utils
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pobapi import from_import_code
    from utils.demo_pobapi import import_code

    build = from_import_code(import_code())
    print_keystones(build)


if __name__ == "__main__":
    main()
