"""Fail if the git tag disagrees with the version in pyproject.toml.

A tag that says one thing while the package says another produces a release
nobody can find, and PyPI will not let a version be uploaded twice.
"""

from __future__ import annotations

import sys

from _project import version

tag_version = sys.argv[1]
packaged = version()

if tag_version != packaged:
    print(f"FAIL: tag says {tag_version!r}, pyproject.toml says {packaged!r}")
    sys.exit(1)

print(f"OK  tag and pyproject.toml agree on {packaged}")
