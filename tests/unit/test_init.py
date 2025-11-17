"""Tests for pobapi.__init__ module."""

import sys
from unittest.mock import patch


def test_import_without_optional_dependencies() -> None:
    """Test that __init__ handles missing optional dependencies gracefully."""
    import builtins

    # Save original state for the modules we are going to manipulate
    modules_to_remove = ["pobapi.crafting", "pobapi.trade", "pobapi"]
    original_modules = {name: sys.modules.get(name) for name in modules_to_remove}
    original_pobapi_all = None
    if "pobapi" in sys.modules:
        pobapi_module = sys.modules["pobapi"]
        original_pobapi_all = (
            getattr(pobapi_module, "__all__", None).copy()
            if hasattr(pobapi_module, "__all__")
            else None
        )

    try:
        # Remove optional modules from sys.modules to simulate their absence
        for module_name in ["pobapi.crafting", "pobapi.trade"]:
            if module_name in sys.modules:
                del sys.modules[module_name]

        # Mock __import__ to raise ImportError for optional modules
        original_import = builtins.__import__

        def mock_import(name, *args, **kwargs):
            if name in ["pobapi.crafting", "pobapi.trade"]:
                error_msg = f"No module named '{name}'"
                raise ImportError(error_msg)
            return original_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=mock_import):
            # Remove pobapi from sys.modules to force reload
            if "pobapi" in sys.modules:
                del sys.modules["pobapi"]

            # Import pobapi to trigger ImportError handling
            import pobapi

            # Verify that pobapi module loaded successfully
            assert pobapi is not None

            # Verify that core functionality is still available
            assert hasattr(pobapi, "PathOfBuildingAPI")
            assert hasattr(pobapi, "__all__")

            # Verify that optional modules are NOT in __all__ when missing
            assert "ItemCraftingAPI" not in pobapi.__all__
            assert "TradeAPI" not in pobapi.__all__

            # Verify that optional modules are NOT available as attributes
            assert not hasattr(pobapi, "ItemCraftingAPI")
            assert not hasattr(pobapi, "TradeAPI")
    finally:
        # Restore only the modules we deliberately manipulated
        for module_name, original in original_modules.items():
            if original is None:
                sys.modules.pop(module_name, None)
            else:
                sys.modules[module_name] = original

        # Restore pobapi's __all__ if it was modified
        if "pobapi" in sys.modules and original_pobapi_all is not None:
            sys.modules["pobapi"].__all__ = original_pobapi_all


def test_all_exports() -> None:
    """Test that __all__ contains expected exports."""
    import pobapi

    # Check that __all__ exists
    assert hasattr(pobapi, "__all__")
    assert isinstance(pobapi.__all__, list)

    # Check for core exports
    core_exports = [
        "PathOfBuildingAPI",
        "BuildFactory",
        "StatsBuilder",
        "ConfigBuilder",
    ]
    # Verify all core exports are in __all__
    for export in core_exports:
        assert export in pobapi.__all__, f"Core export '{export}' missing from __all__"

    # Verify every name in __all__ is actually accessible
    for name in pobapi.__all__:
        assert hasattr(pobapi, name) or name in dir(
            pobapi
        ), f"Export '{name}' declared in __all__ but not accessible on module"


def test_import_error_handling_calculator() -> None:
    """Test that ImportError in calculator import is handled."""
    # Mock ImportError when importing calculator
    with patch.dict("sys.modules", {"pobapi.calculator": None}):
        # Reload module to trigger ImportError
        import importlib

        if "pobapi" in sys.modules:
            importlib.reload(sys.modules["pobapi"])
        else:
            import pobapi  # noqa: F401

        # Should not raise exception
        assert True


def test_import_error_handling_crafting() -> None:
    """Test that ImportError in crafting import is handled."""
    # Mock ImportError when importing crafting
    original_import = __import__

    def mock_import(name, *args, **kwargs):
        if name == "pobapi.crafting":
            raise ImportError("No module named 'pobapi.crafting'")
        return original_import(name, *args, **kwargs)

    with patch("builtins.__import__", side_effect=mock_import):
        # Reload module to trigger ImportError
        import importlib

        if "pobapi" in sys.modules:
            importlib.reload(sys.modules["pobapi"])
        else:
            import pobapi  # noqa: F401

        # Should not raise exception
        assert True


def test_import_error_handling_trade() -> None:
    """Test that ImportError in trade import is handled."""
    # Mock ImportError when importing trade
    original_import = __import__

    def mock_import(name, *args, **kwargs):
        if name == "pobapi.trade":
            raise ImportError("No module named 'pobapi.trade'")
        return original_import(name, *args, **kwargs)

    with patch("builtins.__import__", side_effect=mock_import):
        # Reload module to trigger ImportError
        import importlib

        if "pobapi" in sys.modules:
            importlib.reload(sys.modules["pobapi"])
        else:
            import pobapi  # noqa: F401

        # Should not raise exception
        assert True
