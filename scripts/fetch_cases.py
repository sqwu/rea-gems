#!/usr/bin/env python3
"""Collect excellent REA reverse-engineering cases from across the web.

Sources (all best-effort, failures never break the run):
  1. rea.tools official showcase + blog   (HTML parsing)
  2. GitHub repo search mentioning REA    (REST search API)
  3. morluto/rea GitHub discussions       (REST API)
  4. Hacker News stories + shared repos   (Algolia API)
  5. Reddit posts                         (public JSON, often blocked)

Stdlib only. Outputs:
  - data/cases.json   structured single source of truth
  - README.md         auto-rendered gallery

Usage:
  python scripts/fetch_cases.py [--render-only]
"""

import argparse
import hashlib
import html as htmlmod
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
DATA_FILE = os.path.join(DATA_DIR, "cases.json")
MANUAL_FILE = os.path.join(DATA_DIR, "manual.json")
README_FILE = os.path.join(ROOT, "README.md")

REPO_SLUG = "sqwu/rea-gems"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
UA = f"rea-gems-fetcher/1.0 (+https://github.com/{REPO_SLUG})"

SHOWCASE_URL = "https://rea.tools/showcase/"
BLOG_URL = "https://rea.tools/blog/"
REA_REPO_URL = "https://github.com/morluto/rea"

ENTRY_RE = re.compile(r'<section class="guide-entry">(.*?)</section>', re.S)
GH_LINK_RE = re.compile(r'href="(https?://github\.com/[^"<>\s]+)"')
SHOWCASE_WORDS = re.compile(
    r"(?i)\b(built|build|reversed|reverse[- ]?engineer(ed|ing)?|cloned|"
    r"reimplemented|re-?created|reproduced|reconstruct(ed|ion)?|showcase|"
    r"case study|ported|cracked|decompiled|reimplementation)\b"
)
# Strong, unambiguous REA signals (used to reject lookalikes such as
# realtime-agents, react-tools, reason-tools, Reaper-Tools, ...)
STRONG_RE = re.compile(
    r"(?i)rea-agents|rea\.tools|morluto/rea|reverse\W*engineer\W*anything"
)
REA_TOKEN_RE = re.compile(r"(?i)(^|[^a-z0-9])rea([^a-z0-9]|$)")
RE_CTX_RE = re.compile(
    r"(?i)reverse\W*engineer|decompil|disassembl|binary\W+analysis|"
    r"rebuild|reimplement|reconstruct"
)
MIRROR_NAME_RE = re.compile(r"(?i)\b(mirror|backup|copy)\b|(^|[-_ /])rea([-_ /]|$)")
MIRROR_DESC_RE = re.compile(r"(?i)\b(mirror|backup|clone|copy|archival|archived)\b")
TOOL_TAGLINE_RE = re.compile(
    r"(?i)reverse\W*engineer\W*anything\W*with\W*agents"
)
OFFICIAL_SOURCES = ("official-showcase", "official-blog")


def is_rea_related(name, description, topics=""):
    """Decide whether a GitHub repo is an REA case (not a mirror/lookalike)."""
    name = name or ""
    description = description or ""
    blob = f"{name} {description} {topics or ''}".strip()
    if not blob:
        return False
    if MIRROR_DESC_RE.search(description):
        return False
    mirror_name = bool(MIRROR_NAME_RE.search(name))
    if STRONG_RE.search(blob):
        # Copies of the tool itself (same tagline, empty descriptions) are not cases
        if description and TOOL_TAGLINE_RE.search(description) and len(description) < 120:
            return False
        if not description and mirror_name:
            return False
        return True
    # Weaker signal: 'rea' as a standalone word in the name + RE context
    if REA_TOKEN_RE.search(name) and RE_CTX_RE.search(blob):
        return not (not description and mirror_name)
    return False


# --------------------------------------------------------------------------
# HTTP helpers
# --------------------------------------------------------------------------
def http_get(url, headers=None, timeout=30, retries=3):
    hdrs = {"User-Agent": UA, "Accept": "*/*"}
    if headers:
        hdrs.update(headers)
    if "api.github.com" in url and TOKEN:
        hdrs["Authorization"] = f"Bearer {TOKEN}"
        hdrs["Accept"] = "application/vnd.github+json"
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(min(2 ** attempt * 2, 10))
                continue
            raise
        except Exception as e:  # noqa: BLE001 - network is flaky by nature
            last_err = e
            time.sleep(min(2 ** attempt * 2, 10))
    raise last_err


def get_json(url, headers=None):
    return json.loads(http_get(url, headers=headers))


def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    s = htmlmod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def truncate(s, n):
    s = s or ""
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def canonical_url(u):
    p = urllib.parse.urlsplit(u.strip())
    path = p.path or "/"
    if path != "/":
        path = path.rstrip("/")
    query = "&".join(
        kv for kv in p.query.split("&")
        if kv and not kv.lower().startswith("utm_")
    )
    return urllib.parse.urlunsplit(
        (p.scheme.lower(), p.netloc.lower(), path, query, "")
    )


def make_item(url, title, source, category="", description="", stars=0,
              hn_points=0, comments=0, published_at=None):
    url = canonical_url(url)
    return {
        "id": hashlib.sha1(url.encode()).hexdigest()[:12],
        "url": url,
        "title": truncate(strip_tags(title), 140),
        "source": source,
        "category": category or "General",
        "description": truncate(strip_tags(description), 300),
        "stars": int(stars or 0),
        "hn_points": int(hn_points or 0),
        "comments": int(comments or 0),
        "published_at": published_at,
        "first_seen": None,
        "last_seen": date.today().isoformat(),
    }


# --------------------------------------------------------------------------
# Source 1: rea.tools official showcase + blog
# --------------------------------------------------------------------------
def parse_guide_entries(html, base_url, source):
    items = []
    for match in ENTRY_RE.finditer(html):
        block = match.group(1)
        m_title = re.search(r"<h2>(.*?)</h2>", block, re.S)
        m_link = re.search(r'<a class="text-link"[^>]*href="([^"]+)"', block)
        if not (m_title and m_link):
            continue
        title = strip_tags(m_title.group(1))
        url = urllib.parse.urljoin(base_url, m_link.group(1))

        category = ""
        m_cat = re.search(r'<p class="eyebrow">(.*?)</p>', block, re.S)
        if m_cat:
            category = strip_tags(re.sub(r"<br\s*/?>", " · ", m_cat.group(1)))

        description = ""
        m_desc = re.search(r"<p>(.*?)</p>", block, re.S)
        if m_desc:
            description = strip_tags(m_desc.group(1))

        published_at = None
        m_meta = re.search(r'<p class="page-meta">(.*?)</p>', block, re.S)
        if m_meta:
            m_date = re.search(r"(\d{1,2}\s+\w+\s+\d{4})", strip_tags(m_meta.group(1)))
            if m_date:
                try:
                    published_at = datetime.strptime(
                        m_date.group(1), "%d %B %Y"
                    ).date().isoformat()
                except ValueError:
                    pass

        items.append(make_item(url, title, source, category, description,
                               published_at=published_at))
    return items


def fetch_official():
    items = []
    html = http_get(SHOWCASE_URL).decode("utf-8", "replace")
    items.extend(parse_guide_entries(html, SHOWCASE_URL, "official-showcase"))
    html = http_get(BLOG_URL).decode("utf-8", "replace")
    items.extend(parse_guide_entries(html, BLOG_URL, "official-blog"))
    return items


# --------------------------------------------------------------------------
# Source 2: GitHub repos mentioning REA
# --------------------------------------------------------------------------
def fetch_github_repos():
    query = ('rea-agents OR "rea.tools" OR "morluto/rea" OR "reverse engineer anything" '
             "in:name,description,topics")
    items = {}
    for sort in ("stars", "updated"):
        url = ("https://api.github.com/search/repositories?q="
               + urllib.parse.quote(query)
               + f"&sort={sort}&per_page=50")
        try:
            data = get_json(url)
        except Exception as e:  # noqa: BLE001
            print(f"  [warn] github repo search failed: {e}", file=sys.stderr)
            continue
        for r in data.get("items", []):
            full_name = r.get("full_name", "")
            if not full_name or full_name.lower() == "morluto/rea" or r.get("fork"):
                continue
            desc = (r.get("description") or "").strip()
            # Bare-URL descriptions are copies of the tool, not cases
            if desc.startswith("http") and len(desc) < 60:
                continue
            topics = ", ".join((r.get("topics") or [])[:3])
            if not is_rea_related(full_name, desc,
                                  " ".join(r.get("topics") or [])):
                continue
            item = make_item(
                url=r["html_url"],
                title=full_name,
                source="github",
                category=f"GitHub · {topics}" if topics else "GitHub",
                description=r.get("description") or "",
                stars=r.get("stargazers_count") or 0,
                published_at=(r.get("created_at") or "")[:10] or None,
            )
            items[item["url"]] = item
    return list(items.values())


# --------------------------------------------------------------------------
# Source 3: morluto/rea discussions (show & tell style)
# --------------------------------------------------------------------------
def fetch_discussions():
    url = ("https://api.github.com/repos/morluto/rea/discussions"
           "?per_page=100&sort=updated")
    data = get_json(url)
    items = []
    if not isinstance(data, list):
        return items
    for d in data:
        title = d.get("title") or ""
        body = d.get("body") or ""
        text = f"{title} {body}"
        if not SHOWCASE_WORDS.search(text):
            continue
        cat = (d.get("category") or {}).get("name", "")
        # Only keep show-and-tell style categories; Q&A/ideas are not cases
        if "show" not in cat.lower():
            continue
        if "http" not in body and len(body) < 120:
            continue
        items.append(make_item(
            url=d["html_url"],
            title=title,
            source="discussion",
            category=f"Discussion · {cat}",
            description=truncate(body, 240),
            comments=d.get("comments") or 0,
            published_at=(d.get("created_at") or "")[:10] or None,
        ))
    return items


# --------------------------------------------------------------------------
# Source 4: Hacker News (Algolia)
# --------------------------------------------------------------------------
def fetch_hn():
    items = {}

    def algolia(query, tags, hits=50, extra=""):
        q = urllib.parse.quote(query)
        u = (f"https://hn.algolia.com/api/v1/search?query={q}"
             f"&tags={tags}&hitsPerPage={hits}{extra}")
        return get_json(u).get("hits", [])

    # Stories about REA — search only title/url and keep strong signals only
    seen_story_ids = set()
    seen_story_titles = set()
    for query in ("rea.tools", "rea-agents", '"reverse engineer anything"',
                  "morluto/rea"):
        try:
            hits = algolia(query, "story",
                           extra="&restrictSearchableAttributes=title,url")
        except Exception as e:  # noqa: BLE001
            print(f"  [warn] HN story search failed: {e}", file=sys.stderr)
            continue
        for h in hits:
            story_id = h.get("objectID")
            title = h.get("title") or ""
            story_url = h.get("url") or ""
            if not story_id or not title or story_id in seen_story_ids:
                continue
            if not STRONG_RE.search(f"{title} {story_url}"):
                continue
            seen_story_ids.add(story_id)
            title_key = re.sub(r"\W+", "", title.lower())
            if title_key in seen_story_titles:
                continue  # same story reposted; keep the first (highest-ranked) hit
            seen_story_titles.add(title_key)
            if urllib.parse.urlsplit(story_url).netloc == "rea.tools":
                continue  # product page itself; the official section covers it
            hn_url = f"https://news.ycombinator.com/item?id={story_id}"
            items[hn_url] = make_item(
                url=hn_url,
                title=title,
                source="hackernews",
                category="Hacker News",
                description=f"HN discussion: {story_url}" if story_url else "",
                hn_points=h.get("points") or 0,
                comments=h.get("num_comments") or 0,
                published_at=(h.get("created_at") or "")[:10] or None,
            )

    # Comments mentioning REA -> extract shared GitHub repos
    gh_cache = {}
    seen_comments = set()
    for query in ("rea.tools", "rea-agents"):
        try:
            hits = algolia(query, "comment", 100)
        except Exception as e:  # noqa: BLE001
            print(f"  [warn] HN comment search failed: {e}", file=sys.stderr)
            continue
        for h in hits:
            cid = h.get("objectID")
            if not cid or cid in seen_comments:
                continue
            seen_comments.add(cid)
            text = htmlmod.unescape(h.get("comment_text") or "")
            for m in GH_LINK_RE.finditer(text):
                link = m.group(1).split("?")[0].rstrip("/")
                parts = link[len("https://github.com/"):].split("/")
                if len(parts) < 2:
                    continue
                owner, repo = parts[0], parts[1]
                if owner.lower() == "morluto" or repo.startswith("#"):
                    continue
                if owner.lower() in ("topics", "features", "apps", "marketplace",
                                     "sponsors", "settings", "orgs"):
                    continue
                repo_url = f"https://github.com/{owner}/{repo}"
                if repo_url in items:
                    continue
                if repo_url not in gh_cache:
                    try:
                        r = get_json(f"https://api.github.com/repos/{owner}/{repo}")
                        gh_cache[repo_url] = (r.get("full_name") or f"{owner}/{repo}",
                                              r.get("description") or "",
                                              r.get("stargazers_count") or 0,
                                              (r.get("created_at") or "")[:10] or None)
                    except Exception:  # noqa: BLE001
                        gh_cache[repo_url] = (f"{owner}/{repo}", "", 0, None)
                full_name, desc, stars, created = gh_cache[repo_url]
                items[repo_url] = make_item(
                    url=repo_url,
                    title=full_name,
                    source="github-shared",
                    category="GitHub (shared on HN)",
                    description=desc or f"Shared by REA users on Hacker News",
                    stars=stars,
                    published_at=created,
                )
    return list(items.values())


# --------------------------------------------------------------------------
# Source 5: Reddit (best effort - public endpoint is often blocked)
# --------------------------------------------------------------------------
def fetch_reddit():
    url = ('https://www.reddit.com/search.json?q='
           + urllib.parse.quote('"rea.tools" OR "rea-agents"')
           + "&sort=new&limit=50")
    data = get_json(url, headers={"Accept": "application/json"})
    items = []
    for child in data.get("data", {}).get("children", []):
        p = child.get("data", {})
        if not p.get("title"):
            continue
        items.append(make_item(
            url="https://www.reddit.com" + p["permalink"],
            title=p["title"],
            source="reddit",
            category=f"r/{p.get('subreddit', 'unknown')}",
            description=truncate(p.get("selftext", ""), 200),
            comments=p.get("num_comments") or 0,
            published_at=datetime.fromtimestamp(
                p.get("created_utc", 0), tz=timezone.utc
            ).date().isoformat() if p.get("created_utc") else None,
        ))
    return items


# --------------------------------------------------------------------------
# Scoring, merge, render
# --------------------------------------------------------------------------
def compute_score(it):
    base = 40.0 if it["source"] in OFFICIAL_SOURCES else (
        15.0 if it["source"] == "manual" else 0.0
    )
    engagement = (
        3.0 * math.log1p(it.get("stars", 0))
        + 2.0 * math.log1p(it.get("hn_points", 0))
        + math.log1p(it.get("comments", 0))
    )
    freshness = 0.0
    pub = it.get("published_at")
    if pub:
        try:
            days = max(0, (date.today() - date.fromisoformat(pub)).days)
            freshness = 5.0 * max(0.0, 1 - days / 180)
        except ValueError:
            pass
    return round(base + engagement + freshness, 2)


def load_cases():
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
    except FileNotFoundError:
        pass
    except Exception as e:  # noqa: BLE001
        print(f"  [warn] could not read {DATA_FILE}: {e}", file=sys.stderr)
    return []


def load_manual():
    try:
        with open(MANUAL_FILE, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            out = []
            for it in data:
                it.setdefault("source", "manual")
                out.append(make_item(
                    url=it["url"], title=it["title"], source="manual",
                    category=it.get("category", "Manually curated"),
                    description=it.get("description", ""),
                    published_at=it.get("published_at"),
                ))
            return out
    except FileNotFoundError:
        pass
    except Exception as e:  # noqa: BLE001
        print(f"  [warn] could not read {MANUAL_FILE}: {e}", file=sys.stderr)
    return []


def merge_cases(existing, incoming):
    by_url = {canonical_url(it["url"]): it for it in existing}
    new_count = 0
    for it in incoming:
        key = canonical_url(it["url"])
        cur = by_url.get(key)
        if cur is None:
            it["first_seen"] = it["last_seen"]
            by_url[key] = it
            new_count += 1
        else:
            cur["last_seen"] = max(cur.get("last_seen", ""), it["last_seen"])
            for k in ("stars", "hn_points", "comments"):
                cur[k] = max(int(cur.get(k, 0) or 0), int(it.get(k, 0) or 0))
            is_official = cur["source"] in OFFICIAL_SOURCES
            if (not is_official
                    and len(it.get("description", "")) > len(cur.get("description", ""))):
                cur["description"] = it["description"]
    merged = list(by_url.values())
    for it in merged:
        it["score"] = compute_score(it)
    merged.sort(key=lambda x: (-x["score"], x["title"].lower()))
    return merged, new_count


def cell(s):
    return (s or "").replace("|", "\\|").strip()


def highlights(it):
    parts = []
    if it.get("stars"):
        parts.append(f"★ {it['stars']:,}")
    if it.get("hn_points"):
        parts.append(f"HN {it['hn_points']} pts")
    if it.get("comments"):
        parts.append(f"💬 {it['comments']}")
    return " · ".join(parts) or "—"


SOURCE_LABELS = {
    "official-showcase": "Official showcase",
    "official-blog": "Official blog",
    "github": "GitHub project",
    "github-shared": "GitHub (from HN)",
    "hackernews": "Hacker News",
    "discussion": "GitHub discussion",
    "reddit": "Reddit",
    "manual": "Manually curated",
}


def render_table(items, max_rows=60):
    lines = [
        "| Case | Source | Category | Highlights | First seen |",
        "|------|--------|----------|------------|------------|",
    ]
    for it in items[:max_rows]:
        lines.append(
            f"| [{cell(it['title'])}]({it['url']}) "
            f"| {cell(SOURCE_LABELS.get(it['source'], it['source']))} "
            f"| {cell(it['category'])} "
            f"| {highlights(it)} "
            f"| {it.get('first_seen') or '—'} |"
        )
    if len(items) > max_rows:
        lines.append(f"\n*… {len(items) - max_rows} more in [data/cases.json]"
                     f"](data/cases.json).*")
    return "\n".join(lines)


def render_readme(cases):
    official = [c for c in cases if c["source"] in OFFICIAL_SOURCES]
    projects = [c for c in cases if c["source"] in ("github", "github-shared", "manual")]
    posts = [c for c in cases
             if c["source"] in ("hackernews", "discussion", "reddit")]

    last_refresh = max((c.get("last_seen") or "") for c in cases) or date.today().isoformat()
    cutoff = (date.today().toordinal() - 30)
    new_recent = sum(
        1 for c in cases
        if c.get("first_seen") and date.fromisoformat(c["first_seen"]).toordinal() >= cutoff
    )

    sections = []
    if official:
        sections.append(("### Official case studies (rea.tools)\n\n"
                         "Curated deep dives published by the REA team.", official))
    if projects:
        sections.append(("### Community projects\n\n"
                         "Open-source repos, rebuilds and reimplementations made with REA.",
                         projects))
    if posts:
        sections.append(("### Posts & discussions\n\n"
                         "Hacker News threads, GitHub discussions and Reddit posts "
                         "showing REA in action.", posts))

    body_parts = [
        f"""# REA Gems

[![Auto-updated daily](https://img.shields.io/badge/auto--updated-daily-brightgreen)](https://github.com/{REPO_SLUG}/actions/workflows/update.yml)
[![Cases](https://img.shields.io/badge/cases-{len(cases)}-blue)](data/cases.json)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

**A curated, auto-updated gallery of excellent reverse-engineering cases built with [REA](https://github.com/morluto/rea).**

[REA](https://github.com/morluto/rea) ("reverse engineer anything") connects your
coding agent to tools for inspecting native binaries, JavaScript/Electron apps,
.NET assemblies and websites — and explains how features work, with evidence.
This repo tracks the best things people have **understood, rebuilt or
reconstructed** with it: official case studies, community projects, blog posts
and discussions, collected automatically from across the web.

> **{len(cases)} cases** collected · **{new_recent} added in the last 30 days** · last refresh: **{last_refresh} (UTC)**

<details>
<summary><strong>Disclaimer</strong></summary>

This repository is an unofficial community project and is not affiliated with
the REA team. All case links point to their original authors. Reverse
engineering may be restricted by local law, software licenses or terms of
service — always respect them. Content is indexed for research and educational
purposes.
</details>

## Table of contents

- [Official case studies](#official-case-studies-reatools)
- [Community projects](#community-projects)
- [Posts & discussions](#posts--discussions)
- [How cases are collected](#how-cases-are-collected)
- [Contributing](#contributing)
"""
    ]

    for heading, items in sections:
        body_parts.append(f"\n{heading}\n\n{render_table(items)}\n")

    body_parts.append(f"""
## How cases are collected

A scheduled GitHub Actions job ([update.yml](.github/workflows/update.yml))
runs daily and executes [scripts/fetch_cases.py](scripts/fetch_cases.py),
which searches:

| Source | What it looks for |
|--------|-------------------|
| [rea.tools/showcase](https://rea.tools/showcase/) | Official case studies |
| [rea.tools/blog](https://rea.tools/blog/) | Official deep dives |
| GitHub search | Repos mentioning `rea-agents`, `rea.tools`, `morluto/rea` |
| morluto/rea discussions | Show-and-tell style posts |
| [Hacker News](https://hn.algolia.com/api/v1) | Stories + repos shared in comments |
| Reddit | Posts mentioning REA (best effort) |

Results are deduplicated by URL, scored by engagement
(stars / HN points / comments) and freshness, then merged into
[data/cases.json](data/cases.json). README is regenerated from that file —
the JSON is the source of truth.

## Contributing

Found a great case (yours or someone else's)? Two ways to add it:

1. **Open a PR**: append an entry to [data/manual.json](data/manual.json):
   ```json
   [
     {{
       "url": "https://github.com/you/your-rea-project",
       "title": "What was reversed and how",
       "category": "Electron · Feature tracing",
       "description": "One or two sentences about the case.",
       "published_at": "2026-10-12"
     }}
   ]
   ```
2. **Open an issue** titled `Case: <what it is>` with a link.

Manually curated entries are pinned above the automatic ones.

---

*Auto-generated by [scripts/fetch_cases.py](scripts/fetch_cases.py) — please
don't edit this README by hand. Data © respective authors; repository code
under [MIT](LICENSE).*
""")

    return "\n".join(body_parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--render-only", action="store_true",
                        help="re-render README from existing data only")
    args = parser.parse_args()

    existing = load_cases()
    manual = load_manual()

    if args.render_only:
        cases, new_count = existing, 0
    else:
        incoming = []
        sources = [
            ("official", fetch_official),
            ("github-repos", fetch_github_repos),
            ("discussions", fetch_discussions),
            ("hackernews", fetch_hn),
            ("reddit", fetch_reddit),
        ]
        for name, fn in sources:
            try:
                got = fn()
                print(f"[{name}] {len(got)} item(s)")
                incoming.extend(got)
            except Exception as e:  # noqa: BLE001
                print(f"[{name}] FAILED: {e}", file=sys.stderr)

        incoming.extend(manual)
        if manual:
            print(f"[manual] {len(manual)} item(s)")

        print(f"total incoming: {len(incoming)}")
        cases, new_count = merge_cases(existing, incoming)
        print(f"merged: {len(cases)} cases ({new_count} new)")

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cases, f, indent=2, ensure_ascii=False)
        f.write("\n")

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(render_readme(cases))

    print(f"wrote {DATA_FILE} and {README_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
