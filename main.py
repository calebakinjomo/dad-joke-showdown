"""Dad Joke Showdown entry — one dad joke, at most 200 characters.

Writes the joke directly to $MAKEFUN_OUTPUT_DIR/entry.txt with a plain
file write (no tempfile + rename). Python 3, standard library only.
"""

import os

JOKE = "The Wi-Fi went down at dinner, so I told the kids, 'Relax \u2014 Dad's here. I'm great at making connections.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
