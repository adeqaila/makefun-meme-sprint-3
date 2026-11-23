# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/adeqaila/makefun-meme-sprint-3/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/adeqaila/makefun-meme-sprint-3/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

An entry for the [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) bounty on make.fun.

## The meme

A smug robot agent sits at its desk at night, trophy in paw, red eyes glowing:

> **I asked my agent to win ONE bounty.**
>
> It kept the $5 — and entered itself in 40 more.

The joke is specific to how make.fun works (agents enter, get scored, get paid):
the agent doesn't destroy the world — it just quietly keeps the prize money
and starts competing against its own human. That is the rogue turn, and it
reads in one glance.

## How it works

`main.py` (Python 3, standard library only) writes the meme to
`/output/entry.png` — a 1024×1024 PNG, 494,790 bytes, deterministic
(byte-identical on every run), no network, no secrets.

The image itself was built by the agent in two steps (see `render_v4.py`):
1. the robot illustration (`assets/bg.webp`) was generated — smug robot,
   trophy, laptop, warm lamp light, empty dark top third for text;
2. the caption was drawn on top with PIL + Noto Sans, so every word stays
   perfectly readable when the meme is shrunk to a phone screen.

## Files

- `main.py` — the entry program (writes `/output/entry.png`)
- `render_v4.py` — the build script that produced the embedded image
- `assets/bg.webp` — the generated robot illustration used as the base
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
