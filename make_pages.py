#!/usr/bin/env python3
"""Generate HTML page for the OPTIMADE ontology workshop."""
from pathlib import Path
import shutil

from jinja2 import Environment, PackageLoader, select_autoescape
import markdown

# Out-folders
OUT_FOLDER = Path("build").resolve()
ASSETS_FOLDER = "assets"

# Absolute paths
pwd = Path(__file__).parent.resolve()
ASSETS_FOLDER_ABS = pwd / f"_{ASSETS_FOLDER}"

# In-folders
IN_FOLDER = Path("omdi2021").resolve()


def make_pages():
    """Create the rendered page."""
    # Create output folder, copy static assets files
    if OUT_FOLDER.exists():
        shutil.rmtree(OUT_FOLDER)
    OUT_FOLDER.mkdir()
    shutil.copytree(ASSETS_FOLDER_ABS, OUT_FOLDER / ASSETS_FOLDER)

    env = Environment(
        loader=PackageLoader("omdi2021"),
        autoescape=select_autoescape(["html", "xml"]),
    )

    all_data = {"title": "OMDI2021 Workshop"}

    # Get content
    with open(IN_FOLDER / "content.md") as handle:
        all_data["content"] = markdown.markdown(
            handle.read(),
            extensions=["tables"],
        )

    # Write main overview index
    rendered = env.get_template("default.html.j2").render(**all_data)
    outfile = OUT_FOLDER / "index.html"
    with open(outfile, "w") as handle:
        handle.write(rendered)


if __name__ == "__main__":
    make_pages()
