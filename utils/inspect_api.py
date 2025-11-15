#!/usr/bin/env python3
"""Inspect all methods and objects of PathOfBuildingAPI recursively."""

import inspect
from typing import Any

from pobapi import from_import_code


def should_inspect_recursively(obj: Any) -> bool:
    """Check if object should be inspected recursively.

    :param obj: Object to check.
    :return: True if should inspect recursively.
    """
    if obj is None:
        return False
    if isinstance(obj, str | int | float | bool):
        return False
    if isinstance(obj, list | tuple | dict):
        return False
    if inspect.isclass(obj):
        return False
    if inspect.ismodule(obj):
        return False
    if callable(obj):
        return False
    return True


def get_attr_info(attr: Any) -> dict:
    """Get information about an attribute.

    :param attr: Attribute to inspect.
    :return: Dictionary with attribute information.
    """
    attr_type = type(attr).__name__
    is_callable = callable(attr)

    # Get value representation
    if is_callable:
        try:
            sig = inspect.signature(attr)
            value_repr = f"<method: {sig}>"
        except Exception:
            value_repr = f"<callable: {attr_type}>"
    elif isinstance(attr, str | int | float | bool | type(None)):
        value_repr = repr(attr) if len(repr(attr)) < 100 else repr(attr)[:100] + "..."
    elif isinstance(attr, list | tuple):
        value_repr = f"{attr_type}(length={len(attr)})"
    elif isinstance(attr, dict):
        value_repr = f"{attr_type}(keys={len(attr)})"
    else:
        value_repr = f"<{attr_type}>"

    return {
        "type": attr_type,
        "callable": is_callable,
        "value": value_repr,
        "object": attr if should_inspect_recursively(attr) else None,
    }


def print_structure(
    obj: Any,
    name: str = "root",
    level: int = 0,
    visited: set[int] | None = None,
    max_depth: int = 5,
):
    """Recursively print object structure.

    :param obj: Object to print.
    :param name: Name of the object.
    :param level: Current depth level.
    :param visited: Set of visited object IDs.
    :param max_depth: Maximum depth to traverse.
    """
    if visited is None:
        visited = set()

    if level > max_depth:
        print("  " * level + f"{name}: <max depth reached>")
        return

    indent = "  " * level
    obj_type = type(obj).__name__

    # Handle different types
    if isinstance(obj, str | int | float | bool | type(None)):
        print(f"{indent}{name}: {obj_type} = {repr(obj)}")
        return
    elif isinstance(obj, list | tuple):
        print(f"{indent}{name}: {obj_type}(length={len(obj)})")
        if len(obj) > 0 and level < max_depth:
            print(f"{indent}  [First item]:")
            print_structure(obj[0], "[0]", level + 2, visited, max_depth)
        return
    elif isinstance(obj, dict):
        print(f"{indent}{name}: {obj_type}(keys={len(obj)})")
        if len(obj) > 0 and level < max_depth:
            first_key = list(obj.keys())[0]
            print(f"{indent}  [First key '{first_key}']:")
            print_structure(
                obj[first_key], f"['{first_key}']", level + 2, visited, max_depth
            )
        return

    # For objects, get attributes
    print(f"{indent}{name}: {obj_type}")

    obj_id = id(obj)
    if obj_id in visited:
        print(f"{indent}  [Already visited - skipping]")
        return
    visited.add(obj_id)

    # Get all attributes
    attrs_dict = {}
    for attr_name in dir(obj):
        if attr_name.startswith("__") and attr_name.endswith("__"):
            continue  # Skip special methods

        try:
            attr = getattr(obj, attr_name)
            attrs_dict[attr_name] = get_attr_info(attr)
        except Exception as e:
            attrs_dict[attr_name] = {"error": str(e), "type": "Error"}

    # Sort attributes: callables first, then objects, then values
    def sort_key(item):
        name, info = item
        if not isinstance(info, dict):
            return (3, name)
        if "error" in info:
            return (4, name)
        if info.get("callable"):
            return (0, name)
        if info.get("object") is not None:
            return (1, name)
        return (2, name)

    sorted_attrs = sorted(attrs_dict.items(), key=sort_key)

    for attr_name, attr_info in sorted_attrs:
        if not isinstance(attr_info, dict):
            attr_repr = repr(attr_info)[:100]
            type_name = type(attr_info).__name__
            print(f"{indent}  {attr_name}: {type_name} = {attr_repr}")
            continue

        if "error" in attr_info:
            print(f"{indent}  {attr_name}: [Error: {attr_info['error']}]")
            continue

        attr_type = attr_info.get("type", "Unknown")
        is_callable = attr_info.get("callable", False)
        value_repr = attr_info.get("value", "")
        attr_obj = attr_info.get("object")

        if is_callable:
            print(f"{indent}  {attr_name}(): {value_repr}")
        elif attr_obj is not None and level < max_depth:
            # Recursively print object structure
            print_structure(attr_obj, attr_name, level + 1, visited, max_depth)
        else:
            print(f"{indent}  {attr_name}: {attr_type} = {value_repr}")


def main():
    """Main function."""
    print("=" * 80)
    print("PathOfBuildingAPI Structure Inspection")
    print("=" * 80)
    print()

    # Load build
    print("Loading build from import code...")
    try:
        with open("data/import_code.txt", encoding="utf-8") as f:
            import_code = f.read().strip()
        build = from_import_code(import_code)
        print("Build loaded successfully!\n")
    except Exception as e:
        print(f"Error loading build: {e}")
        return

    # Print structure
    print("=" * 80)
    print("Full API Structure:")
    print("=" * 80)
    print()

    print_structure(build, "PathOfBuildingAPI", max_depth=4)

    print()
    print("=" * 80)
    print("Inspection complete")
    print("=" * 80)


if __name__ == "__main__":
    import sys
    from contextlib import redirect_stdout

    # Check if output file is specified
    output_file = None
    if len(sys.argv) > 1:
        if sys.argv[1] in ["-o", "--output"] and len(sys.argv) > 2:
            output_file = sys.argv[2]
        elif sys.argv[1] == "--auto-output":
            from datetime import datetime
            from pathlib import Path

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"output/api_structure_{timestamp}.txt"
            Path("output").mkdir(exist_ok=True)

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            with redirect_stdout(f):
                main()
        print(f"\nOutput saved to: {output_file}", file=sys.stderr)
    else:
        main()
