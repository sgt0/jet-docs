# jet-docs

Unofficial API docs for [JET][] packages.

## Build

Python v3.12 and [uv][] v0.4.5 may be used to build the project. Older versions
will likely work fine but they aren't explicitly supported.

```bash
$ git clone https://github.com/sgt0/jet-docs.git
$ cd jet-docs

# Install dependencies.
$ uv sync

# Build the site.
$ uv run mkdocs build
```

[JET]: https://github.com/Jaded-Encoding-Thaumaturgy
[uv]: https://docs.astral.sh/uv/
