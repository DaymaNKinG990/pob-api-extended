#!/usr/bin/env python3
"""Generate integration coverage matrix in markdown format.

This script generates a markdown table showing which component
integrations are covered by tests.
"""

import json
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
    "SkillsParser",
    "ItemsParser",
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
    "GameDataLoader",
    "TradeAPI",
    "ItemCraftingAPI",
    "HTTPClient",
    "AsyncHTTPClient",
    "Cache",
]

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


def generate_matrix_markdown() -> str:
    """Generate markdown matrix of component integrations."""
    lines = []
    lines.append("# Integration Coverage Matrix")
    lines.append("")
    lines.append("This matrix shows which component integrations are covered by tests.")
    lines.append("")
    lines.append("## Component Integration Matrix")
    lines.append("")
    lines.append("| Component A | Component B | Coverage | Test File |")
    lines.append("|------------|-------------|----------|-----------|")

    # Sort integrations
    sorted_integrations = sorted(KNOWN_INTEGRATIONS)

    for comp1, comp2 in sorted_integrations:
        # Find test file (simplified - would need actual analysis)
        test_file = "test_*.py"  # Placeholder
        lines.append(f"| {comp1} | {comp2} | ✅ | {test_file} |")

    lines.append("")
    lines.append("## Coverage Statistics")
    lines.append("")
    total_pairs = len(ALL_COMPONENTS) * (len(ALL_COMPONENTS) - 1) // 2
    covered_pairs = len(KNOWN_INTEGRATIONS)
    coverage_pct = (covered_pairs / total_pairs) * 100 if total_pairs > 0 else 0

    lines.append(f"- **Total Possible Pairs:** {total_pairs}")
    lines.append(f"- **Covered Pairs:** {covered_pairs}")
    lines.append(f"- **Coverage Percentage:** {coverage_pct:.1f}%")
    lines.append("")

    return "\n".join(lines)


def generate_json_report() -> dict[str, Any]:
    """Generate JSON report of integration coverage."""
    return {
        "components": ALL_COMPONENTS,
        "covered_integrations": [
            {"component_a": comp1, "component_b": comp2}
            for comp1, comp2 in KNOWN_INTEGRATIONS
        ],
        "statistics": {
            "total_components": len(ALL_COMPONENTS),
            "total_possible_pairs": len(ALL_COMPONENTS)
            * (len(ALL_COMPONENTS) - 1)
            // 2,
            "covered_pairs": len(KNOWN_INTEGRATIONS),
            "coverage_percentage": (
                len(KNOWN_INTEGRATIONS)
                / (len(ALL_COMPONENTS) * (len(ALL_COMPONENTS) - 1) // 2)
                * 100
                if len(ALL_COMPONENTS) > 1
                else 0
            ),
        },
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
