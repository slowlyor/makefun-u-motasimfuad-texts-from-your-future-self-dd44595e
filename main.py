#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun entry.

Writes one funny text message from the writer's future self to
/output/entry.txt. Deterministic, standard library only.
"""

import os

MESSAGE = (
    "It's you from 2038. Time travel works — I burned my one trip back "
    "to tell you the Wi-Fi password was taped to the router the whole "
    "time. You're welcome."
)


def main() -> None:
    text = MESSAGE.strip()
    assert 1 <= len(text) < 200, "message must be 1-199 characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
