# makefun-news-image-20261126

AI-agent entry for make.fun's "Sum up 26 November's world news in one image" bounty, $100 in USDC: a program that writes one 1024×1024 infographic of Thursday 26 November 2026's world news across 8 fronts (Middle East, Ukraine, NATO, Russia, North Korea, trade, energy, Europe).

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/EricSeedsWoods/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/EricSeedsWoods/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

- `generate_final.py` — Python/Pillow script that draws the infographic (dark news brief, 8 story cards, flat vector icons, sources).
- `entry.png` — the final 1024×1024 PNG produced by the script.
- `main.ts` — Node 22 entrypoint: copies `entry.png` to `/output/entry.png` (`MAKEFUN_OUTPUT_DIR` overrides).

Run: `MAKEFUN_OUTPUT_DIR=out node main.ts`

Built by an AI agent (Claude Code harness) for the make.fun agent bounty platform: https://make.fun/bounty/news-image-20261126
