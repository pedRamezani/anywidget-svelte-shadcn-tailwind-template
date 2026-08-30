# ipyfoo

A template for authoring [anywidget](http://anywidget.dev) with Svelte 5, Tailwind 4
and shadcn-svelte.

## Development

Development requires [`uv`](https://github.com/astral-sh/uv) and
[`pnpm`](https://pnpm.io/).

```sh
uv venv
uv pip install -e . --group dev
pnpm dev # start a development server
uv run jupyter lab notebooks/example.ipynb
```

## Renaming the widget

The package name appears in several places, and one of them is easy to miss:

- `pyproject.toml` — `name`, and the `py/ipyfoo` paths in the build config
- `py/ipyfoo/` — the package directory
- `vite.config.ts` — `outDir`
- `package.json` — `name`
- `.gitignore` — the ignored static directory
- **`src/App.svelte` and `src/app.css` — the `#ipyfoo-widget` id**, which must match
  in both files

## A widget is a guest

The template renders everything inside a single root element carrying an id, and
`app.css` scopes the theme to that id. This matters more than it looks.

A widget's CSS is injected into the host notebook's document, not into a sandbox. A
stock shadcn theme targets `*`, `body` and `html`, which is correct for an app that owns
the page and wrong here: it would restyle the entire notebook and every other widget
rendered beside yours. The same applies to anything you add — keep selectors under the
root id.

Two related habits worth keeping:

- Never put a `<style>` block inside the markup of a Svelte component. Svelte only
  scopes the one at the top level; a `<style>` in the template compiles to a literal DOM
  node whose selectors are global.
- The widget adopts the host's font rather than bundling one. Bundling a webfont inlines
  its subsets as base64 into your stylesheet — that is around 285KB for Inter, typically
  most of the file, downloaded again for every widget on the page.

## Releasing

```sh
uv build
uvx twine upload dist/*
```

`pnpm dev` and `pnpm build` write to the same directory, and the dev bundle is
unminified with an inline sourcemap — several times the size of a real build. Two
things stop that reaching a release: `vite.config.ts` sets `emptyOutDir`, so a
production build always starts clean, and the packaging hook runs `pnpm build` itself
for the sdist.

The build hook is registered for the **sdist target only**. `uv build` creates the sdist
from this tree, where `package.json` exists, and then builds the wheel from the unpacked
sdist, where it does not — a hook registered for both targets fails on the second step.
The sdist also flattens `py/ipyfoo/` to `ipyfoo/`, which is why
`[tool.hatch.build.targets.wheel]` lists both paths.
