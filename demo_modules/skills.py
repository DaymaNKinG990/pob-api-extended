"""Module for displaying skills and skill groups."""

from pobapi import PathOfBuildingAPI


def print_skill_groups(build: PathOfBuildingAPI) -> None:
    """Print skill groups information.

    :param build: PathOfBuildingAPI instance.
    """
    print("=" * 80)
    print("  4. Skill Groups")
    print("=" * 80)
    print()

    # Show active skill group first
    try:
        active_group = build.active_skill_group
        print("Active Skill Group:")
        print(f"  Enabled: {active_group.enabled}")
        print(f"  Label: {active_group.label or '(no label)'}")
        print(f"  Main Active Skill Index: {active_group.active}")
        print(f"  Number of abilities: {len(active_group.abilities)}")
        for j, ability in enumerate(active_group.abilities, 1):
            print(f"\n    Ability {j}:")
            print(f"      Name: {ability.name}")
            print(f"      Enabled: {ability.enabled}")
            print(f"      Level: {ability.level}")
            if hasattr(ability, "quality") and ability.quality is not None:
                print(f"      Quality: {ability.quality}%")
            if hasattr(ability, "support"):
                print(f"      Support: {ability.support}")
        print()
    except (IndexError, AttributeError) as e:
        print(f"Could not determine active skill group: {e}\n")

    print(f"Number of skill groups: {len(build.skill_groups)}")
    for i, group in enumerate(build.skill_groups, 1):
        print(f"\n  Skill Group {i}:")
        print(f"    Enabled: {group.enabled}")
        print(f"    Label: {group.label}")
        print(f"    Main Active Skill Index: {group.active}")
        print(f"    Number of abilities: {len(group.abilities)}")
        for j, ability in enumerate(group.abilities, 1):  # Show all abilities
            print(f"\n      Ability {j}:")
            print(f"        Name: {ability.name}")
            print(f"        Enabled: {ability.enabled}")
            print(f"        Level: {ability.level}")
            # Gem has quality and support fields,
            # GrantedAbility has them but they're always None/False
            if hasattr(ability, "quality") and ability.quality is not None:
                print(f"        Quality: {ability.quality}%")
            if hasattr(ability, "support"):
                print(f"        Support: {ability.support}")


def print_active_skill(build: PathOfBuildingAPI) -> None:
    """Print active skill information.

    :param build: PathOfBuildingAPI instance.
    """
    print("=" * 80)
    print("  5. Active Skill")
    print("=" * 80)
    print()
    if len(build.skill_groups) > 0:
        try:
            active_skill = build.active_skill
            if active_skill is None:
                print("No active skill selected (active index is None)")
            else:
                print(f"Name: {active_skill.name}")
                print(f"Level: {active_skill.level}")
                if hasattr(active_skill, "quality"):
                    print(f"Quality: {active_skill.quality}")
                if hasattr(active_skill, "support"):
                    print(f"Support: {active_skill.support}")
        except (IndexError, AttributeError, TypeError) as e:
            print(f"Could not determine active skill: {e}")
    else:
        print("No skill groups available")


def print_skill_gems(build: PathOfBuildingAPI) -> None:
    """Print all skill gems information.

    :param build: PathOfBuildingAPI instance.
    """
    print("=" * 80)
    print("  5a. All Skill Gems")
    print("=" * 80)
    print()
    skill_gems = build.skill_gems
    print(f"Total skill gems: {len(skill_gems)}")

    # Group by name for better readability
    gems_by_name = {}
    for gem in skill_gems:
        if gem.name not in gems_by_name:
            gems_by_name[gem.name] = []
        gems_by_name[gem.name].append(gem)

    print(f"Unique gem names: {len(gems_by_name)}")
    print("\nGems (grouped by name):")
    for gem_name in sorted(gems_by_name.keys()):
        gems = gems_by_name[gem_name]
        print(f"\n  {gem_name} ({len(gems)} instance(s)):")
        for i, gem in enumerate(gems, 1):
            print(f"    Instance {i}:")
            print(f"      Enabled: {gem.enabled}")
            print(f"      Level: {gem.level}")
            print(f"      Quality: {gem.quality}%")
            print(f"      Support: {gem.support}")


def main():
    """Main function."""
    import sys
    from pathlib import Path

    # Add parent directory to path to import from utils
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pobapi import from_import_code
    from utils.demo_pobapi import import_code

    build = from_import_code(import_code())
    print_skill_groups(build)


if __name__ == "__main__":
    main()
