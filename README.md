# REA Gems

<p align="center">
  <img src="assets/logo.svg" width="120" alt="REA Gems logo" />
</p>

[![Auto-updated daily](https://img.shields.io/badge/auto--updated-daily-brightgreen)](https://github.com/sqwu/rea-gems/actions/workflows/update.yml)
[![Cases](https://img.shields.io/badge/cases-93-blue)](data/cases.json)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

**A curated, auto-updated gallery of excellent reverse-engineering cases built with [REA](https://github.com/morluto/rea).**

[REA](https://github.com/morluto/rea) ("reverse engineer anything") connects your
coding agent to tools for inspecting native binaries, JavaScript/Electron apps,
.NET assemblies and websites — and explains how features work, with evidence.
This repo tracks the best things people have **understood, rebuilt or
reconstructed** with it: official case studies, community projects, blog posts
and discussions, collected automatically from across the web.

<p align="center">
  <img src="assets/og-cover.svg" width="640" alt="REA Gems — cover banner" />
</p>

> **93 cases** collected · **93 added in the last 30 days** · last refresh: **2026-10-16 (UTC)**

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

> **Live gallery**: [sqwu.github.io/rea-gems](https://sqwu.github.io/rea-gems/) — interactive visual gallery with tag filtering and search.


### Official case studies (rea.tools)

Curated deep dives published by the REA team.

| Case | Source | Tags | Highlights | First seen |
|------|--------|------|------------|------------|
| [Does reverse engineering need a bigger model?](https://rea.tools/blog/reverse-engineering-models) | Official blog | `reconstruction` `official` | — | 2026-10-13 |
| [The industrial revolution in reverse engineering](https://rea.tools/blog/touhou-reconstruction) | Official blog | `reconstruction` `official` | — | 2026-10-12 |
| [DX-Ball's sound-pan calculation](https://rea.tools/showcase/dx-ball) | Official showcase | `native` `windows` `reconstruction` `binary-analysis` `official` | — | 2026-10-12 |
| [How an authenticator generates a login code](https://rea.tools/showcase/aegis) | Official showcase | `android` `feature-tracing` `official` | — | 2026-10-12 |
| [How Notion copies text and HTML](https://rea.tools/showcase/notion) | Official showcase | `electron` `web` `feature-tracing` `official` | — | 2026-10-12 |
| [How TH04 aims a ring of bullets](https://rea.tools/showcase/th04) | Official showcase | `dos` `reconstruction` `official` | — | 2026-10-12 |
| [Solve a CTF flag checker](https://rea.tools/showcase/ctf) | Official showcase | `native` `ctf` `official` | — | 2026-10-12 |


### Community projects

Open-source repos, rebuilds and reimplementations made with REA.

| Case | Source | Tags | Highlights | First seen |
|------|--------|------|------------|------------|
| [ringozzt/rea-research](https://github.com/ringozzt/rea-research) | GitHub project | `community` | ★ 55 | 2026-10-12 |
| [ShadowSwaps/REA-Reconstruction-Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion) | GitHub project | `reconstruction` `community` | ★ 48 | 2026-10-15 |
| [ReverseEngineerAnything/REA](https://github.com/ReverseEngineerAnything/REA) | GitHub project | `native` `windows` `decompilation` `community` | ★ 49 | 2026-10-12 |
| [rea-githu/REA](https://github.com/rea-githu/REA) | GitHub project | `native` `windows` `decompilation` `community` | ★ 37 | 2026-10-14 |
| [Fanqi89/dsh-rea](https://github.com/Fanqi89/dsh-rea) | GitHub project | `community` | ★ 25 | 2026-10-13 |
| [valorisa/Reverse-Engineer-Anything](https://github.com/valorisa/Reverse-Engineer-Anything) | GitHub project | `decompilation` `community` | ★ 25 | 2026-10-13 |
| [czcdr/dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea) | GitHub project | `android` `electron` `decompilation` `binary-analysis` `community` | ★ 12 | 2026-10-12 |
| [pablodiazjorge/rea-lab](https://github.com/pablodiazjorge/rea-lab) | GitHub project | `windows` `decompilation` `binary-analysis` `community` | ★ 3 | 2026-10-12 |
| [dav1dngy/era-agent](https://github.com/dav1dngy/era-agent) | GitHub project | `community` | ★ 2 | 2026-10-14 |
| [sheilacraig/dsh-rea-mcp](https://github.com/sheilacraig/dsh-rea-mcp) | GitHub project | `community` | ★ 2 | 2026-10-13 |
| [laaielichter/reverseport](https://github.com/laaielichter/reverseport) | GitHub project | `web` `reconstruction` `binary-analysis` `community` | ★ 2 | 2026-10-12 |
| [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) | GitHub project | `reconstruction` `decompilation` `community` | ★ 2 | 2026-10-12 |
| [git-sanbu/awesome-rea](https://github.com/git-sanbu/awesome-rea) | GitHub project | `android` `community` | ★ 1 | 2026-10-16 |
| [awesomerea/awesome-rea](https://github.com/awesomerea/awesome-rea) | GitHub project | `community` | ★ 1 | 2026-10-16 |
| [victcn/rea-codex](https://github.com/victcn/rea-codex) | GitHub project | `reconstruction` `binary-analysis` `community` | ★ 1 | 2026-10-15 |
| [zheedevVn/Rea-Unlock](https://github.com/zheedevVn/Rea-Unlock) | GitHub project | `decompilation` `binary-analysis` `community` | ★ 1 | 2026-10-15 |
| [alexmi256/rea-agent-docker](https://github.com/alexmi256/rea-agent-docker) | GitHub project | `decompilation` `community` | ★ 1 | 2026-10-14 |
| [ReversoAgent/reverso](https://github.com/ReversoAgent/reverso) | GitHub project | `community` | ★ 1 | 2026-10-15 |
| [sickpyramid/ReaFuse](https://github.com/sickpyramid/ReaFuse) | GitHub project | `community` | ★ 1 | 2026-10-14 |
| [stuinfla/morluto-rea-explainer](https://github.com/stuinfla/morluto-rea-explainer) | GitHub project | `community` | ★ 1 | 2026-10-14 |
| [xingxue-ux/dsh-reverse-mode](https://github.com/xingxue-ux/dsh-reverse-mode) | GitHub project | `native` `community` | ★ 1 | 2026-10-13 |
| [maximilianfeix/hexvero](https://github.com/maximilianfeix/hexvero) | GitHub project | `electron` `native` `web` `binary-analysis` `community` | ★ 1 | 2026-10-13 |
| [miles990/rea-awesome](https://github.com/miles990/rea-awesome) | GitHub project | `community` | ★ 1 | 2026-10-12 |
| [miles990/rea-case-rankings](https://github.com/miles990/rea-case-rankings) | GitHub project | `community` | ★ 1 | 2026-10-14 |
| [inematds/rea-engenharia-reversa](https://github.com/inematds/rea-engenharia-reversa) | GitHub project | `decompilation` `community` | ★ 1 | 2026-10-12 |
| [ya123-4/rea-dsh-plugin](https://github.com/ya123-4/rea-dsh-plugin) | GitHub project | `community` | ★ 1 | 2026-10-15 |
| [ylwl1997/rea-run](https://github.com/ylwl1997/rea-run) | GitHub project | `community` | ★ 1 | 2026-10-12 |
| [shaochengrun/rea-tool](https://github.com/shaochengrun/rea-tool) | GitHub project | `community` | — | 2026-10-16 |
| [TheBabelDragon/REA](https://github.com/TheBabelDragon/REA) | GitHub project | `reconstruction` `community` | — | 2026-10-16 |
| [xingruochun/dsh-rea](https://github.com/xingruochun/dsh-rea) | GitHub project | `community` | — | 2026-10-16 |
| [znadi953-commits/rea](https://github.com/znadi953-commits/rea) | GitHub project | `community` | — | 2026-10-16 |
| [AllwynGeorgeA/Reverse-Engineer-Anything](https://github.com/AllwynGeorgeA/Reverse-Engineer-Anything) | GitHub project | `community` | — | 2026-10-16 |
| [DevgenX/seo-rea](https://github.com/DevgenX/seo-rea) | GitHub project | `community` | — | 2026-10-15 |
| [jhwaijeh-gif/reverse-engineer-anything](https://github.com/jhwaijeh-gif/reverse-engineer-anything) | GitHub project | `community` | — | 2026-10-16 |
| [majbal87/rea-addons](https://github.com/majbal87/rea-addons) | GitHub project | `community` | — | 2026-10-16 |
| [ManuzXo/REA-AGENT](https://github.com/ManuzXo/REA-AGENT) | GitHub project | `community` | — | 2026-10-16 |
| [stevenli91748/Reverse-Engineer-Anything---](https://github.com/stevenli91748/Reverse-Engineer-Anything---) | GitHub project | `community` | — | 2026-10-16 |
| [tororex250-ship-it/rea-mcp-bridge](https://github.com/tororex250-ship-it/rea-mcp-bridge) | GitHub project | `community` | — | 2026-10-15 |
| [wyfirstname/rea-ui](https://github.com/wyfirstname/rea-ui) | GitHub project | `windows` `community` | — | 2026-10-16 |
| [848gaming/anti-rea](https://github.com/848gaming/anti-rea) | GitHub project | `electron` `binary-analysis` `community` | — | 2026-10-14 |
| [aliaihub/rea-casebook](https://github.com/aliaihub/rea-casebook) | GitHub project | `reconstruction` `binary-analysis` `community` | — | 2026-10-15 |
| [andresanino/rea-cloud](https://github.com/andresanino/rea-cloud) | GitHub project | `community` | — | 2026-10-16 |
| [arwinwijaya/maw-rea](https://github.com/arwinwijaya/maw-rea) | GitHub project | `community` | — | 2026-10-14 |
| [Gerrard-Lewu/reverse-engineer-anything](https://github.com/Gerrard-Lewu/reverse-engineer-anything) | GitHub project | `community` | — | 2026-10-14 |
| [jefersonprimer/reverse-engineer-anything](https://github.com/jefersonprimer/reverse-engineer-anything) | GitHub project | `community` | — | 2026-10-15 |
| [junaid-bacha/reverse-engineer-anything](https://github.com/junaid-bacha/reverse-engineer-anything) | GitHub project | `community` | — | 2026-10-14 |
| [makimeaqua/rea-empty-placeholder](https://github.com/makimeaqua/rea-empty-placeholder) | GitHub project | `windows` `community` | — | 2026-10-14 |
| [scottkw/rea-installer](https://github.com/scottkw/rea-installer) | GitHub project | `windows` `linux` `macos` `community` | — | 2026-10-15 |
| [AdamLinCodes/AdamTerm](https://github.com/AdamLinCodes/AdamTerm) | GitHub project | `macos` `community` | — | 2026-10-14 |
| [andy778/ananasar](https://github.com/andy778/ananasar) | GitHub project | `electron` `reconstruction` `community` | — | 2026-10-14 |
| [Asymmetrical-1024/awsome-REA](https://github.com/Asymmetrical-1024/awsome-REA) | GitHub project | `community` | — | 2026-10-13 |
| [caixuf/dsh-rea](https://github.com/caixuf/dsh-rea) | GitHub project | `android` `electron` `native` `web` `binary-analysis` | — | 2026-10-13 |
| [crabsoupT0T/rea-plus](https://github.com/crabsoupT0T/rea-plus) | GitHub project | `android` `electron` `reconstruction` `community` | — | 2026-10-14 |
| [Nowng/rea-mcp](https://github.com/Nowng/rea-mcp) | GitHub project | `community` | — | 2026-10-13 |
| [shivangsaxena1011/Reverse-Engineer-Anything](https://github.com/shivangsaxena1011/Reverse-Engineer-Anything) | GitHub project | `community` | — | 2026-10-13 |
| [shreyvijayvargiya/reverse-engineer-crm](https://github.com/shreyvijayvargiya/reverse-engineer-crm) | GitHub project | `community` | — | 2026-10-14 |
| [UnknownHacker1/rea-groundtruth](https://github.com/UnknownHacker1/rea-groundtruth) | GitHub project | `electron` `community` | — | 2026-10-14 |
| [Ydjin1984/rea-reverse-engineering](https://github.com/Ydjin1984/rea-reverse-engineering) | GitHub project | `android` `electron` `web` `decompilation` `community` | — | 2026-10-14 |
| [ALC-kcurtis/rea](https://github.com/ALC-kcurtis/rea) | GitHub project | `community` | — | 2026-10-13 |
| [beyborges/REA](https://github.com/beyborges/REA) | GitHub project | `electron` `native` `windows` `decompilation` `binary-analysis` | — | 2026-10-13 |

*… 7 more in [data/cases.json]](data/cases.json).*


### Posts & discussions

Hacker News threads, GitHub discussions and Reddit posts showing REA in action.

| Case | Source | Tags | Highlights | First seen |
|------|--------|------|------------|------------|
| [Reverse engineer anything with agents, from app behavior down to native binaries](https://news.ycombinator.com/item?id=50058850) | Hacker News | `native` `discussion` | HN 99 pts · 💬 38 | 2026-10-13 |
| [REA: Reverse Engineer Anything is now #1 trending repo on GitHub](https://news.ycombinator.com/item?id=50028294) | Hacker News | `discussion` | HN 2 pts · 💬 2 | 2026-10-12 |
| [Reverse Engineer Anything](https://news.ycombinator.com/item?id=50012930) | Hacker News | `discussion` | HN 4 pts | 2026-10-12 |
| [Ask HN: Have you checked REA(reverse engineer anything) GitHub repo?](https://news.ycombinator.com/item?id=50034003) | Hacker News | `discussion` | HN 2 pts · 💬 1 | 2026-10-12 |
| [Show and tell: Reducing token waste in REA workflows. What are you using?](https://github.com/morluto/rea/discussions/1958) | GitHub discussion | `reconstruction` `discussion` | 💬 9 | 2026-10-12 |
| [REA on Fedora-based Linux: setup notes, gotchas and my test queue](https://github.com/morluto/rea/discussions/1435) | GitHub discussion | `android` `linux` `decompilation` `discussion` | 💬 7 | 2026-10-12 |
| [First speed results: kuna, rsleigh and Ghidra on the same three files](https://github.com/morluto/rea/discussions/3858) | GitHub discussion | `decompilation` `discussion` | 💬 3 | 2026-10-15 |
| [Benchmarks: REA on Linux (Node 22, 24 and 26 startup, plus five local models)](https://github.com/morluto/rea/discussions/1998) | GitHub discussion | `linux` `discussion` | 💬 2 | 2026-10-12 |
| [Showcase: outside-in "leak check" of a production Next.js + Stripe app on Windows](https://github.com/morluto/rea/discussions/1406) | GitHub discussion | `web` `windows` `security-audit` `discussion` | 💬 2 | 2026-10-12 |
| [Community resource: Reverse Engineering 101 with REA + Ghidra](https://github.com/morluto/rea/discussions/3791) | GitHub discussion | `.net` `decompilation` `discussion` | 💬 1 | 2026-10-15 |
| [Show HN: A MCP for Agents to reverse engineer binary code](https://news.ycombinator.com/item?id=48901763) | Hacker News | `binary-analysis` `discussion` | HN 3 pts | 2026-10-12 |
| [Built a defensive counterpart: check your own site the way REA would](https://github.com/morluto/rea/discussions/4328) | GitHub discussion | `discussion` | — | 2026-10-16 |
| [Reverse Engineering toolkit](https://github.com/morluto/rea/discussions/3845) | GitHub discussion | `discussion` | — | 2026-10-15 |
| [Show and tell: LX-D02 thermal printer on Windows (React Native/Hermes app reversed)](https://github.com/morluto/rea/discussions/4152) | GitHub discussion | `android` `native` `web` `ios` `windows` | — | 2026-10-16 |
| [A 32K local model drove REA over MCP: 3 of 3 with 10 tools](https://github.com/morluto/rea/discussions/3098) | GitHub discussion | `discussion` | — | 2026-10-14 |
| [Project #000002: Tax Reborn now runs on desktop and Android (code + downloads)](https://github.com/morluto/rea/discussions/3110) | GitHub discussion | `android` `windows` `feature-tracing` `discussion` | — | 2026-10-14 |
| [Showcase: keeping browser-use tasks moving when a CAPTCHA interrupts the run](https://github.com/morluto/rea/discussions/3579) | GitHub discussion | `discussion` | — | 2026-10-15 |
| [A stripped bzip2 build on Linux: what REA returned, checked against the build and the docs](https://github.com/morluto/rea/discussions/2254) | GitHub discussion | `linux` `discussion` | — | 2026-10-13 |
| [Project #000001: From REA to a working QuickBooks-style desktop app (Mac + Windows)](https://github.com/morluto/rea/discussions/2198) | GitHub discussion | `windows` `discussion` | — | 2026-10-12 |


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
