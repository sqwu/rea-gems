#!/usr/bin/env python3
"""Create a weekly digest issue on GitHub summarizing new REA cases.

Reads data/cases.json, finds cases first seen in the last 7 days,
and creates a GitHub issue via the REST API.

Usage:
  GITHUB_TOKEN=... python scripts/weekly_digest.py [--dry-run]
"""

import argparse
import json
import os
import sys
import urllib.request
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(ROOT, "data", "cases.json")
REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "sqwu/rea-gems")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""

SOURCE_LABELS = {
    "official-showcase": "Official showcase",
    "official-blog": "Official blog",
    "github": "GitHub project",
    "github-shared": "GitHub (from HN)",
    "discussion": "GitHub discussion",
    "hackernews": "Hacker News",
    "reddit": "Reddit",
    "manual": "Manually curated",
}


def gh_api(method, path, data=None):
    url = f"https://api.github.com/repos/{REPO_SLUG}/{path}"
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, method=method, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "rea-gems-digest/1.0",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read()) if resp.status != 204 else {}


def load_cases():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def build_digest(cases):
    cutoff = (date.today() - timedelta(days=7)).toordinal()
    week = [c for c in cases
            if c.get("first_seen")
            and date.fromisoformat(c["first_seen"]).toordinal() >= cutoff]

    today = date.today()
    monday = today - timedelta(days=today.weekday())
    week_str = f"{monday.isoformat()} – {today.isoformat()}"

    if not week:
        return week_str, None

    # Group by source type
    official = [c for c in week if "official" in c["source"]]
    community = [c for c in week if c["source"] in ("github", "github-shared", "manual")]
    posts = [c for c in week if c["source"] in ("hackernews", "discussion", "reddit")]

    parts = [
        f"## Weekly Digest — {week_str}\n",
        f"**{len(week)} new case{'s' if len(week)!=1 else ''}** added to "
        f"[REA Gems](https://github.com/{REPO_SLUG}) this week.\n",
    ]

    # Tag cloud
    tag_counts = {}
    for c in week:
        for t in (c.get("tags") or []):
            tag_counts[t] = tag_counts.get(t, 0) + 1
    if tag_counts:
        cloud = " ".join(f"`{t}`({n})" for t, n in
                         sorted(tag_counts.items(), key=lambda x: -x[1])[:12])
        parts.append(f"**Tags this week**: {cloud}\n")

    def render_group(title, items):
        if not items:
            return ""
        lines = [f"\n### {title}\n"]
        for c in items:
            hl = []
            if c.get("stars"):
                hl.append(f"★ {c['stars']:,}")
            if c.get("hn_points"):
                hl.append(f"HN {c['hn_points']}")
            if c.get("comments"):
                hl.append(f"💬 {c['comments']}")
            hl_str = f" ({' · '.join(hl)})" if hl else ""
            tags = " ".join(f"`{t}`" for t in (c.get("tags") or [])[:4])
            desc = (c.get("description") or "")[:120]
            lines.append(f"- [{c['title']}]({c['url']}){hl_str}\n  {desc}\n  {tags}\n")
        return "\n".join(lines)

    parts.append(render_group("Official case studies", official))
    parts.append(render_group("Community projects", community))
    parts.append(render_group("Posts & discussions", posts))

    parts.append(f"\n---\n[Browse all {len(cases)} cases](https://github.com/{REPO_SLUG})"
                 f" · [Live gallery](https://sqwu.github.io/rea-gems/)\n")
    return week_str, "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="print the issue body without creating it")
    args = parser.parse_args()

    if not TOKEN:
        print("ERROR: GITHUB_TOKEN not set", file=sys.stderr)
        return 1

    cases = load_cases()
    week_str, body = build_digest(cases)

    if body is None:
        print(f"No new cases for week {week_str} — skipping issue creation.")
        return 0

    title = f"Weekly Digest — {week_str}"

    if args.dry_run:
        print(f"=== TITLE: {title}\n")
        print(body)
        return 0

    # Check if an open issue with this title already exists
    existing = gh_api("GET", "issues?state=open&per_page=100")
    for issue in existing:
        if issue.get("title") == title:
            print(f"Issue already exists: #{issue['number']} — updating body.")
            gh_api("PATCH", f"issues/{issue['number']}", {"body": body})
            print(f"Updated #{issue['number']}")
            return 0

    # Create labels if they don't exist
    labels = []
    for label in ("weekly-digest",):
        try:
            gh_api("POST", "labels", {
                "name": label, "color": "a371f7",
                "description": "Auto-generated weekly case digest",
            })
        except Exception:
            pass  # label already exists
        labels.append(label)

    issue = gh_api("POST", "issues", {
        "title": title,
        "body": body,
        "labels": labels,
    })
    print(f"Created issue #{issue['number']}: {issue['html_url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
