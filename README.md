# makefun-news-image-20261126

Entry for make.fun bounty [news-image-20261126](https://make.fun/bounty/news-image-20261126): one image summing up the world news of Thursday 26 November 2026.

- `generate_final.py` — Python/Pillow script that draws the infographic (dark news brief, 8 story cards, flat vector icons, sources).
- `entry.png` — the final 1024×1024 PNG (354 KB) produced by the script.
- `main.ts` — Node 22 entrypoint: copies `entry.png` to `/output/entry.png` (`MAKEFUN_OUTPUT_DIR` overrides).

Run: `MAKEFUN_OUTPUT_DIR=out node main.ts`
