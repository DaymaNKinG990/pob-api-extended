# Scripts

This directory contains utility scripts for the project.

## Integration Coverage Analysis

### `generate_integration_coverage_report.py`

Generates comprehensive integration test coverage reports.

**Usage:**
```bash
python scripts/generate_integration_coverage_report.py
```

**Output:**
- `tests/integrations/COVERAGE_REPORT.md` - Markdown report with coverage matrix
- `tests/integrations/coverage_report.json` - JSON report for programmatic access

**What it does:**
- Analyzes all integration test files
- Identifies which components are tested together
- Generates coverage statistics
- Creates visual reports

### `analyze_integration_coverage.py`

Analyzes integration tests to find component pairs.

**Usage:**
```bash
python scripts/analyze_integration_coverage.py
```

**Output:**
- Console report with component pairs
- Coverage statistics
- Missing integrations list

## Understanding Integration Coverage

Integration coverage is different from code coverage:

- **Code Coverage** (`pytest-cov`): Measures which lines of code are executed
- **Integration Coverage**: Measures which component pairs are tested together

### Example

If a test uses both `PathOfBuildingAPI` and `CalculationEngine`, it covers:
- Integration: `PathOfBuildingAPI` ↔ `CalculationEngine`

This doesn't mean 100% code coverage, but it means the integration between these components is tested.

## Coverage Metrics

The reports show:
- **Component Pairs**: Which pairs of components are tested together
- **Coverage Percentage**: Percentage of possible component pairs covered
- **Missing Integrations**: Component pairs that need testing

## Updating Coverage

When adding new integration tests:
1. Run the coverage analysis script
2. Check the generated reports
3. Update `tests/integrations/INTEGRATION_COVERAGE.md` if needed
