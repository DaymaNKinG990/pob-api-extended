# Init Module Unit Test Cases

## Module: pobapi.__init__

### Overview
Unit test cases for the `__init__` module, which handles imports and exports of the pobapi package. The module conditionally imports optional dependencies (calculator, crafting, trade) and gracefully handles ImportError exceptions.

### Test Implementation Status
**Purpose:** Automated pytest tests
**Target Location:** `tests/unit/test_init.py`
**Note:** Some tests are already implemented. This specification serves as a comprehensive test plan and should be used to verify coverage and guide additional test implementation.

---

## Test Case: TC-INIT-001
**Title:** Import pobapi without optional dependencies

**Category:** Positive

**Purpose:** Automated pytest test

**Description:** Verify that pobapi imports successfully when optional dependencies (crafting, trade) are missing. The module should handle ImportError gracefully and exclude optional exports from `__all__`.

**Preconditions:**
- Python environment is set up
- pobapi package is installed
- Optional modules `pobapi.crafting` and `pobapi.trade` can be removed from `sys.modules`

**Setup:**
- Fixture: None required
- Mocks: Mock `builtins.__import__` to raise `ImportError` for `pobapi.crafting` and `pobapi.trade`
- Module manipulation: Remove `pobapi.crafting`, `pobapi.trade`, and `pobapi` from `sys.modules` before import

**Test Steps (pytest actions):**
1. Save original state of `sys.modules` for `pobapi.crafting`, `pobapi.trade`, and `pobapi`
2. Remove `pobapi.crafting` and `pobapi.trade` from `sys.modules` if present
3. Create a mock function for `builtins.__import__` that raises `ImportError` for `pobapi.crafting` and `pobapi.trade`
4. Use `unittest.mock.patch` to replace `builtins.__import__` with the mock
5. Remove `pobapi` from `sys.modules` to force reload
6. Import `pobapi` module
7. Restore original modules in `finally` block

**Expected Assertions:**
- `assert pobapi is not None`
- `assert hasattr(pobapi, "PathOfBuildingAPI")`
- `assert hasattr(pobapi, "__all__")`
- `assert "ItemCraftingAPI" not in pobapi.__all__`
- `assert "TradeAPI" not in pobapi.__all__`
- `assert not hasattr(pobapi, "ItemCraftingAPI")`
- `assert not hasattr(pobapi, "TradeAPI")`

**Code Skeleton:**
```python
def test_import_without_optional_dependencies():
    import builtins
    modules_to_remove = ["pobapi.crafting", "pobapi.trade", "pobapi"]
    original_modules = {name: sys.modules.get(name) for name in modules_to_remove}

    try:
        # Remove optional modules
        for module_name in ["pobapi.crafting", "pobapi.trade"]:
            if module_name in sys.modules:
                del sys.modules[module_name]

        # Mock __import__ to raise ImportError
        original_import = builtins.__import__
        def mock_import(name, *args, **kwargs):
            if name in ["pobapi.crafting", "pobapi.trade"]:
                raise ImportError(f"No module named '{name}'")
            return original_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=mock_import):
            if "pobapi" in sys.modules:
                del sys.modules["pobapi"]
            import pobapi
            # Assertions here
    finally:
        # Restore modules
        for module_name, original in original_modules.items():
            if original is None:
                sys.modules.pop(module_name, None)
            else:
                sys.modules[module_name] = original
```

---

## Test Case: TC-INIT-002
**Title:** Verify __all__ contains expected exports

**Category:** Positive

**Purpose:** Automated pytest test

**Description:** Verify that `__all__` attribute exists, is a list, contains all core exports, and all listed exports are accessible from the module.

**Preconditions:**
- pobapi package is installed
- pobapi can be imported normally

**Setup:**
- Fixture: None required
- Mocks: None required

**Test Steps (pytest actions):**
1. Import `pobapi` module
2. Check that `__all__` attribute exists
3. Verify `__all__` is a list
4. Check for presence of core exports in `__all__`
5. Iterate through all names in `__all__` and verify accessibility

**Expected Assertions:**
- `assert hasattr(pobapi, "__all__")`
- `assert isinstance(pobapi.__all__, list)`
- `assert "PathOfBuildingAPI" in pobapi.__all__`
- `assert "BuildFactory" in pobapi.__all__`
- `assert "StatsBuilder" in pobapi.__all__`
- `assert "ConfigBuilder" in pobapi.__all__`
- For each `name` in `pobapi.__all__`: `assert hasattr(pobapi, name) or name in dir(pobapi)`

**Code Skeleton:**
```python
def test_all_exports():
    import pobapi
    assert hasattr(pobapi, "__all__")
    assert isinstance(pobapi.__all__, list)

    core_exports = ["PathOfBuildingAPI", "BuildFactory", "StatsBuilder", "ConfigBuilder"]
    for export in core_exports:
        assert export in pobapi.__all__

    for name in pobapi.__all__:
        assert hasattr(pobapi, name) or name in dir(pobapi)
```

---

## Test Case: TC-INIT-003
**Title:** Import error handling for calculator module

**Category:** Positive

**Purpose:** Automated pytest test

**Description:** Verify that pobapi handles ImportError gracefully when the calculator module is missing. The module should still import successfully and maintain core functionality.

**Preconditions:**
- pobapi package is installed
- `pobapi.calculator` can be removed from `sys.modules`

**Setup:**
- Fixture: None required
- Mocks: Use `patch.dict` to set `pobapi.calculator` to `None` in `sys.modules`
- Module manipulation: Remove `pobapi.calculator` and `pobapi` from `sys.modules` before import

**Test Steps (pytest actions):**
1. Remove `pobapi.calculator` from `sys.modules` if present
2. Remove `pobapi` from `sys.modules` if present
3. Use `patch.dict(sys.modules, {"pobapi.calculator": None})` to mock missing calculator
4. Import `pobapi` module
5. Verify module state

**Expected Assertions:**
- `assert pobapi is not None`
- `assert "pobapi" in sys.modules`
- `assert hasattr(pobapi, "__all__")`
- `assert len(pobapi.__all__) > 0`
- `assert getattr(pobapi, pobapi.__all__[0]) is not None`

**Code Skeleton:**
```python
def test_import_error_handling_calculator():
    if "pobapi.calculator" in sys.modules:
        del sys.modules["pobapi.calculator"]
    if "pobapi" in sys.modules:
        del sys.modules["pobapi"]

    with patch.dict(sys.modules, {"pobapi.calculator": None}):
        import pobapi
        # Assertions here
```

---

## Test Case: TC-INIT-004
**Title:** Import error handling for crafting module

**Category:** Positive

**Purpose:** Automated pytest test

**Description:** Verify that pobapi handles ImportError gracefully when the crafting module is missing. Crafting-related exports should not appear in `__all__` or as module attributes.

**Preconditions:**
- pobapi package is installed
- `pobapi.crafting` can be removed from `sys.modules`

**Setup:**
- Fixture: None required
- Mocks: Mock `builtins.__import__` to raise `ImportError` for `pobapi.crafting`
- Module manipulation: Remove `pobapi.crafting` and `pobapi` from `sys.modules` before import

**Test Steps (pytest actions):**
1. Save original state of `pobapi.crafting` and `pobapi` modules
2. Remove `pobapi.crafting` from `sys.modules` if present
3. Create a mock function for `builtins.__import__` that raises `ImportError` for `pobapi.crafting`
4. Use `unittest.mock.patch` to replace `builtins.__import__` with the mock
5. Remove `pobapi` from `sys.modules` to force reload
6. Import `pobapi` module
7. Restore original modules in `finally` block

**Expected Assertions:**
- `assert "pobapi" in sys.modules`
- `pobapi_module = sys.modules["pobapi"]`
- `assert pobapi_module is not None`
- `assert getattr(pobapi_module, "crafting", None) is None`
- `assert "ItemCraftingAPI" not in pobapi_module.__all__`
- `assert "ItemModifier" not in pobapi_module.__all__`
- `assert "CraftingModifier" not in pobapi_module.__all__`
- `assert "CraftingResult" not in pobapi_module.__all__`
- `assert "ModifierTier" not in pobapi_module.__all__`
- `assert not hasattr(pobapi_module, "ItemCraftingAPI")`

**Code Skeleton:**
```python
def test_import_error_handling_crafting():
    original_crafting = sys.modules.get("pobapi.crafting")
    original_pobapi = sys.modules.get("pobapi")

    try:
        if "pobapi.crafting" in sys.modules:
            del sys.modules["pobapi.crafting"]

        original_import = __import__
        def mock_import(name, *args, **kwargs):
            if name == "pobapi.crafting":
                raise ImportError("No module named 'pobapi.crafting'")
            return original_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=mock_import):
            if "pobapi" in sys.modules:
                del sys.modules["pobapi"]
            import pobapi
            # Assertions here
    finally:
        # Restore modules
        if original_crafting is not None:
            sys.modules["pobapi.crafting"] = original_crafting
        if original_pobapi is not None:
            sys.modules["pobapi"] = original_pobapi
```

---

## Test Case: TC-INIT-005
**Title:** Import error handling for trade module with reload

**Category:** Positive

**Purpose:** Automated pytest test

**Description:** Verify that pobapi handles ImportError gracefully when the trade module is missing, even when using `importlib.reload()`. Trade-related exports should not appear in `__all__` or as module attributes.

**Preconditions:**
- pobapi package is installed
- pobapi is already imported (present in `sys.modules`)
- `pobapi.trade` can be removed from `sys.modules`

**Setup:**
- Fixture: None required
- Mocks: Mock `builtins.__import__` to raise `ImportError` for `pobapi.trade`
- Module manipulation: Remove `pobapi.trade` from `sys.modules`, use `importlib.reload()` on `pobapi`

**Test Steps (pytest actions):**
1. Save original state of `pobapi.trade` and `pobapi` modules
2. Remove `pobapi.trade` from `sys.modules` if present
3. Create a mock function for `builtins.__import__` that raises `ImportError` for `pobapi.trade`
4. Use `unittest.mock.patch` to replace `builtins.__import__` with the mock
5. If `pobapi` is in `sys.modules`, use `importlib.reload(sys.modules["pobapi"])`
6. Otherwise, import `pobapi`
7. Remove `pobapi.trade` from `sys.modules` if it was re-added during reload
8. Remove trade-related attributes from `pobapi` module if they exist
9. Restore original modules in `finally` block

**Expected Assertions:**
- `assert "pobapi" in sys.modules`
- `pobapi_module = sys.modules["pobapi"]`
- `assert pobapi_module is not None`
- `assert getattr(pobapi_module, "trade", None) is None`
- `assert "TradeAPI" not in pobapi_module.__all__`
- `assert "TradeFilter" not in pobapi_module.__all__`
- `assert "TradeQuery" not in pobapi_module.__all__`
- `assert "TradeResult" not in pobapi_module.__all__`
- `assert "PriceRange" not in pobapi_module.__all__`
- `assert "FilterType" not in pobapi_module.__all__`
- `assert not hasattr(pobapi_module, "TradeAPI")`

**Code Skeleton:**
```python
def test_import_error_handling_trade():
    import importlib
    original_trade = sys.modules.get("pobapi.trade")
    original_pobapi = sys.modules.get("pobapi")

    try:
        if "pobapi.trade" in sys.modules:
            del sys.modules["pobapi.trade"]

        original_import = __import__
        def mock_import(name, *args, **kwargs):
            if name == "pobapi.trade":
                raise ImportError("No module named 'pobapi.trade'")
            return original_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=mock_import):
            if "pobapi" in sys.modules:
                importlib.reload(sys.modules["pobapi"])
            else:
                import pobapi

            if "pobapi.trade" in sys.modules:
                del sys.modules["pobapi.trade"]

            pobapi_module = sys.modules["pobapi"]
            # Remove trade attributes if they exist
            trade_attributes = ["TradeAPI", "TradeFilter", "TradeQuery", "TradeResult", "PriceRange", "FilterType"]
            for attr in trade_attributes:
                if hasattr(pobapi_module, attr):
                    delattr(pobapi_module, attr)
            # Assertions here
    finally:
        # Restore modules
        if original_trade is not None:
            sys.modules["pobapi.trade"] = original_trade
        if original_pobapi is not None:
            sys.modules["pobapi"] = original_pobapi
```

---

## Test Case: TC-INIT-006
**Title:** All exports are accessible from module

**Category:** Positive

**Purpose:** Automated pytest test

**Description:** Verify that every name listed in `__all__` is actually accessible from the pobapi module using `hasattr()` or `dir()`.

**Preconditions:**
- pobapi package is installed
- pobapi can be imported normally

**Setup:**
- Fixture: None required
- Mocks: None required

**Test Steps (pytest actions):**
1. Import `pobapi` module
2. Iterate through each name in `pobapi.__all__`
3. For each name, verify it is accessible

**Expected Assertions:**
- For each `name` in `pobapi.__all__`: `assert hasattr(pobapi, name) or name in dir(pobapi)`

**Code Skeleton:**
```python
def test_all_exports_accessible():
    import pobapi
    for name in pobapi.__all__:
        assert hasattr(pobapi, name) or name in dir(pobapi), \
            f"Export '{name}' declared in __all__ but not accessible"
```

---

## Test Case: TC-INIT-007
**Title:** Core exports are always present

**Category:** Positive

**Purpose:** Automated pytest test

**Description:** Verify that core exports (PathOfBuildingAPI, BuildFactory, StatsBuilder, ConfigBuilder) are always present in `__all__`, regardless of optional dependencies.

**Preconditions:**
- pobapi package is installed
- pobapi can be imported normally

**Setup:**
- Fixture: None required
- Mocks: None required

**Test Steps (pytest actions):**
1. Import `pobapi` module
2. Check for presence of each core export in `__all__`

**Expected Assertions:**
- `assert "PathOfBuildingAPI" in pobapi.__all__`
- `assert "BuildFactory" in pobapi.__all__`
- `assert "StatsBuilder" in pobapi.__all__`
- `assert "ConfigBuilder" in pobapi.__all__`

**Code Skeleton:**
```python
def test_core_exports_always_present():
    import pobapi
    core_exports = ["PathOfBuildingAPI", "BuildFactory", "StatsBuilder", "ConfigBuilder"]
    for export in core_exports:
        assert export in pobapi.__all__, f"Core export '{export}' missing from __all__"
```

---

## Test Case: TC-INIT-008
**Title:** Optional exports are conditionally present

**Category:** Positive

**Purpose:** Automated pytest test

**Description:** Verify that optional exports (from calculator, crafting, trade modules) are present in `__all__` when their respective modules are available, and absent when modules are missing.

**Preconditions:**
- pobapi package is installed
- Ability to test both scenarios: with and without optional modules

**Setup:**
- Fixture: None required
- Mocks: May require mocking `builtins.__import__` to simulate missing modules
- Module manipulation: May require removing modules from `sys.modules`

**Test Steps (pytest actions):**
1. Test scenario 1: Import pobapi with all optional modules available
2. Verify optional exports are present in `__all__`
3. Test scenario 2: Remove optional modules and reimport
4. Verify optional exports are absent from `__all__`

**Expected Assertions:**
- When modules available: `assert "CalculationEngine" in pobapi.__all__` (if calculator available)
- When modules available: `assert "ItemCraftingAPI" in pobapi.__all__` (if crafting available)
- When modules available: `assert "TradeAPI" in pobapi.__all__` (if trade available)
- When modules missing: `assert "CalculationEngine" not in pobapi.__all__` (if calculator missing)
- When modules missing: `assert "ItemCraftingAPI" not in pobapi.__all__` (if crafting missing)
- When modules missing: `assert "TradeAPI" not in pobapi.__all__` (if trade missing)

**Code Skeleton:**
```python
def test_optional_exports_conditionally_present():
    import pobapi

    # Test with available modules (if they exist)
    calculator_exports = ["CalculationEngine", "DamageCalculator", "ModifierSystem"]
    crafting_exports = ["ItemCraftingAPI", "ItemModifier", "CraftingModifier"]
    trade_exports = ["TradeAPI", "TradeFilter", "TradeQuery"]

    # Check which optional modules are available
    has_calculator = "CalculationEngine" in pobapi.__all__
    has_crafting = "ItemCraftingAPI" in pobapi.__all__
    has_trade = "TradeAPI" in pobapi.__all__

    # Verify exports match module availability
    if has_calculator:
        for export in calculator_exports:
            assert export in pobapi.__all__ and export in dir(pobapi)
    if has_crafting:
        for export in crafting_exports:
            assert export in pobapi.__all__ and export in dir(pobapi)
    if has_trade:
        for export in trade_exports:
            assert export in pobapi.__all__ and export in dir(pobapi)
```

---

## Test Case: TC-INIT-009
**Title:** Module reload preserves state correctly

**Category:** Positive

**Purpose:** Automated pytest test

**Description:** Verify that when `importlib.reload()` is called on the pobapi module, the module state is preserved correctly, including `__all__` and all exports.

**Preconditions:**
- pobapi package is installed
- pobapi is already imported

**Setup:**
- Fixture: None required
- Mocks: None required

**Test Steps (pytest actions):**
1. Import `pobapi` module
2. Store a copy of `pobapi.__all__` before reload
3. Use `importlib.reload(sys.modules["pobapi"])` to reload the module
4. Verify module state after reload

**Expected Assertions:**
- `assert "pobapi" in sys.modules`
- `pobapi_module = sys.modules["pobapi"]`
- `assert pobapi_module is not None`
- `assert hasattr(pobapi_module, "__all__")`
- `assert isinstance(pobapi_module.__all__, list)`
- `assert len(pobapi_module.__all__) > 0`
- Verify that core exports are still present

**Code Skeleton:**
```python
def test_module_reload_preserves_state():
    import importlib
    import pobapi

    original_all = pobapi.__all__.copy()
    importlib.reload(sys.modules["pobapi"])

    pobapi_module = sys.modules["pobapi"]
    assert pobapi_module is not None
    assert hasattr(pobapi_module, "__all__")
    assert isinstance(pobapi_module.__all__, list)
    assert len(pobapi_module.__all__) > 0

    # Verify core exports are still present
    core_exports = ["PathOfBuildingAPI", "BuildFactory", "StatsBuilder", "ConfigBuilder"]
    for export in core_exports:
        assert export in pobapi_module.__all__
```

---

## Test Case: TC-INIT-010
**Title:** Import with all optional modules available

**Category:** Positive

**Purpose:** Automated pytest test

**Description:** Verify that when all optional modules (calculator, crafting, trade) are available, all their respective exports are present in `__all__` and accessible from the module.

**Preconditions:**
- pobapi package is installed
- All optional modules (calculator, crafting, trade) are available in the environment

**Setup:**
- Fixture: None required
- Mocks: None required (assumes modules are actually available)

**Test Steps (pytest actions):**
1. Import `pobapi` module
2. Check for presence of optional exports from calculator module
3. Check for presence of optional exports from crafting module
4. Check for presence of optional exports from trade module
5. Verify all optional exports are accessible

**Expected Assertions:**
- Calculator exports (if available): `assert "CalculationEngine" in pobapi.__all__`
- Calculator exports (if available): `assert "DamageCalculator" in pobapi.__all__`
- Calculator exports (if available): `assert "ModifierSystem" in pobapi.__all__`
- Crafting exports (if available): `assert "ItemCraftingAPI" in pobapi.__all__`
- Crafting exports (if available): `assert "ItemModifier" in pobapi.__all__`
- Trade exports (if available): `assert "TradeAPI" in pobapi.__all__`
- Trade exports (if available): `assert "TradeFilter" in pobapi.__all__`
- For each optional export in `__all__`: `assert hasattr(pobapi, name) or name in dir(pobapi)`

**Code Skeleton:**
```python
def test_import_with_all_optional_modules():
    import pobapi

    # Define expected optional exports
    calculator_exports = [
        "CalculationEngine", "DamageCalculator", "DefenseCalculator",
        "ModifierSystem", "ResourceCalculator", "SkillStatsCalculator",
        "PenetrationCalculator", "ItemModifierParser", "PassiveTreeParser",
        "SkillModifierParser", "ConfigModifierParser", "ConditionEvaluator",
        "UniqueItemParser", "GameDataLoader", "PassiveNode", "SkillGem", "UniqueItem"
    ]
    crafting_exports = [
        "ItemCraftingAPI", "ItemModifier", "CraftingModifier",
        "CraftingResult", "ModifierTier"
    ]
    trade_exports = [
        "TradeAPI", "TradeFilter", "TradeQuery", "TradeResult",
        "PriceRange", "FilterType"
    ]

    # Check which optional modules are available
    all_optional = calculator_exports + crafting_exports + trade_exports

    for export in all_optional:
        if export in pobapi.__all__:
            assert hasattr(pobapi, export) or export in dir(pobapi), \
                f"Optional export '{export}' in __all__ but not accessible"
```

---

## Implementation Notes

### Test File Location
All automated tests should be implemented in: `tests/unit/test_init.py`

### Common Patterns
1. **Module State Management:** Always save and restore original module state in `try/finally` blocks
2. **Import Mocking:** Use `unittest.mock.patch` with `side_effect` to mock `builtins.__import__`
3. **Module Reload:** Use `importlib.reload()` when testing reload scenarios
4. **Cleanup:** Remove modules from `sys.modules` and delete attributes when testing missing modules

### Fixtures to Consider
- Consider creating a fixture for module cleanup/restoration
- Consider creating a fixture for mocking `__import__` with specific module exclusions

### Dependencies
- `pytest`
- `unittest.mock` (for patching)
- `importlib` (for reload functionality)
- `sys` (for module manipulation)
