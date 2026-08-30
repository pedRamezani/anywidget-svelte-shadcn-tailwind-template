"""Exercise the installed package, on the oldest Python the project claims.

Not a substitute for a test suite. It checks the things that would make a
release useless: that the module imports, that the frontend assets made it into
the wheel, and that the widget's traits work.

Replace the body below as the widget grows.
"""

from __future__ import annotations

import importlib
import sys

from _project import package_name

package = importlib.import_module(package_name())
print(f"python {sys.version.split()[0]}, {package.__name__} from {package.__file__}")

assets = package.bundler_assets_dir
for name in ("main.js", "main.css"):
    path = assets / name
    assert path.exists(), f"{path} missing from the installed package"
    assert path.stat().st_size > 0, f"{path} is empty"

widget = package.Widget()
assert widget.value == 0, widget.value
widget.value = 7
assert widget.value == 7, widget.value

print("OK  all smoke checks passed")
