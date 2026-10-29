# REA Gems

<p align="center">
  <img src="assets/logo.svg" width="120" alt="REA Gems logo" />
</p>

[![Auto-updated daily](https://img.shields.io/badge/auto--updated-daily-brightgreen)](https://github.com/sqwu/rea-gems/actions/workflows/update.yml)
[![Cases](https://img.shields.io/badge/cases-222-blue)](data/cases.json)
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

> **222 cases** collected · **222 added in the last 30 days** · last refresh: **2026-10-29 (UTC)**

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
| [Build RL environments with REA](https://rea.tools/guides/rl-environments) | Official showcase | `web` `reconstruction` `feature-tracing` `official` | — | 2026-10-26 |
| [DX-Ball's sound-pan calculation](https://rea.tools/showcase/dx-ball) | Official showcase | `native` `windows` `reconstruction` `binary-analysis` `official` | — | 2026-10-12 |
| [How an authenticator generates a login code](https://rea.tools/showcase/aegis) | Official showcase | `android` `feature-tracing` `official` | — | 2026-10-12 |
| [How Notion copies text and HTML](https://rea.tools/showcase/notion) | Official showcase | `electron` `web` `feature-tracing` `official` | — | 2026-10-12 |
| [How TH04 aims a ring of bullets](https://rea.tools/showcase/th04) | Official showcase | `dos` `reconstruction` `official` | — | 2026-10-12 |
| [Solve a CTF flag checker](https://rea.tools/showcase/ctf) | Official showcase | `native` `ctf` `official` | — | 2026-10-12 |


### Community projects

Open-source repos, rebuilds and reimplementations made with REA.

| Case | Source | Tags | Highlights | First seen |
|------|--------|------|------------|------------|
| [aicodeking/leanrea](https://github.com/aicodeking/leanrea) | GitHub project | `community` | ★ 3,510 | 2026-10-17 |
| [AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything) | GitHub project | `reconstruction` `community` | ★ 268 | 2026-10-18 |
| [Speedrunlab/reverse-engineer-anything-self-learning-loop](https://github.com/Speedrunlab/reverse-engineer-anything-self-learning-loop) | GitHub project | `native` `reconstruction` `community` | ★ 110 | 2026-10-23 |
| [ShadowSwaps/REA-Reconstruction-Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion) | GitHub project | `reconstruction` `community` | ★ 118 | 2026-10-15 |
| [ringozzt/rea-research](https://github.com/ringozzt/rea-research) | GitHub project | `community` | ★ 84 | 2026-10-12 |
| [Fanqi89/dsh-rea](https://github.com/Fanqi89/dsh-rea) | GitHub project | `community` | ★ 81 | 2026-10-13 |
| [inematds/rea-engenharia-reversa](https://github.com/inematds/rea-engenharia-reversa) | GitHub project | `decompilation` `community` | ★ 58 | 2026-10-12 |
| [REA-Gith/REA](https://github.com/REA-Gith/REA) | GitHub project | `native` `windows` `decompilation` `community` | ★ 52 | 2026-10-17 |
| [czcdr/dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea) | GitHub project | `android` `electron` `decompilation` `binary-analysis` `community` | ★ 49 | 2026-10-12 |
| [ReverseEngineerAnything/REA](https://github.com/ReverseEngineerAnything/REA) | GitHub project | `native` `windows` `decompilation` `community` | ★ 49 | 2026-10-12 |
| [rea-githu/REA](https://github.com/rea-githu/REA) | GitHub project | `native` `windows` `decompilation` `community` | ★ 37 | 2026-10-14 |
| [valorisa/Reverse-Engineer-Anything](https://github.com/valorisa/Reverse-Engineer-Anything) | GitHub project | `decompilation` `community` | ★ 36 | 2026-10-13 |
| [ReverseEngineer-Anything/REA-Github](https://github.com/ReverseEngineer-Anything/REA-Github) | GitHub project | `decompilation` `community` | ★ 31 | 2026-10-22 |
| [dav1dngy/era-agent](https://github.com/dav1dngy/era-agent) | GitHub project | `community` | ★ 20 | 2026-10-14 |
| [kandada/rea-python](https://github.com/kandada/rea-python) | GitHub project | `native` `web` `reconstruction` `community` | ★ 16 | 2026-10-17 |
| [alexmi256/rea-agent-docker](https://github.com/alexmi256/rea-agent-docker) | GitHub project | `decompilation` `community` | ★ 14 | 2026-10-14 |
| [awesomerea/awesome-rea](https://github.com/awesomerea/awesome-rea) | GitHub project | `community` | ★ 11 | 2026-10-16 |
| [git-sanbu/awesome-rea](https://github.com/git-sanbu/awesome-rea) | GitHub project | `android` `community` | ★ 9 | 2026-10-16 |
| [pablodiazjorge/rea-lab](https://github.com/pablodiazjorge/rea-lab) | GitHub project | `windows` `decompilation` `binary-analysis` `community` | ★ 7 | 2026-10-12 |
| [reverse-engineer-anything/REA-Github](https://github.com/reverse-engineer-anything/REA-Github) | GitHub project | `native` `windows` `decompilation` `community` | ★ 6 | 2026-10-20 |
| [dagoSte/rea-safe-agents](https://github.com/dagoSte/rea-safe-agents) | GitHub project | `windows` `linux` `macos` `security-audit` `community` | ★ 6 | 2026-10-19 |
| [xingxue-ux/dsh-reverse-mode](https://github.com/xingxue-ux/dsh-reverse-mode) | GitHub project | `native` `community` | ★ 5 | 2026-10-13 |
| [caixuf/dsh-rea](https://github.com/caixuf/dsh-rea) | GitHub project | `android` `electron` `native` `web` `binary-analysis` | ★ 4 | 2026-10-13 |
| [laaielichter/Reverseport](https://github.com/laaielichter/Reverseport) | GitHub project | `web` `reconstruction` `binary-analysis` `community` | ★ 4 | 2026-10-19 |
| [KoNit-K/papertrade-research](https://github.com/KoNit-K/papertrade-research) | GitHub project | `binary-analysis` `community` | ★ 3 | 2026-10-22 |
| [miles990/rea-case-rankings](https://github.com/miles990/rea-case-rankings) | GitHub project | `community` | ★ 3 | 2026-10-14 |
| [Speedrunlab/reverse-engineer-anything](https://github.com/Speedrunlab/reverse-engineer-anything) | GitHub project | `community` | ★ 2 | 2026-10-22 |
| [sheilacraig/dsh-rea-mcp](https://github.com/sheilacraig/dsh-rea-mcp) | GitHub project | `community` | ★ 2 | 2026-10-13 |
| [laaielichter/reverseport](https://github.com/laaielichter/reverseport) | GitHub project | `web` `reconstruction` `binary-analysis` `community` | ★ 2 | 2026-10-12 |
| [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) | GitHub project | `reconstruction` `decompilation` `community` | ★ 2 | 2026-10-12 |
| [reagithu/REA-Github](https://github.com/reagithu/REA-Github) | GitHub project | `decompilation` `community` | ★ 1 | 2026-10-28 |
| [Verisw/rea-dsh](https://github.com/Verisw/rea-dsh) | GitHub project | `web` `decompilation` `community` | ★ 1 | 2026-10-25 |
| [jtcjwm/dsh-rea-own](https://github.com/jtcjwm/dsh-rea-own) | GitHub project | `community` | ★ 1 | 2026-10-24 |
| [womp08310-cyber/rea-antigravity](https://github.com/womp08310-cyber/rea-antigravity) | GitHub project | `decompilation` `community` | ★ 1 | 2026-10-22 |
| [67rb/reverse-engineer-anything-beta](https://github.com/67rb/reverse-engineer-anything-beta) | GitHub project | `electron` `web` `macos` `community` | ★ 1 | 2026-10-21 |
| [67rb/reverse-engineer-anything-beta-improved](https://github.com/67rb/reverse-engineer-anything-beta-improved) | GitHub project | `electron` `web` `macos` `community` | ★ 1 | 2026-10-26 |
| [psyb0t/docker-reverse-engineer-anything](https://github.com/psyb0t/docker-reverse-engineer-anything) | GitHub project | `android` `decompilation` `community` | ★ 1 | 2026-10-19 |
| [sqkl520/rea-handbook](https://github.com/sqkl520/rea-handbook) | GitHub project | `community` | ★ 1 | 2026-10-19 |
| [Thegreatprabh/Argus](https://github.com/Thegreatprabh/Argus) | GitHub project | `reconstruction` `community` | ★ 1 | 2026-10-18 |
| [dushudou/dsh-rea](https://github.com/dushudou/dsh-rea) | GitHub project | `community` | ★ 1 | 2026-10-17 |
| [Fractal-Tess/rea-flake](https://github.com/Fractal-Tess/rea-flake) | GitHub project | `community` | ★ 1 | 2026-10-19 |
| [victcn/rea-codex](https://github.com/victcn/rea-codex) | GitHub project | `reconstruction` `binary-analysis` `community` | ★ 1 | 2026-10-15 |
| [zheedevVn/Rea-Unlock](https://github.com/zheedevVn/Rea-Unlock) | GitHub project | `decompilation` `binary-analysis` `community` | ★ 1 | 2026-10-15 |
| [aliaihub/rea-casebook](https://github.com/aliaihub/rea-casebook) | GitHub project | `reconstruction` `binary-analysis` `community` | ★ 1 | 2026-10-15 |
| [ReversoAgent/reverso](https://github.com/ReversoAgent/reverso) | GitHub project | `community` | ★ 1 | 2026-10-15 |
| [sickpyramid/ReaFuse](https://github.com/sickpyramid/ReaFuse) | GitHub project | `community` | ★ 1 | 2026-10-14 |
| [stuinfla/morluto-rea-explainer](https://github.com/stuinfla/morluto-rea-explainer) | GitHub project | `community` | ★ 1 | 2026-10-14 |
| [maximilianfeix/hexvero](https://github.com/maximilianfeix/hexvero) | GitHub project | `electron` `native` `web` `binary-analysis` `community` | ★ 1 | 2026-10-13 |
| [miles990/rea-awesome](https://github.com/miles990/rea-awesome) | GitHub project | `community` | ★ 1 | 2026-10-12 |
| [Sage-is/CleanRoom](https://github.com/Sage-is/CleanRoom) | GitHub project | `reconstruction` `community` | ★ 1 | 2026-10-25 |
| [ya123-4/rea-dsh-plugin](https://github.com/ya123-4/rea-dsh-plugin) | GitHub project | `community` | ★ 1 | 2026-10-15 |
| [ylwl1997/rea-run](https://github.com/ylwl1997/rea-run) | GitHub project | `community` | ★ 1 | 2026-10-12 |
| [cognixws/picode-rea](https://github.com/cognixws/picode-rea) | GitHub project | `community` | ★ 1 | 2026-10-20 |
| [kirinchen/goldsrc-agent-kit](https://github.com/kirinchen/goldsrc-agent-kit) | GitHub project | `community` | ★ 1 | 2026-10-22 |
| [Aetherx86/rea](https://github.com/Aetherx86/rea) | GitHub project | `native` `.net` `decompilation` `community` | — | 2026-10-29 |
| [CurLeaf/dsh-command-rea](https://github.com/CurLeaf/dsh-command-rea) | GitHub project | `community` | — | 2026-10-29 |
| [gbtweilai-star/gbt-rea-reverse](https://github.com/gbtweilai-star/gbt-rea-reverse) | GitHub project | `android` `electron` `decompilation` `community` | — | 2026-10-28 |
| [gbtweilai-star/gbt-recon-distill](https://github.com/gbtweilai-star/gbt-recon-distill) | GitHub project | `community` | — | 2026-10-28 |
| [Hamid3400/Reverse-Engineer-Anything](https://github.com/Hamid3400/Reverse-Engineer-Anything) | GitHub project | `community` | — | 2026-10-29 |
| [robort-gabriel/reverse-engineer-anything-rea-coding180](https://github.com/robort-gabriel/reverse-engineer-anything-rea-coding180) | GitHub project | `web` `community` | — | 2026-10-28 |

*… 129 more in [data/cases.json]](data/cases.json).*


### Posts & discussions

Hacker News threads, GitHub discussions and Reddit posts showing REA in action.

| Case | Source | Tags | Highlights | First seen |
|------|--------|------|------------|------------|
| [Reverse engineer anything with agents, from app behavior down to native binaries](https://news.ycombinator.com/item?id=50058850) | Hacker News | `native` `discussion` | HN 101 pts · 💬 39 | 2026-10-13 |
| ['Reverse-Engineer Anything' Is the New Wild West of AI](https://news.ycombinator.com/item?id=50167587) | Hacker News | `discussion` | HN 23 pts · 💬 8 | 2026-10-21 |
| [REA: Reverse Engineer Anything is now #1 trending repo on GitHub](https://news.ycombinator.com/item?id=50028294) | Hacker News | `discussion` | HN 2 pts · 💬 2 | 2026-10-12 |
| [Reverse Engineer Anything](https://news.ycombinator.com/item?id=50012930) | Hacker News | `discussion` | HN 4 pts | 2026-10-12 |
| [Ask HN: Have you checked REA(reverse engineer anything) GitHub repo?](https://news.ycombinator.com/item?id=50034003) | Hacker News | `discussion` | HN 2 pts · 💬 1 | 2026-10-12 |
| [Show and tell: Reducing token waste in REA workflows. What are you using?](https://github.com/morluto/rea/discussions/1958) | GitHub discussion | `reconstruction` `discussion` | 💬 9 | 2026-10-12 |
| [REA on Fedora-based Linux: setup notes, gotchas and my test queue](https://github.com/morluto/rea/discussions/1435) | GitHub discussion | `android` `linux` `decompilation` `discussion` | 💬 8 | 2026-10-12 |
| [First speed results: kuna, rsleigh and Ghidra on the same three files](https://github.com/morluto/rea/discussions/3858) | GitHub discussion | `decompilation` `discussion` | 💬 3 | 2026-10-15 |
| [A 32K local model drove REA over MCP: 3 of 3 with 10 tools](https://github.com/morluto/rea/discussions/3098) | GitHub discussion | `discussion` | 💬 2 | 2026-10-14 |
| [Benchmarks: REA on Linux (Node 22, 24 and 26 startup, plus five local models)](https://github.com/morluto/rea/discussions/1998) | GitHub discussion | `linux` `discussion` | 💬 2 | 2026-10-12 |
| [Showcase: outside-in "leak check" of a production Next.js + Stripe app on Windows](https://github.com/morluto/rea/discussions/1406) | GitHub discussion | `web` `windows` `security-audit` `discussion` | 💬 2 | 2026-10-12 |
| [An independent REA learning guide, plus a small investigation-question template](https://github.com/morluto/rea/discussions/5334) | GitHub discussion | `discussion` | 💬 1 | 2026-10-20 |
| [Awesome REA: a curated list of 250 REA resources, projects built with it, tools, and guides](https://github.com/morluto/rea/discussions/4470) | GitHub discussion | `electron` `native` `web` `discussion` | 💬 1 | 2026-10-17 |
| [Community resource: Reverse Engineering 101 with REA + Ghidra](https://github.com/morluto/rea/discussions/3791) | GitHub discussion | `.net` `decompilation` `discussion` | 💬 1 | 2026-10-15 |
| [Show HN: A MCP for Agents to reverse engineer binary code](https://news.ycombinator.com/item?id=48901763) | Hacker News | `binary-analysis` `discussion` | HN 3 pts | 2026-10-12 |
| [A worked example in Spanish: complete REA + Ghidra case with practice files](https://github.com/morluto/rea/discussions/5141) | GitHub discussion | `decompilation` `discussion` | — | 2026-10-19 |
| [REA Safe Agent: running REA and the coding agent in two network-less containers for untrusted files (unofficial)](https://github.com/morluto/rea/discussions/5255) | GitHub discussion | `discussion` | — | 2026-10-20 |
| [Python-native REA implementation for MCP (unofficial)](https://github.com/morluto/rea/discussions/4728) | GitHub discussion | `native` `reconstruction` `discussion` | — | 2026-10-18 |
| [Built a defensive counterpart: check your own site the way REA would](https://github.com/morluto/rea/discussions/4328) | GitHub discussion | `discussion` | — | 2026-10-16 |
| [Reverse Engineering toolkit](https://github.com/morluto/rea/discussions/3845) | GitHub discussion | `discussion` | — | 2026-10-15 |
| [Show and tell: LX-D02 thermal printer on Windows (React Native/Hermes app reversed)](https://github.com/morluto/rea/discussions/4152) | GitHub discussion | `android` `native` `web` `ios` `windows` | — | 2026-10-16 |
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
