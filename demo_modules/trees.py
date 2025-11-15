"""Module for displaying skill trees."""

from pobapi import PathOfBuildingAPI


def print_trees(build: PathOfBuildingAPI) -> None:
    """Print all skill trees information.

    :param build: PathOfBuildingAPI instance.
    """
    print("=" * 80)
    print("  8. Skill Trees")
    print("=" * 80)
    print()
    print(f"Number of trees: {len(build.trees)}")
    for i, tree in enumerate(build.trees, 1):
        print(f"\n  Tree {i}:")
        print(f"    URL: {tree.url}")
        print(f"    Number of allocated nodes: {len(tree.nodes)}")
        print(f"    Number of jewel sockets: {len(tree.sockets)}")
        if tree.sockets:
            print("    Jewel sockets (Node ID -> Item ID):")
            for node_id, item_id in sorted(tree.sockets.items()):
                # Find item name if possible
                item_name = "Unknown"
                if item_id < len(build.items):
                    item = build.items[item_id]
                    item_name = item.name
                print(f"      Node {node_id} -> Item #{item_id + 1} ({item_name})")


def print_active_tree(build: PathOfBuildingAPI):
    """Print active skill tree information.

    :param build: PathOfBuildingAPI instance.
    :return: Active tree instance or None if not available.
    """
    print("=" * 80)
    print("  9. Active Skill Tree")
    print("=" * 80)
    print()
    try:
        active_tree = build.active_skill_tree
        print(f"URL: {active_tree.url}")
        print(f"Number of allocated nodes: {len(active_tree.nodes)}")
        print(f"Number of jewel sockets: {len(active_tree.sockets)}")
        if active_tree.sockets:
            print("Jewel sockets (Node ID -> Item ID):")
            for node_id, item_id in sorted(active_tree.sockets.items()):
                # Find item name if possible
                item_name = "Unknown"
                if item_id < len(build.items):
                    item = build.items[item_id]
                    item_name = item.name
                print(f"  Node {node_id} -> Item #{item_id + 1} ({item_name})")
        return active_tree
    except (IndexError, AttributeError) as e:
        print(f"Could not determine active skill tree: {e}")
        return None


def main():
    """Main function."""
    import sys
    from pathlib import Path

    # Add parent directory to path to import from utils
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pobapi import from_import_code
    from utils.demo_pobapi import import_code

    build = from_import_code(import_code())
    print_trees(build)


if __name__ == "__main__":
    main()
