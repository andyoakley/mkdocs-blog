# mkdocs-blog

Allows `mkdocs` to be used as a simple blog.

Features:

- Provides timestamps based on folder structure
- Enables jinja2 templating
- Generates a simple RSS feed for recent content

## Content layout

Assumes blog content is laid out in a standardized format with numeric years and months as follows:

`docs/<year>/<month>/page.md`

Within a month, file modification time is used to provide chronological ordering.

## Examples

- [Archive page](tests/test_data/docs/archive.md), listing posts in chronological order
- [Recently posted](tests/test_data/docs/recent.md), listed just the most recent posts
