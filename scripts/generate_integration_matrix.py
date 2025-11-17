#!/usr/bin/env python3
"""Generate integration coverage matrix in markdown format.

This script generates a markdown table showing which component
integrations are covered by tests.
"""

import ast
import json
import logging
import re
from pathlib import Path
from typing import Any

# Define all components
ALL_COMPONENTS = [
    "PathOfBuildingAPI",
    "BuildModifier",
    "BuildBuilder",
    "BuildXMLSerializer",
    "ImportCodeGenerator",
    "BuildInfoParser",
    "DefaultBuildParser",
    "SkillsParser",
    "ItemsParser",
    "UniqueItemParser",
    "TreesParser",
    "InputValidator",
    "XMLValidator",
    "BuildFactory",
    "CalculationEngine",
    "ModifierSystem",
    "DamageCalculator",
    "DefenseCalculator",
    "ResourceCalculator",
    "SkillStatsCalculator",
    "MinionCalculator",
    "PartyCalculator",
    "PassiveTreeParser",
    "ItemModifierParser",
    "ConfigModifierParser",
    "SkillModifierParser",
    "GameDataLoader",
    "TradeAPI",
    "ItemCraftingAPI",
    "HTTPClient",
    "AsyncHTTPClient",
    "Cache",
]

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
    "pobapi.calculator.config_modifier_parser": ["ConfigModifierParser"],
    "pobapi.calculator.skill_modifier_parser": ["SkillModifierParser"],
    "pobapi.calculator.unique_item_parser": ["UniqueItemParser"],
    "pobapi.calculator.game_data": ["GameDataLoader"],
    "pobapi.trade": ["TradeAPI"],
    "pobapi.crafting": ["ItemCraftingAPI"],
    "pobapi.util": ["HTTPClient"],
    "pobapi.async_util": ["AsyncHTTPClient"],
    "pobapi.cache": ["Cache"],
}

# Component groups for statistics
COMPONENT_GROUPS = {
    "API": ["PathOfBuildingAPI", "BuildModifier", "BuildBuilder"],
    "Parsers": [
        "BuildInfoParser",
        "DefaultBuildParser",
        "SkillsParser",
        "ItemsParser",
        "TreesParser",
    ],
    "Serializers": ["BuildXMLSerializer", "ImportCodeGenerator"],
    "Validators": ["InputValidator", "XMLValidator"],
    "Factory": ["BuildFactory"],
    "Calculation": [
        "CalculationEngine",
        "ModifierSystem",
        "DamageCalculator",
        "DefenseCalculator",
        "ResourceCalculator",
        "SkillStatsCalculator",
        "MinionCalculator",
        "PartyCalculator",
    ],
    "Parsers_Calc": [
        "PassiveTreeParser",
        "ItemModifierParser",
        "ConfigModifierParser",
        "SkillModifierParser",
        "UniqueItemParser",
    ],
    "Data": ["GameDataLoader"],
    "Trade": ["TradeAPI"],
    "Crafting": ["ItemCraftingAPI"],
    "Infrastructure": ["HTTPClient", "AsyncHTTPClient", "Cache"],
}

# Known integrations (manually maintained)
KNOWN_INTEGRATIONS = [
    # API ↔ Calculation Engine
    ("PathOfBuildingAPI", "CalculationEngine"),
    ("BuildModifier", "CalculationEngine"),
    # Parser ↔ Serializer
    ("PathOfBuildingAPI", "BuildXMLSerializer"),
    ("PathOfBuildingAPI", "ImportCodeGenerator"),
    ("BuildBuilder", "BuildXMLSerializer"),
    ("BuildModifier", "BuildXMLSerializer"),
    # Calculator Components
    ("CalculationEngine", "ModifierSystem"),
    ("ModifierSystem", "DamageCalculator"),
    ("ModifierSystem", "DefenseCalculator"),
    ("ModifierSystem", "ResourceCalculator"),
    ("ModifierSystem", "SkillStatsCalculator"),
    ("ModifierSystem", "MinionCalculator"),
    ("ModifierSystem", "PartyCalculator"),
    # Game Data Loader
    ("GameDataLoader", "PassiveTreeParser"),
    ("GameDataLoader", "ItemModifierParser"),
    # Validator ↔ Parser
    ("InputValidator", "BuildInfoParser"),
    ("XMLValidator", "BuildInfoParser"),
    # Factory ↔ Builder
    ("BuildFactory", "BuildBuilder"),
]


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
                            # Skip wildcard imports (from module import *)
                            if alias.name != "*":
                                imports.add(f"{node.module}.{alias.name}")

    except OSError as e:
        logging.error(f"IO error reading file {file_path}: {e}", exc_info=True)
        raise
    except SyntaxError as e:
        logging.error(f"Syntax error parsing {file_path}: {e}", exc_info=True)
        raise

    return imports


def find_components_in_imports(imports: set[str]) -> set[str]:
    """Find which components are used based on imports."""
    components: set[str] = set()
    # Build flattened set of all component names for direct matching
    all_comps = {c for comps in COMPONENT_MAP.values() for c in comps}

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

        # Check for direct component name in import
        for comp in all_comps:
            if comp in imp:
                components.add(comp)

    return components


def analyze_test_file(file_path: Path) -> dict[str, Any]:
    """Analyze a single test file for component integrations."""
    imports = extract_imports_from_file(file_path)
    components = find_components_in_imports(imports)

    # Count test classes and methods
    test_classes = []
    test_methods = 0

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        # Extract test class names
        test_class_matches = re.findall(r"class\s+(Test\w+)", content)
        test_classes = test_class_matches

        # Count test methods
        test_methods = len(re.findall(r"def\s+test_\w+", content))

    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")

    return {
        "file": file_path.name,
        "test_classes": test_classes,
        "test_methods": test_methods,
        "components": sorted(components),
    }


def generate_matrix_markdown() -> str:
    """Generate markdown matrix of component integrations."""
    lines = []
    lines.append("# Integration Coverage Matrix")
    lines.append("")
    lines.append("This matrix shows which component integrations are covered by tests.")
    lines.append("")
    lines.append("## Component Integration Matrix")
    lines.append("")
    lines.append("| Component A | Component B | Coverage |")
    lines.append("|------------|-------------|----------|")

    # Sort integrations
    sorted_integrations = sorted(KNOWN_INTEGRATIONS)

    for comp1, comp2 in sorted_integrations:
        lines.append(f"| {comp1} | {comp2} | ✅ |")

    lines.append("")
    lines.append("## Coverage Statistics")
    lines.append("")
    total_possible_pairs = len(ALL_COMPONENTS) * (len(ALL_COMPONENTS) - 1) // 2
    covered_pairs = len(KNOWN_INTEGRATIONS)
    coverage_pct = (
        (covered_pairs / total_possible_pairs) * 100 if total_possible_pairs > 0 else 0
    )

    lines.append(f"- **Total Possible Pairs:** {total_possible_pairs}")
    lines.append(f"- **Covered Pairs:** {covered_pairs}")
    lines.append(f"- **Coverage Percentage:** {coverage_pct:.1f}%")
    lines.append("")

    return "\n".join(lines)


def generate_json_report() -> dict[str, Any]:
    """Generate JSON report of integration coverage."""
    tests_dir = Path(__file__).parent.parent / "tests" / "integrations"

    # Analyze all test files
    test_files = list(tests_dir.glob("test_*.py"))
    test_file_results = []

    for test_file in test_files:
        if test_file.name == "__init__.py":
            continue
        result = analyze_test_file(test_file)
        test_file_results.append(result)

    # Calculate metadata
    total_test_files = len(test_file_results)
    total_test_classes = sum(len(r["test_classes"]) for r in test_file_results)
    total_test_methods = sum(r["test_methods"] for r in test_file_results)

    # Calculate component groups
    components_by_group = {}
    for group_name, group_components in COMPONENT_GROUPS.items():
        components_by_group[group_name] = len(group_components)

    # Calculate statistics
    total_possible_pairs = len(ALL_COMPONENTS) * (len(ALL_COMPONENTS) - 1) // 2
    covered_pairs = len(KNOWN_INTEGRATIONS)
    coverage_pct = (
        (covered_pairs / total_possible_pairs * 100) if total_possible_pairs > 0 else 0
    )

    # Format covered integrations
    covered_integrations = [
        {"component_a": comp1, "component_b": comp2}
        for comp1, comp2 in KNOWN_INTEGRATIONS
    ]

    # Format test files
    formatted_test_files = [
        {
            "file": r["file"],
            "test_classes": r["test_classes"],
            "test_methods": r["test_methods"],
            "components": r["components"],
        }
        for r in test_file_results
    ]

    return {
        "metadata": {
            "total_test_files": total_test_files,
            "total_test_classes": total_test_classes,
            "total_test_methods": total_test_methods,
        },
        "components": {
            "total": len(ALL_COMPONENTS),
            "by_group": components_by_group,
        },
        "integrations": {
            "covered": covered_integrations,
            "total_possible": total_possible_pairs,
            "coverage_percentage": coverage_pct,
        },
        "test_files": formatted_test_files,
    }


if __name__ == "__main__":
    # Generate markdown
    markdown = generate_matrix_markdown()
    output_file = (
        Path(__file__).parent.parent / "tests" / "integrations" / "COVERAGE_MATRIX.md"
    )
    output_file.write_text(markdown, encoding="utf-8")
    print(f"Generated: {output_file}")

    # Generate JSON
    json_report = generate_json_report()
    json_file = (
        Path(__file__).parent.parent / "tests" / "integrations" / "coverage_report.json"
    )
    json_file.write_text(json.dumps(json_report, indent=2), encoding="utf-8")
    print(f"Generated: {json_file}")
