"""Module for displaying skill trees."""

from pobapi import PathOfBuildingAPI


def print_trees(build: PathOfBuildingAPI) -> None:
    """
    Print a human-readable summary of all skill trees from the given
    PathOfBuildingAPI instance.

    For each tree this prints the tree index, tree URL, number of
    allocated nodes, and number of jewel sockets. If a tree has jewel
    sockets, prints "Node ID -> Item ID" mappings and attempts to resolve
    each socket's item name from build.items; uses "Unknown" when the item
    cannot be resolved.

    Parameters:
        build (PathOfBuildingAPI): Source build data containing trees,
            items, and sockets.
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
    """
    Display the active skill tree and its jewel-socket mappings.

    Parameters:
        build (PathOfBuildingAPI): PathOfBuildingAPI instance whose
            active skill tree will be displayed.

    Returns:
        active_tree: The active skill tree instance if available, `None` otherwise.
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
    """
    Construct a PathOfBuildingAPI build from the bundled demo import code
    and print its skill trees to standard output.
    """
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
