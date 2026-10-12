# REA Gems

[![Auto-updated daily](https://img.shields.io/badge/auto--updated-daily-brightgreen)](https://github.com/sqwu/rea-gems/actions/workflows/update.yml)
[![Cases](https://img.shields.io/badge/cases-28-blue)](data/cases.json)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

**A curated, auto-updated gallery of excellent reverse-engineering cases built with [REA](https://github.com/morluto/rea).**

[REA](https://github.com/morluto/rea) ("reverse engineer anything") connects your
coding agent to tools for inspecting native binaries, JavaScript/Electron apps,
.NET assemblies and websites — and explains how features work, with evidence.
This repo tracks the best things people have **understood, rebuilt or
reconstructed** with it: official case studies, community projects, blog posts
and discussions, collected automatically from across the web.

> **28 cases** collected · **28 added in the last 30 days** · last refresh: **2026-10-12 (UTC)**

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


### Official case studies (rea.tools)

Curated deep dives published by the REA team.

| Case | Source | Category | Highlights | First seen |
|------|--------|----------|------------|------------|
| [The industrial revolution in reverse engineering](https://rea.tools/blog/touhou-reconstruction) | Official blog | Game reconstruction · Essay | — | 2026-10-12 |
| [DX-Ball's sound-pan calculation](https://rea.tools/showcase/dx-ball) | Official showcase | Native · Reconstruction | — | 2026-10-12 |
| [How an authenticator generates a login code](https://rea.tools/showcase/aegis) | Official showcase | Android · APK analysis | — | 2026-10-12 |
| [How Notion copies text and HTML](https://rea.tools/showcase/notion) | Official showcase | Electron · Feature tracing | — | 2026-10-12 |
| [How TH04 aims a ring of bullets](https://rea.tools/showcase/th04) | Official showcase | PC-98 DOS · Reconstruction | — | 2026-10-12 |
| [Solve a CTF flag checker](https://rea.tools/showcase/ctf) | Official showcase | CTF · Native analysis | — | 2026-10-12 |


### Community projects

Open-source repos, rebuilds and reimplementations made with REA.

| Case | Source | Category | Highlights | First seen |
|------|--------|----------|------------|------------|
| [ReverseEngineerAnything/REA](https://github.com/ReverseEngineerAnything/REA) | GitHub project | GitHub · decompilation, game-reversing, github-rea | ★ 49 | 2026-10-12 |
| [ringozzt/rea-research](https://github.com/ringozzt/rea-research) | GitHub project | GitHub | ★ 15 | 2026-10-12 |
| [czcdr/dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea) | GitHub project | GitHub · binary-analysis, cordis-plugin, deepseek-harness | ★ 1 | 2026-10-12 |
| [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) | GitHub project | GitHub · ai-agents, claude-code, claude-code-mod | ★ 1 | 2026-10-12 |
| [pablodiazjorge/rea-lab](https://github.com/pablodiazjorge/rea-lab) | GitHub project | GitHub · agentic-ai, ai-agents, binary-analysis | ★ 1 | 2026-10-12 |
| [laaielichter/reverseport](https://github.com/laaielichter/reverseport) | GitHub project | GitHub · ai-agents, binary-analysis, claude-code | — | 2026-10-12 |
| [miles990/rea-awesome](https://github.com/miles990/rea-awesome) | GitHub project | GitHub | — | 2026-10-12 |
| [Prabhendra/Reverse-engineer-anything](https://github.com/Prabhendra/Reverse-engineer-anything) | GitHub project | GitHub · agent-skills, ai-agents, binary-analysis | — | 2026-10-12 |
| [Rojios/Reverse-Engineer-Anything](https://github.com/Rojios/Reverse-Engineer-Anything) | GitHub project | GitHub | — | 2026-10-12 |
| [sqwu/rea-gems](https://github.com/sqwu/rea-gems) | GitHub project | GitHub · ai-agents, awesome-list, binary-analysis | — | 2026-10-12 |
| [tuunanet/rea-ski-or-die-reconstruction](https://github.com/tuunanet/rea-ski-or-die-reconstruction) | GitHub project | GitHub · dos-games, reverse-engineering, rust | — | 2026-10-12 |
| [inematds/rea-engenharia-reversa](https://github.com/inematds/rea-engenharia-reversa) | GitHub project | GitHub | — | 2026-10-12 |
| [ylwl1997/rea-run](https://github.com/ylwl1997/rea-run) | GitHub project | GitHub | — | 2026-10-12 |


### Posts & discussions

Hacker News threads, GitHub discussions and Reddit posts showing REA in action.

| Case | Source | Category | Highlights | First seen |
|------|--------|----------|------------|------------|
| [REA: Reverse Engineer Anything is now #1 trending repo on GitHub](https://news.ycombinator.com/item?id=50028294) | Hacker News | Hacker News | HN 2 pts · 💬 2 | 2026-10-12 |
| [Reverse Engineer Anything](https://news.ycombinator.com/item?id=50012930) | Hacker News | Hacker News | HN 4 pts | 2026-10-12 |
| [Ask HN: Have you checked REA(reverse engineer anything) GitHub repo?](https://news.ycombinator.com/item?id=50034003) | Hacker News | Hacker News | HN 2 pts · 💬 1 | 2026-10-12 |
| [Show and tell: Reducing token waste in REA workflows. What are you using?](https://github.com/morluto/rea/discussions/1958) | GitHub discussion | Discussion · Show and tell | 💬 9 | 2026-10-12 |
| [REA on Fedora-based Linux: setup notes, gotchas and my test queue](https://github.com/morluto/rea/discussions/1435) | GitHub discussion | Discussion · Show and tell | 💬 7 | 2026-10-12 |
| [Benchmarks: REA on Linux (Node 22, 24 and 26 startup, plus five local models)](https://github.com/morluto/rea/discussions/1998) | GitHub discussion | Discussion · Show and tell | 💬 1 | 2026-10-12 |
| [Showcase: outside-in "leak check" of a production Next.js + Stripe app on Windows](https://github.com/morluto/rea/discussions/1406) | GitHub discussion | Discussion · Show and tell | 💬 1 | 2026-10-12 |
| [Show HN: A MCP for Agents to reverse engineer binary code](https://news.ycombinator.com/item?id=48901763) | Hacker News | Hacker News | HN 3 pts | 2026-10-12 |
| [Project #000001: From REA to a working QuickBooks-style desktop app (Mac + Windows)](https://github.com/morluto/rea/discussions/2198) | GitHub discussion | Discussion · Show and tell | — | 2026-10-12 |


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
     {
       "url": "https://github.com/you/your-rea-project",
       "title": "What was reversed and how",
       "category": "Electron · Feature tracing",
       "description": "One or two sentences about the case.",
       "published_at": "2026-10-12"
     }
   ]
   ```
2. **Open an issue** titled `Case: <what it is>` with a link.

Manually curated entries are pinned above the automatic ones.

---

*Auto-generated by [scripts/fetch_cases.py](scripts/fetch_cases.py) — please
don't edit this README by hand. Data © respective authors; repository code
under [MIT](LICENSE).*
