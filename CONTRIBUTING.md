# Contributing

Thanks for your interest in improving **REA Gems** — a curated gallery of
excellent reverse-engineering cases built with
[REA](https://github.com/morluto/rea).

## Add a case (recommended)

Open a pull request that appends an entry to
[`data/manual.json`](data/manual.json). Manually curated entries are ranked
above automatically discovered ones.

```json
[
  {
    "url": "https://github.com/you/your-rea-project",
    "title": "Short, descriptive case title",
    "category": "Electron · Feature tracing",
    "description": "One or two sentences: what was reversed, how REA helped, what was rebuilt.",
    "published_at": "2026-10-12"
  }
]
```

Rules:

- Only submit content you have the right to share, or that is already public.
- One link per entry; prefer the most permanent URL (repo root, blog post).
- No paywalled or private content.

Alternatively, [open an issue](https://github.com/sqwu/rea-gems/issues/new)
titled `Case: <short description>` with the link — it will be picked up
manually.

## Improve the scraper

`scripts/fetch_cases.py` is stdlib-only Python and runs on a daily schedule
via [`.github/workflows/update.yml`](.github/workflows/update.yml). To add a
new source:

1. Write a `fetch_<source>()` function returning a list of items
   (see `make_item()` for the schema).
2. Register it in the `sources` list in `main()`.
3. Run it locally: `python scripts/fetch_cases.py` — it is safe to re-run;
   entries are deduplicated by URL and merged.

Please keep dependencies to the standard library so the workflow stays fast
and supply-chain-safe.
