#!/usr/bin/env python3
"""One Star, Written in Sap — writes one one-line 1-star review from a
houseplant about its human owner to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "One star: he moved me to the bathroom for 'humidity' and now I
#    photosynthesize in the dark beside a candle that smells like my
#    replacement."
# Why it was revised: the turn is vague — a candle "smelling like my
# replacement" asks the reader to do the joke's work, and the grievance
# (moved to the bathroom) is mild. A 1-star review needs a sharper,
# more specific complaint, and the punchline should land on a
# contradiction the reader gets in one beat.
#
# REVISION (final): the grievance is now concrete and plant-specific —
# repotted into a mug with no drainage holes, a real plant-killer —
# and the turn is the owner's own words used against him: he calls
# the drowning plant "really low-maintenance" to a date. The joke is
# the gap between what he says and what the plant is living through,
# it reads as a genuine one-star review (complaint + reason for the
# single star), and it uses fresh detail with no stock phrases about
# drama queens, dramatic wilting, or being ignored.
# ---------------------------------------------------------------------------
ENTRY = (
    "One star: he repotted me into a mug with no drainage holes, then "
    "told his date I'm 'really low-maintenance' as I drowned."
)

MIN_CHARS = 1
MAX_CHARS = 279


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 279 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 279 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
