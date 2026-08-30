"""Where the package name comes from, so renaming the widget does not break CI.

`pyproject.toml` is the authority: `[tool.hatch.build] packages = ["py/<name>"]`
gives the import name, which is what appears inside the wheel. Deliberately
avoids `tomllib`, which is 3.11+, so these scripts run under whatever
interpreter the workflow happens to have.
"""

from __future__ import annotations

import pathlib
import re
import sys


def _pyproject() -> str:
    return pathlib.Path("pyproject.toml").read_text()


def package_name() -> str:
    """The import name, e.g. `ipyfoo` for `packages = ["py/ipyfoo"]`."""
    match = re.search(r'packages\s*=\s*\[\s*"py/([A-Za-z0-9_]+)"', _pyproject())
    if not match:
        print("FAIL: could not find the package name in pyproject.toml", file=sys.stderr)
        sys.exit(1)
    return match.group(1)


def version() -> str:
    project = _pyproject().split("[project]", 1)[-1]
    match = re.search(r'^version\s*=\s*"([^"]+)"', project, re.MULTILINE)
    if not match:
        print("FAIL: could not find a version in pyproject.toml", file=sys.stderr)
        sys.exit(1)
    return match.group(1)
