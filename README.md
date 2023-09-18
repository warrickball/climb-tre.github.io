# climb-tre.github.io

This repo hosts the source from which the CLIMB-TRE website (https://climb-tre.github.io/) is generated.
The pages are built using the [Material theme](https://squidfunk.github.io/mkdocs-material/)
for [MkDocs](https://www.mkdocs.org/)
plus [MkDocstrings](https://mkdocstrings.github.io/) to generate Python APIs and
[MkDocs with PDF](https://github.com/orzih/mkdocs-with-pdf) to generate a PDF version.

## How to edit these pages

You'll need to install the Python packages `mkdocs-material`,
`mkdocstrings[python]` and `mkdocs-with-pdf` however you usually do.
Clone this repository, then build the docs with `mkdocs build`,
after which the site can be viewed in HTML at `site/index.html`
or PDF at `site/climb-tre.pdf`.

You can also run a local webserver to watch the pages as you
edit them by running `mkdocs serve` and navigating to the page
that's given in the output (usually `http://127.0.0.1:8000/`).

The documentation itself is written in [Markdown](https://www.markdownguide.org/)
files in the `docs` folder.  The site configuration is in
`mkdocs.yml` (in [YAML](https://yaml.org/) format) in the top-level directory.

The GitHub action will deploy changes made to the `main` branch.

Don't forget to add new pages to the `nav` section
of `mkdocs.yml`.
