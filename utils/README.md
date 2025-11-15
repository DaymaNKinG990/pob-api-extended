# Utility Scripts

This directory contains utility scripts for working with the Path of Building API.

## Scripts

### `demo_pobapi.py`

Demo script that showcases all capabilities of the pobapi library.

**Usage:**
```bash
# Run and display output to console
python utils/demo_pobapi.py

# Save output to a specific file
python utils/demo_pobapi.py --output output/my_build_info.txt

# Auto-generate output file with timestamp
python utils/demo_pobapi.py --auto-output
```

**Features:**
- Displays all build information (stats, items, skills, trees, etc.)
- Modular output functions for easy customization
- Supports output to file or console

### `inspect_api.py`

Recursively inspects and displays the structure of the `PathOfBuildingAPI` object.

**Usage:**
```bash
# Display to console
python utils/inspect_api.py

# Save to specific file
python utils/inspect_api.py --output output/api_structure.txt

# Auto-generate output file with timestamp
python utils/inspect_api.py --auto-output
```

**Features:**
- Recursive inspection of API object structure
- Shows all methods, properties, and nested objects
- Useful for understanding the API structure

### `compare_stats.py`

Compares statistics extracted from Path of Building screenshots with API-extracted values.

**Usage:**
```bash
python utils/compare_stats.py
```

**Features:**
- Validates that all stats from screenshots are correctly extracted
- Shows matched, different, and missing statistics
- Helps verify API correctness

### `check_xml_stats.py`

Utility for checking XML statistics parsing.

**Usage:**
```bash
python utils/check_xml_stats.py
```

## Requirements

All scripts require:
- Python 3.12+
- `pobapi` package (installed in development mode)
- Import code file at `data/import_code.txt`

## Notes

- All scripts read import codes from `data/import_code.txt`
- Output files are saved to `output/` directory (created automatically)
- Scripts use relative paths, so they should be run from the project root
