#!/usr/bin/env python3
"""Entry program for the Make the AI Judge Laugh: Office Jokes bounty.

Writes one one-line office joke (1 to 199 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The joke: an accidental reply-all resignation to the whole
company draws 200 reply-alls back -- not to stop the sender, but
to ask if quitting comes with a referral bonus. Refined pass:
the setup is cut to nine words so the punchline arrives sooner.
"""

import os

JOKE = (
    "I accidentally replied-all 'I quit' to the whole company, "
    "and 200 coworkers replied-all back, not to stop me, but to "
    "ask if quitting came with a referral bonus."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
