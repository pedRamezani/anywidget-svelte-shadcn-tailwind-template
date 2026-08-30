"""Check that the built distribution is one worth publishing.

Every assertion here corresponds to something this template actually produced
before it was fixed. They are cheap; the failures they catch are not, because a
bad wheel on PyPI cannot be replaced, only superseded.
"""

from __future__ import annotations

import glob
import sys
import zipfile

from _project import package_name

# A production bundle is a few hundred KB; the dev one is several times that and
# carries an inline sourcemap.
MAX_JS_BYTES = 1_500_000


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> None:
    package = package_name()
    expected = {
        f"{package}/__init__.py",
        f"{package}/static/main.js",
        f"{package}/static/main.css",
    }

    wheels = glob.glob("dist/*.whl")
    sdists = glob.glob("dist/*.tar.gz")
    if len(wheels) != 1:
        fail(f"expected exactly one wheel, found {wheels}")
    if len(sdists) != 1:
        fail(f"expected exactly one sdist, found {sdists}")

    with zipfile.ZipFile(wheels[0]) as archive:
        names = {n for n in archive.namelist() if ".dist-info/" not in n}

        # The sdist flattens `py/<package>/` to `<package>/`, and the wheel is
        # built from the unpacked sdist. Get the paths wrong and the wheel
        # installs cleanly while containing nothing at all.
        missing = expected - names
        if missing:
            fail(f"wheel is missing {sorted(missing)}; it contains {sorted(names)}")

        js = archive.read(f"{package}/static/main.js")

        # `pnpm dev` and `pnpm build` share an output directory. A stale dev
        # bundle reaching a release is invisible until someone loads the widget.
        if b"sourceMappingURL" in js:
            fail("main.js carries a sourcemap -- this is a dev bundle, not a build")
        if len(js) > MAX_JS_BYTES:
            fail(f"main.js is {len(js):,} bytes, over the {MAX_JS_BYTES:,} limit")

        # A bundled webfont inlines its subsets as base64, typically adding a few
        # hundred KB to every widget on the page.
        css = archive.read(f"{package}/static/main.css")
        if b"base64" in css:
            fail("main.css contains base64 data -- a font or image is inlined")

    print(f"OK  {wheels[0]}")
    print(f"    package {package!r}, main.js {len(js):,} bytes, main.css {len(css):,} bytes")
    print(f"OK  {sdists[0]}")


if __name__ == "__main__":
    main()
