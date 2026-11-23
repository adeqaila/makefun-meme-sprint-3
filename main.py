#!/usr/bin/env python3
"""Meme Sprint 3 entry: emit the pre-rendered meme image.

The finished meme ships in this repo as assets/meme.png; this program
just copies those bytes to /output/entry.png. Stdlib only, deterministic.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "assets", "meme.png")
    os.makedirs("/output", exist_ok=True)
    dst = os.path.join("/output", "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("copied file size does not match source")
    print("wrote", dst)


if __name__ == "__main__":
    main()
