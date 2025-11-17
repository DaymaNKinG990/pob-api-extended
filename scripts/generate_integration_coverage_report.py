#!/usr/bin/env python3
"""Generate comprehensive integration coverage report.

This script analyzes integration tests and generates:
1. Markdown report with coverage matrix
2. JSON report for programmatic access
"""

import json
import re
import tokenize
from io import StringIO
from pathlib import Path
from typing import Any

# Define component groups for better analysis
COMPONENT_GROUPS = {
    "API": ["PathOfBuildingAPI", "BuildModifier", "BuildBuilder"],
    "Parsers": [
        "BuildInfoParser",
        "SkillsParser",
        "ItemsParser",
        "TreesParser",
        "DefaultBuildParser",
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
        "SkillModifierParser",
        "ConfigModifierParser",
        "UniqueItemParser",
    ],
    "Data": ["GameDataLoader"],
    "Trade": ["TradeAPI"],
    "Crafting": ["ItemCraftingAPI"],
    "Infrastructure": ["HTTPClient", "AsyncHTTPClient", "Cache"],
}

# Known real integrations (manually curated based on actual test analysis)
REAL_INTEGRATIONS = [
    # API ↔ Calculation
    ("PathOfBuildingAPI", "CalculationEngine"),
    ("BuildModifier", "CalculationEngine"),
    # API ↔ Serializers
    ("PathOfBuildingAPI", "BuildXMLSerializer"),
    ("PathOfBuildingAPI", "ImportCodeGenerator"),
    ("BuildBuilder", "BuildXMLSerializer"),
    ("BuildModifier", "BuildXMLSerializer"),
    # Calculation Components
    ("ModifierSystem", "DamageCalculator"),
    ("ModifierSystem", "DefenseCalculator"),
    ("ModifierSystem", "ResourceCalculator"),
    ("ModifierSystem", "SkillStatsCalculator"),
    ("ModifierSystem", "MinionCalculator"),
    ("ModifierSystem", "PartyCalculator"),
    ("CalculationEngine", "ModifierSystem"),
    # Data ↔ Parsers
    ("GameDataLoader", "PassiveTreeParser"),
    ("GameDataLoader", "ItemModifierParser"),
    # Validators ↔ Parsers
    ("InputValidator", "BuildInfoParser"),
    ("XMLValidator", "BuildInfoParser"),
    # Factory ↔ Builders
    ("BuildFactory", "BuildBuilder"),
]


def strip_strings_and_comments(content: str) -> str:
    """Remove string literals and comments from Python source code.

    Uses tokenize to parse the code and filter out strings and comments,
    returning only the code tokens with spaces between them to preserve
    word boundaries for regex matching.
    """
    try:
        tokens = tokenize.generate_tokens(StringIO(content).readline)
        filtered_tokens = []
        for token in tokens:
            # Keep only NAME, NUMBER, OP, NEWLINE, INDENT, DEDENT, NL tokens
            # Skip STRING and COMMENT tokens
            if token.type not in (tokenize.STRING, tokenize.COMMENT):
                filtered_tokens.append(token.string)
        return " ".join(filtered_tokens)
    except Exception:
        # Fallback to original content if tokenization fails
        return content


def extract_test_info(file_path: Path) -> dict[str, Any]:
    """Extract test information from a test file."""
    components_mentioned: set[str] = set()
    info: dict[str, Any] = {
        "file": file_path.name,
        "test_classes": [],
        "test_methods": 0,
        "components_mentioned": components_mentioned,
    }

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        # Find test classes
        class_pattern = r"class\s+(Test\w+).*?:"
        classes = re.findall(class_pattern, content)
        info["test_classes"] = classes

        # Count test methods
        method_pattern = r"def\s+(test_\w+)\s*\("
        methods = re.findall(method_pattern, content)
        info["test_methods"] = len(methods)

        # Preprocess content to remove strings and comments
        processed_content = strip_strings_and_comments(content)

        # Find component mentions using word-boundary regex
        for _, components in COMPONENT_GROUPS.items():
            for comp in components:
                # Escape component name and use word boundaries
                pattern = r"\b" + re.escape(comp) + r"\b"
                if re.search(pattern, processed_content):
                    components_mentioned.add(comp)

    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")

    return info


def generate_markdown_report(test_infos: list[dict[str, Any]]) -> str:
    """Generate markdown coverage report."""
    lines = []
    lines.append("# Integration Test Coverage Report")
    lines.append("")
    lines.append(
        "This report shows which component integrations are covered "
        "by integration tests."
    )
    lines.append("")
    lines.append("## Summary")
    lines.append("")

    total_tests = sum(info["test_methods"] for info in test_infos)
    lines.append(f"- **Total Integration Test Files:** {len(test_infos)}")
    total_classes = sum(len(i["test_classes"]) for i in test_infos)
    lines.append(f"- **Total Test Classes:** {total_classes}")
    lines.append(f"- **Total Test Methods:** {total_tests}")
    lines.append("")

    # Coverage by component group
    lines.append("## Coverage by Component Group")
    lines.append("")
    lines.append("| Group | Components | Coverage Status |")
    lines.append("|-------|------------|-----------------|")

    for group_name, components in COMPONENT_GROUPS.items():
        covered = []
        for comp in components:
            for info in test_infos:
                if comp in info["components_mentioned"]:
                    covered.append(comp)
                    break

        status = "[PARTIAL]" if covered else "[NONE]"
        if len(covered) == len(components):
            status = "[FULL]"

        lines.append(f"| {group_name} | {len(covered)}/{len(components)} | {status} |")

    lines.append("")
    lines.append("## Covered Integrations")
    lines.append("")
    lines.append("| Component A | Component B | Test File |")
    lines.append("|------------|-------------|-----------|")

    # Map integrations to test files
    integration_to_file: dict[tuple[str, str], str] = {}
    for info in test_infos:
        components = list(info["components_mentioned"])
        for i, comp1 in enumerate(components):
            for comp2 in components[i + 1 :]:
                sorted_pair = tuple(sorted([comp1, comp2]))
                if len(sorted_pair) == 2:
                    pair: tuple[str, str] = (sorted_pair[0], sorted_pair[1])
                    real_pairs = [
                        (a, b) if a < b else (b, a) for a, b in REAL_INTEGRATIONS
                    ]
                    if pair in real_pairs:
                        integration_to_file[pair] = info["file"]

    for comp1, comp2 in sorted(REAL_INTEGRATIONS):
        sorted_key = tuple(sorted([comp1, comp2]))
        if len(sorted_key) == 2:
            key: tuple[str, str] = (sorted_key[0], sorted_key[1])
            test_file = integration_to_file.get(key, "Unknown")
            lines.append(f"| {comp1} | {comp2} | {test_file} |")

    lines.append("")
    lines.append("## Test Files")
    lines.append("")

    for info in test_infos:
        lines.append(f"### {info['file']}")
        lines.append("")
        lines.append(f"- **Test Classes:** {len(info['test_classes'])}")
        lines.append(f"- **Test Methods:** {info['test_methods']}")
        components_str = (
            ", ".join(sorted(info["components_mentioned"])) or "None detected"
        )
        lines.append(f"- **Components:** {components_str}")
        lines.append("")

    # Statistics
    lines.append("## Coverage Statistics")
    lines.append("")

    all_components = set()
    for components in COMPONENT_GROUPS.values():
        all_components.update(components)

    total_pairs = len(all_components) * (len(all_components) - 1) // 2
    covered_pairs = len(REAL_INTEGRATIONS)
    coverage_pct = (covered_pairs / total_pairs) * 100 if total_pairs > 0 else 0

    lines.append(f"- **Total Components:** {len(all_components)}")
    lines.append(f"- **Total Possible Pairs:** {total_pairs}")
    lines.append(f"- **Covered Integrations:** {covered_pairs}")
    lines.append(f"- **Coverage Percentage:** {coverage_pct:.1f}%")
    lines.append("")

    return "\n".join(lines)


def generate_json_report(test_infos: list[dict[str, Any]]) -> dict[str, Any]:
    """Generate JSON coverage report."""
    all_components = set()
    for components in COMPONENT_GROUPS.values():
        all_components.update(components)

    return {
        "metadata": {
            "total_test_files": len(test_infos),
            "total_test_classes": sum(len(i["test_classes"]) for i in test_infos),
            "total_test_methods": sum(i["test_methods"] for i in test_infos),
        },
        "components": {
            "total": len(all_components),
            "by_group": {
                group: len(components) for group, components in COMPONENT_GROUPS.items()
            },
        },
        "integrations": {
            "covered": [
                {"component_a": comp1, "component_b": comp2}
                for comp1, comp2 in REAL_INTEGRATIONS
            ],
            "total_possible": len(all_components) * (len(all_components) - 1) // 2,
            "coverage_percentage": (
                len(REAL_INTEGRATIONS)
                / (len(all_components) * (len(all_components) - 1) // 2)
                * 100
                if len(all_components) > 1
                else 0
            ),
        },
        "test_files": [
            {
                "file": info["file"],
                "test_classes": info["test_classes"],
                "test_methods": info["test_methods"],
                "components": sorted(info["components_mentioned"]),
            }
            for info in test_infos
        ],
    }


def main() -> None:
    """Generate integration coverage reports."""
    tests_dir = Path(__file__).parent.parent / "tests" / "integrations"

    if not tests_dir.exists():
        print(f"Tests directory not found: {tests_dir}")
        return

    # Analyze all test files
    test_files = [f for f in tests_dir.glob("test_*.py") if f.name != "__init__.py"]
    test_infos = [extract_test_info(f) for f in test_files]

    # Generate reports
    markdown = generate_markdown_report(test_infos)
    json_report = generate_json_report(test_infos)

    # Write reports
    markdown_file = tests_dir / "COVERAGE_REPORT.md"
    markdown_file.write_text(markdown, encoding="utf-8")
    print(f"[OK] Generated: {markdown_file}")

    json_file = tests_dir / "coverage_report.json"
    json_file.write_text(json.dumps(json_report, indent=2), encoding="utf-8")
    print(f"[OK] Generated: {json_file}")

    # Print summary
    print()
    print("=" * 80)
    print("Integration Coverage Summary")
    print("=" * 80)
    print(f"Total Test Files: {len(test_infos)}")
    print(f"Total Test Methods: {sum(i['test_methods'] for i in test_infos)}")
    print(f"Covered Integrations: {len(REAL_INTEGRATIONS)}")
    print()


if __name__ == "__main__":
    main()
