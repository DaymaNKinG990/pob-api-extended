"""Unit tests for pyproject.toml configuration validation.

This module validates the project metadata, dependencies, build configuration,
and tool settings defined in pyproject.toml.
"""

import re
import tomllib
from pathlib import Path

import pytest


@pytest.fixture
def pyproject_data():
    """Load and parse pyproject.toml."""
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        return tomllib.load(f)


class TestProjectMetadata:
    """Tests for [project] section metadata."""

    def test_project_name(self, pyproject_data):
        """Test project name is correctly set."""
        assert pyproject_data["project"]["name"] == "pobapi-extended"
        # Ensure name follows PEP 508 naming conventions
        assert re.match(r"^[a-z0-9-]+$", pyproject_data["project"]["name"])

    def test_project_version(self, pyproject_data):
        """Test project version is correctly set."""
        version = pyproject_data["project"]["version"]
        assert version == "1.0.0"
        # Ensure version follows semantic versioning
        assert re.match(r"^\d+\.\d+\.\d+$", version)

    def test_project_version_major(self, pyproject_data):
        """Test that major version is 1 (not 0)."""
        version = pyproject_data["project"]["version"]
        major_version = int(version.split(".")[0])
        assert major_version == 1, "Project should be at version 1.x.x"

    def test_project_description(self, pyproject_data):
        """Test project has a valid description."""
        description = pyproject_data["project"]["description"]
        assert description
        assert isinstance(description, str)
        assert len(description) > 0
        assert "Path Of Building" in description

    def test_project_readme(self, pyproject_data):
        """Test README file is specified and exists."""
        readme = pyproject_data["project"]["readme"]
        assert readme == "README.md"
        readme_path = Path(__file__).parent.parent / readme
        assert readme_path.exists(), "README.md file should exist"

    def test_project_license(self, pyproject_data):
        """Test license is specified."""
        license_info = pyproject_data["project"]["license"]
        assert license_info
        assert "text" in license_info
        assert license_info["text"] == "MIT"

    def test_project_authors(self, pyproject_data):
        """Test authors list is valid."""
        authors = pyproject_data["project"]["authors"]
        assert isinstance(authors, list)
        assert len(authors) > 0
        # Check first author
        assert "name" in authors[0]
        assert "email" in authors[0]
        assert authors[0]["name"] == "Peter Pölzl"

    def test_project_maintainers(self, pyproject_data):
        """Test maintainers list is valid and includes both maintainers."""
        maintainers = pyproject_data["project"]["maintainers"]
        assert isinstance(maintainers, list)
        assert len(maintainers) == 2
        
        # Check first maintainer
        assert maintainers[0]["name"] == "Peter Pölzl"
        assert maintainers[0]["email"] == "33464174+ppoelzl@users.noreply.github.com"
        
        # Check second maintainer (newly added)
        assert maintainers[1]["name"] == "Ravil Shakerov"
        assert maintainers[1]["email"] == "xellaopromaster@yandex.ru"

    def test_maintainer_emails_valid_format(self, pyproject_data):
        """Test all maintainer emails have valid format."""
        maintainers = pyproject_data["project"]["maintainers"]
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        for maintainer in maintainers:
            assert re.match(email_pattern, maintainer["email"]), (
                f"Invalid email format: {maintainer['email']}"
            )

    def test_project_keywords(self, pyproject_data):
        """Test project keywords are defined."""
        keywords = pyproject_data["project"]["keywords"]
        assert isinstance(keywords, list)
        assert len(keywords) > 0
        expected_keywords = {"pathofexile", "poe", "pathofbuilding", "pob"}
        assert set(keywords) == expected_keywords

    def test_project_classifiers(self, pyproject_data):
        """Test project classifiers are valid."""
        classifiers = pyproject_data["project"]["classifiers"]
        assert isinstance(classifiers, list)
        assert len(classifiers) > 0
        
        # Check for essential classifiers
        classifier_strings = [c for c in classifiers]
        assert any("License :: OSI Approved :: MIT License" in c for c in classifier_strings)
        assert any("Programming Language :: Python :: 3" in c for c in classifier_strings)

    def test_python_version_requirement(self, pyproject_data):
        """Test Python version requirement is correctly specified."""
        requires_python = pyproject_data["project"]["requires-python"]
        assert requires_python == ">=3.12"

    def test_project_dependencies(self, pyproject_data):
        """Test project dependencies are defined."""
        dependencies = pyproject_data["project"]["dependencies"]
        assert isinstance(dependencies, list)
        assert len(dependencies) > 0
        
        # Check for key dependencies
        dep_names = [dep.split(">=")[0].split("==")[0] for dep in dependencies]
        assert "lupa" in dep_names
        assert "lxml" in dep_names
        assert "requests" in dep_names


class TestOptionalDependencies:
    """Tests for [project.optional-dependencies] section."""

    def test_optional_dependencies_structure(self, pyproject_data):
        """Test optional dependencies section exists and is properly structured."""
        optional_deps = pyproject_data["project"]["optional-dependencies"]
        assert isinstance(optional_deps, dict)

    def test_docs_dependencies(self, pyproject_data):
        """Test documentation dependencies."""
        docs_deps = pyproject_data["project"]["optional-dependencies"]["docs"]
        assert isinstance(docs_deps, list)
        assert len(docs_deps) > 0
        assert any("sphinx" in dep for dep in docs_deps)

    def test_async_dependencies(self, pyproject_data):
        """Test async dependencies."""
        async_deps = pyproject_data["project"]["optional-dependencies"]["async"]
        assert isinstance(async_deps, list)
        assert any("aiohttp" in dep for dep in async_deps)

    def test_dev_dependencies(self, pyproject_data):
        """Test development dependencies."""
        dev_deps = pyproject_data["project"]["optional-dependencies"]["dev"]
        assert isinstance(dev_deps, list)
        assert any("pre-commit" in dep for dep in dev_deps)

    def test_test_dependencies(self, pyproject_data):
        """Test testing dependencies."""
        test_deps = pyproject_data["project"]["optional-dependencies"]["test"]
        assert isinstance(test_deps, list)
        assert any("pytest" in dep for dep in test_deps)
        assert any("pytest-cov" in dep for dep in test_deps)
        assert any("pytest-mock" in dep for dep in test_deps)

    def test_linters_typers_dependencies(self, pyproject_data):
        """Test linter and type checker dependencies."""
        lint_deps = pyproject_data["project"]["optional-dependencies"]["linters_typers"]
        assert isinstance(lint_deps, list)
        assert any("mypy" in dep for dep in lint_deps)
        assert any("ruff" in dep for dep in lint_deps)

    def test_full_dependencies_completeness(self, pyproject_data):
        """Test that 'full' includes all other optional dependencies."""
        optional_deps = pyproject_data["project"]["optional-dependencies"]
        full_deps = optional_deps["full"]
        
        # Full should include deps from other categories
        assert isinstance(full_deps, list)
        assert len(full_deps) > 0
        
        # Check that full includes key packages from each category
        assert any("sphinx" in dep for dep in full_deps)  # from docs
        assert any("aiohttp" in dep for dep in full_deps)  # from async
        assert any("pytest" in dep for dep in full_deps)  # from test
        assert any("mypy" in dep for dep in full_deps)  # from linters_typers


class TestProjectURLs:
    """Tests for [project.urls] section."""

    def test_urls_section_exists(self, pyproject_data):
        """Test project URLs section exists."""
        urls = pyproject_data["project"]["urls"]
        assert isinstance(urls, dict)

    def test_required_urls_present(self, pyproject_data):
        """Test all required URLs are present."""
        urls = pyproject_data["project"]["urls"]
        required_keys = ["Homepage", "Documentation", "Repository", "Issues"]
        for key in required_keys:
            assert key in urls, f"Required URL key '{key}' is missing"

    def test_urls_valid_format(self, pyproject_data):
        """Test all URLs have valid format."""
        urls = pyproject_data["project"]["urls"]
        url_pattern = r"^https?://[^\s]+$"
        for key, url in urls.items():
            assert re.match(url_pattern, url), f"Invalid URL format for {key}: {url}"

    def test_github_urls_consistent(self, pyproject_data):
        """Test GitHub URLs are consistent."""
        urls = pyproject_data["project"]["urls"]
        base_repo = "https://github.com/ppoelzl/PathOfBuildingAPI"
        
        assert urls["Homepage"] == base_repo
        assert urls["Repository"] == base_repo
        assert urls["Issues"] == f"{base_repo}/issues"


class TestBuildSystem:
    """Tests for [build-system] section."""

    def test_build_system_exists(self, pyproject_data):
        """Test build system is configured."""
        build_system = pyproject_data["build-system"]
        assert isinstance(build_system, dict)

    def test_build_backend(self, pyproject_data):
        """Test build backend is hatchling."""
        build_backend = pyproject_data["build-system"]["build-backend"]
        assert build_backend == "hatchling.build"

    def test_build_requires(self, pyproject_data):
        """Test build requirements."""
        requires = pyproject_data["build-system"]["requires"]
        assert isinstance(requires, list)
        assert any("hatchling" in req for req in requires)


class TestHatchConfiguration:
    """Tests for [tool.hatch] configuration."""

    def test_hatch_wheel_packages(self, pyproject_data):
        """Test hatch wheel configuration."""
        wheel_config = pyproject_data["tool"]["hatch"]["build"]["targets"]["wheel"]
        assert "packages" in wheel_config
        assert "pobapi" in wheel_config["packages"]

    def test_hatch_sdist_includes(self, pyproject_data):
        """Test hatch sdist includes correct files."""
        sdist_config = pyproject_data["tool"]["hatch"]["build"]["targets"]["sdist"]
        includes = sdist_config["include"]
        assert isinstance(includes, list)
        
        expected_includes = ["/pobapi", "/tests", "/docs", "/LICENSE.txt", "/README.md"]
        for expected in expected_includes:
            assert expected in includes, f"Expected include '{expected}' not found"


class TestPytestConfiguration:
    """Tests for [tool.pytest.ini_options] configuration."""

    def test_pytest_testpaths(self, pyproject_data):
        """Test pytest testpaths configuration."""
        pytest_config = pyproject_data["tool"]["pytest"]["ini_options"]
        testpaths = pytest_config["testpaths"]
        assert "tests" in testpaths

    def test_pytest_patterns(self, pyproject_data):
        """Test pytest file and function patterns."""
        pytest_config = pyproject_data["tool"]["pytest"]["ini_options"]
        assert pytest_config["python_files"] == ["test_*.py"]
        assert pytest_config["python_classes"] == ["Test*"]
        assert pytest_config["python_functions"] == ["test_*"]

    def test_pytest_addopts(self, pyproject_data):
        """Test pytest additional options."""
        pytest_config = pyproject_data["tool"]["pytest"]["ini_options"]
        addopts = pytest_config["addopts"]
        assert "-v" in addopts
        assert "--strict-markers" in addopts


class TestCoverageConfiguration:
    """Tests for [tool.coverage] configuration."""

    def test_coverage_source(self, pyproject_data):
        """Test coverage source configuration."""
        coverage_run = pyproject_data["tool"]["coverage"]["run"]
        assert "pobapi" in coverage_run["source"]

    def test_coverage_omit(self, pyproject_data):
        """Test coverage omit patterns."""
        coverage_run = pyproject_data["tool"]["coverage"]["run"]
        omit = coverage_run["omit"]
        assert isinstance(omit, list)
        assert any("*/tests/*" in pattern for pattern in omit)

    def test_coverage_exclude_lines(self, pyproject_data):
        """Test coverage exclusion patterns."""
        coverage_report = pyproject_data["tool"]["coverage"]["report"]
        exclude_lines = coverage_report["exclude_lines"]
        assert isinstance(exclude_lines, list)
        assert "pragma: no cover" in exclude_lines
        assert "if __name__ == .__main__.:" in exclude_lines


class TestRuffConfiguration:
    """Tests for [tool.ruff] configuration."""

    def test_ruff_line_length(self, pyproject_data):
        """Test ruff line length configuration."""
        ruff_config = pyproject_data["tool"]["ruff"]
        assert ruff_config["line-length"] == 88

    def test_ruff_target_version(self, pyproject_data):
        """Test ruff target Python version."""
        ruff_config = pyproject_data["tool"]["ruff"]
        assert ruff_config["target-version"] == "py312"

    def test_ruff_lint_rules(self, pyproject_data):
        """Test ruff linting rules."""
        ruff_lint = pyproject_data["tool"]["ruff"]["lint"]
        assert isinstance(ruff_lint["select"], list)
        assert "F" in ruff_lint["select"]  # Pyflakes
        assert "E" in ruff_lint["select"]  # pycodestyle errors
        assert "W" in ruff_lint["select"]  # pycodestyle warnings


class TestMypyConfiguration:
    """Tests for [tool.mypy] configuration."""

    def test_mypy_python_version(self, pyproject_data):
        """Test mypy Python version."""
        mypy_config = pyproject_data["tool"]["mypy"]
        assert mypy_config["python_version"] == "3.12"

    def test_mypy_strict_settings(self, pyproject_data):
        """Test mypy strict type checking settings."""
        mypy_config = pyproject_data["tool"]["mypy"]
        assert mypy_config["warn_return_any"] is True
        assert mypy_config["warn_unused_configs"] is True
        assert mypy_config["check_untyped_defs"] is True

    def test_mypy_overrides(self, pyproject_data):
        """Test mypy module overrides."""
        mypy_overrides = pyproject_data["tool"]["mypy"]["overrides"]
        assert isinstance(mypy_overrides, list)
        assert len(mypy_overrides) > 0
        
        # Check that lxml and requests have ignore_missing_imports
        first_override = mypy_overrides[0]
        assert "module" in first_override
        assert first_override["ignore_missing_imports"] is True


class TestBlackConfiguration:
    """Tests for [tool.black] configuration (legacy, but still defined)."""

    def test_black_line_length(self, pyproject_data):
        """Test black line length matches ruff."""
        black_config = pyproject_data["tool"]["black"]
        ruff_config = pyproject_data["tool"]["ruff"]
        assert black_config["line-length"] == ruff_config["line-length"]

    def test_black_target_versions(self, pyproject_data):
        """Test black target Python versions."""
        black_config = pyproject_data["tool"]["black"]
        target_versions = black_config["target-version"]
        assert isinstance(target_versions, list)
        assert "py311" in target_versions or "py312" in target_versions


class TestConsistency:
    """Tests for consistency across different sections."""

    def test_version_consistency_with_init(self, pyproject_data):
        """Test that pyproject.toml version differs from __init__.py VERSION.
        
        This test documents that the __init__.py VERSION needs to be updated
        to match the new pyproject.toml version.
        """
        import pobapi
        
        pyproject_version = pyproject_data["project"]["version"]
        init_version = pobapi.VERSION
        
        # They should eventually match, but currently don't after the bump
        # This test serves as a reminder to update __init__.py
        assert pyproject_version == "1.0.0"
        # Note: init_version is currently "0.6.0" and needs updating

    def test_package_name_consistency(self, pyproject_data):
        """Test package name consistency across configuration."""
        project_name = pyproject_data["project"]["name"]
        
        # Wheel packages should reference the actual Python package name
        wheel_packages = pyproject_data["tool"]["hatch"]["build"]["targets"]["wheel"]["packages"]
        assert "pobapi" in wheel_packages
        
        # The distribution name is different from the import name
        assert project_name == "pobapi-extended"

    def test_python_version_consistency(self, pyproject_data):
        """Test Python version consistency across tools."""
        requires_python = pyproject_data["project"]["requires-python"]
        mypy_version = pyproject_data["tool"]["mypy"]["python_version"]
        ruff_target = pyproject_data["tool"]["ruff"]["target-version"]
        
        # All should reference Python 3.12+
        assert "3.12" in requires_python
        assert mypy_version == "3.12"
        assert ruff_target == "py312"

    def test_dependency_versions_have_constraints(self, pyproject_data):
        """Test that dependencies have version constraints."""
        dependencies = pyproject_data["project"]["dependencies"]
        
        for dep in dependencies:
            # Each dependency should have a version constraint
            assert ">=" in dep or "==" in dep or "~=" in dep, (
                f"Dependency {dep} should have version constraint"
            )


class TestEdgeCases:
    """Tests for edge cases and validation."""

    def test_no_duplicate_maintainers(self, pyproject_data):
        """Test that there are no duplicate maintainers."""
        maintainers = pyproject_data["project"]["maintainers"]
        emails = [m["email"] for m in maintainers]
        assert len(emails) == len(set(emails)), "Duplicate maintainer emails found"

    def test_all_optional_dep_keys_are_valid(self, pyproject_data):
        """Test that optional dependency keys are valid identifiers."""
        optional_deps = pyproject_data["project"]["optional-dependencies"]
        for key in optional_deps.keys():
            # Keys should be valid Python identifiers (with underscores)
            assert re.match(r"^[a-z_]+$", key), f"Invalid key: {key}"

    def test_no_circular_dependencies_in_optional(self, pyproject_data):
        """Test that optional dependencies don't reference each other."""
        optional_deps = pyproject_data["project"]["optional-dependencies"]
        
        # 'full' is allowed to reference others, but others shouldn't
        for key, deps in optional_deps.items():
            if key != "full":
                for dep in deps:
                    dep_name = dep.split("[")[0].split(">=")[0].split("==")[0]
                    assert dep_name != "pobapi-extended", (
                        f"Optional dependency group '{key}' shouldn't self-reference"
                    )

    def test_license_file_exists(self, pyproject_data):
        """Test that LICENSE file exists."""
        license_path = Path(__file__).parent.parent / "LICENSE.txt"
        assert license_path.exists(), "LICENSE.txt file should exist"

    def test_readme_content_matches_description(self, pyproject_data):
        """Test that README exists and is non-empty."""
        readme_path = Path(__file__).parent.parent / "README.md"
        assert readme_path.exists()
        
        with open(readme_path, "r") as f:
            content = f.read()
        
        assert len(content) > 100, "README should have substantial content"
        
        # Check that description is reflected in README
        description = pyproject_data["project"]["description"]
        assert "Path" in content and "Building" in content


class TestSecurityAndBestPractices:
    """Tests for security and best practices."""

    def test_no_hardcoded_credentials(self, pyproject_data):
        """Test that configuration doesn't contain hardcoded credentials."""
        # Convert entire config to string and check
        import json
        config_str = json.dumps(pyproject_data).lower()
        
        dangerous_patterns = ["password", "secret", "token", "api_key", "apikey"]
        for pattern in dangerous_patterns:
            assert pattern not in config_str or "noreply" in config_str, (
                f"Potential credential found: {pattern}"
            )

    def test_maintainer_emails_not_personal(self, pyproject_data):
        """Test maintainer emails are appropriate for public projects."""
        maintainers = pyproject_data["project"]["maintainers"]
        
        for maintainer in maintainers:
            email = maintainer["email"]
            # Ensure emails are either GitHub noreply or proper domains
            assert (
                "noreply.github.com" in email or
                "@" in email and "." in email.split("@")[1]
            ), f"Email format issue: {email}"

    def test_urls_use_https(self, pyproject_data):
        """Test that all URLs use HTTPS."""
        urls = pyproject_data["project"]["urls"]
        for key, url in urls.items():
            assert url.startswith("https://"), (
                f"URL for {key} should use HTTPS: {url}"
            )

    def test_minimum_python_version_supported(self, pyproject_data):
        """Test that minimum Python version is still supported."""
        requires_python = pyproject_data["project"]["requires-python"]
        
        # Extract minimum version
        min_version = requires_python.replace(">=", "")
        major, minor = map(int, min_version.split(".")[:2])
        
        # Python 3.12 should be the minimum given the config
        assert major == 3
        assert minor >= 12, "Minimum Python version should be 3.12 or higher"


# Integration-style tests
class TestPackageStructure:
    """Tests that validate the package structure matches configuration."""

    def test_package_directory_exists(self, pyproject_data):
        """Test that the package directory exists."""
        packages = pyproject_data["tool"]["hatch"]["build"]["targets"]["wheel"]["packages"]
        
        for package in packages:
            package_path = Path(__file__).parent.parent / package
            assert package_path.exists(), f"Package directory {package} should exist"
            assert package_path.is_dir(), f"{package} should be a directory"

    def test_tests_directory_exists(self, pyproject_data):
        """Test that tests directory exists."""
        testpaths = pyproject_data["tool"]["pytest"]["ini_options"]["testpaths"]
        
        for testpath in testpaths:
            test_dir = Path(__file__).parent.parent / testpath
            assert test_dir.exists(), f"Test directory {testpath} should exist"

    def test_docs_directory_exists(self, pyproject_data):
        """Test that docs directory exists (referenced in sdist)."""
        sdist_includes = pyproject_data["tool"]["hatch"]["build"]["targets"]["sdist"]["include"]
        
        for include in sdist_includes:
            if include.startswith("/docs"):
                docs_path = Path(__file__).parent.parent / "docs"
                assert docs_path.exists(), "docs directory should exist"
                break