from __future__ import annotations

import inspect
from pathlib import Path

import mkdocs_gen_files
import vsaa
import vsdeband
import vsdehalo
import vsdeinterlace
import vsdenoise
import vsexprtools
import vskernels
import vsmasktools
import vspreview
import vspyplugin
import vsrgtools
import vsscale
import vssource
import vstools

# Modules to document.
MODULES = [
    vsaa,
    vsdeband,
    vsdehalo,
    vsdeinterlace,
    vsdenoise,
    vsexprtools,
    vskernels,
    vsmasktools,
    vspreview,
    vspyplugin,
    vsrgtools,
    vsscale,
    vssource,
    vstools,
]

# Excluded submodules.
EXCLUDE = [
    # These cause infinite recursion in griffe.
    "vsdeband.noise",
    "vsdenoise.nlm",
    "vsdenoise.prefilters",
]

nav = mkdocs_gen_files.Nav()

for module in MODULES:
    src = Path(inspect.getfile(module)).parent
    site_packages = src.parent
    for path in sorted(src.rglob("*.py")):
        module_path = path.relative_to(site_packages).with_suffix("")
        doc_path = path.relative_to(site_packages).with_suffix(".md")
        full_doc_path = Path("api", doc_path)
        parts = tuple(module_path.parts)

        if parts[-1] == "__init__":
            parts = parts[:-1]
            doc_path = doc_path.with_name("index.md")
            full_doc_path = full_doc_path.with_name("index.md")
        elif parts[-1].startswith("_") or ".".join(parts) in EXCLUDE:
            continue

        nav[parts] = doc_path.as_posix()

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)

            # TODO: figure out what to do with `__init__.py`'s. They're only
            # reexporting items from submodules so it becomes cluttered and
            # duplicated content on the site.
            if full_doc_path.name == "index.md":
                fd.write(f"---\ntitle: {ident}\n---\n\n{ident}")
            else:
                fd.write(f"---\ntitle: {ident}\n---\n\n::: {ident}")

        mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("api/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
