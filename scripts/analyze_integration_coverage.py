#!/usr/bin/env python3
"""Analyze integration test coverage.

This script analyzes integration tests to determine which component
integrations are covered by tests.
"""

import ast
import re
from pathlib import Path
from typing import Any

# Component mapping: module name -> component names
COMPONENT_MAP = {
    "pobapi.api": ["PathOfBuildingAPI"],
    "pobapi.build_modifier": ["BuildModifier"],
    "pobapi.build_builder": ["BuildBuilder"],
    "pobapi.serializers": ["BuildXMLSerializer", "ImportCodeGenerator"],
    "pobapi.parsers": [
        "BuildInfoParser",
        "SkillsParser",
        "ItemsParser",
        "TreesParser",
        "DefaultBuildParser",
    ],
    "pobapi.validators": ["InputValidator", "XMLValidator"],
    "pobapi.factory": ["BuildFactory"],
    "pobapi.calculator.engine": ["CalculationEngine"],
    "pobapi.calculator.modifiers": ["ModifierSystem"],
    "pobapi.calculator.damage": ["DamageCalculator"],
    "pobapi.calculator.defense": ["DefenseCalculator"],
    "pobapi.calculator.resource": ["ResourceCalculator"],
    "pobapi.calculator.skill_stats": ["SkillStatsCalculator"],
    "pobapi.calculator.minion": ["MinionCalculator"],
    "pobapi.calculator.party": ["PartyCalculator"],
    "pobapi.calculator.passive_tree_parser": ["PassiveTreeParser"],
    "pobapi.calculator.item_modifier_parser": ["ItemModifierParser"],
    "pobapi.calculator.game_data": ["GameDataLoader"],
    "pobapi.trade": ["TradeAPI"],
    "pobapi.crafting": ["ItemCraftingAPI"],
    "pobapi.util": ["HTTPClient"],
    "pobapi.async_util": ["AsyncHTTPClient"],
    "pobapi.cache": ["Cache"],
}


def extract_imports_from_file(file_path: Path) -> set[str]:
    """Extract all imported components from a test file."""
    imports: set[str] = set()

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        # Parse AST
        tree = ast.parse(content)

        # Extract imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module)
                    if node.names:
                        for alias in node.names:
                            imports.add(f"{node.module}.{alias.name}")

    except Exception as e:
        print(f"Error parsing {file_path}: {e}")

    return imports


def find_components_in_imports(imports: set[str]) -> set[str]:
    """Find which components are used based on imports."""
    components: set[str] = set()

    for imp in imports:
        # Check direct module match
        if imp in COMPONENT_MAP:
            components.update(COMPONENT_MAP[imp])

        # Check if import is from a module we track
        for module, comps in COMPONENT_MAP.items():
            if imp.startswith(module):
                # Check for specific component imports
                for comp in comps:
                    if comp in imp or imp.endswith(comp):
                        components.add(comp)

        # Check for direct component name
        for module, comps in COMPONENT_MAP.items():
            for comp in comps:
                if comp in imp:
                    components.add(comp)

    return components


def analyze_test_file(file_path: Path) -> dict[str, Any]:
    """Analyze a single test file for component integrations."""
    imports = extract_imports_from_file(file_path)
    components = find_components_in_imports(imports)

    # Count test classes and methods
    test_classes = 0
    test_methods = 0

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        # Count test classes
        test_classes = len(re.findall(r"class\s+Test\w+", content))

        # Count test methods
        test_methods = len(re.findall(r"def\s+test_\w+", content))

    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")

    return {
        "file": file_path.name,
        "components": sorted(components),
        "test_classes": test_classes,
        "test_methods": test_methods,
        "imports": sorted(imports),
    }


def find_integration_pairs(components: set[str]) -> list[tuple[str, str]]:
    """Find all pairs of components that could be integrated."""
    pairs = []
    comp_list = sorted(components)

    for i, comp1 in enumerate(comp_list):
        for comp2 in comp_list[i + 1 :]:
            pairs.append((comp1, comp2))

    return pairs


def generate_coverage_report() -> None:
    """Generate integration coverage report."""
    tests_dir = Path(__file__).parent.parent / "tests" / "integrations"

    if not tests_dir.exists():
        print(f"Tests directory not found: {tests_dir}")
        return

    # Analyze all test files
    test_files = list(tests_dir.glob("test_*.py"))
    results = []

    for test_file in test_files:
        if test_file.name == "__init__.py":
            continue
        result = analyze_test_file(test_file)
        results.append(result)

    # Generate component pairs
    all_components: set[str] = set()
    for result in results:
        all_components.update(result["components"])

    # Find all possible pairs
    all_pairs = find_integration_pairs(all_components)

    # Find covered pairs
    covered_pairs: set[tuple[str, str]] = set()
    for result in results:
        if len(result["components"]) >= 2:
            pairs = find_integration_pairs(set(result["components"]))
            covered_pairs.update(pairs)

    # Print report
    print("=" * 80)
    print("Integration Test Coverage Report")
    print("=" * 80)
    print()

    print(f"Total Integration Test Files: {len(results)}")
    print(f"Total Test Classes: {sum(r['test_classes'] for r in results)}")
    print(f"Total Test Methods: {sum(r['test_methods'] for r in results)}")
    print()

    print("Component Coverage by File:")
    print("-" * 80)
    for result in results:
        print(f"\n{result['file']}:")
        print(f"  Components: {', '.join(result['components']) or 'None detected'}")
        print(f"  Test Classes: {result['test_classes']}")
        print(f"  Test Methods: {result['test_methods']}")

    print()
    print("=" * 80)
    print("Coverage Statistics")
    print("=" * 80)
    print(f"Total Possible Component Pairs: {len(all_pairs)}")
    print(f"Covered Component Pairs: {len(covered_pairs)}")
    if all_pairs:
        coverage_pct = (len(covered_pairs) / len(all_pairs)) * 100
        print(f"Coverage Percentage: {coverage_pct:.1f}%")
    print()

    print("Covered Component Pairs:")
    print("-" * 80)
    for comp1, comp2 in sorted(covered_pairs):
        print(f"  {comp1} <-> {comp2}")

    print()
    print("Missing Component Pairs:")
    print("-" * 80)
    missing_pairs = set(all_pairs) - covered_pairs
    for comp1, comp2 in sorted(missing_pairs):
        print(f"  {comp1} <-> {comp2}")


if __name__ == "__main__":
    generate_coverage_report()
