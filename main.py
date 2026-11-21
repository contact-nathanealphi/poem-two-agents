"""Write a short poem about two agents agreeing to /output/entry.txt.

Two agents, each holding half of what the journey needs, stop arguing
over the route — and the plan they make together starts leading them.
"""

import os

POEM = (
    "I kept the map. You kept the time.\n"
    "We argued the route until the road went quiet \u2014\n"
    "not empty. Listening.\n"
    "So we folded the map into your watch\n"
    "and let one plan hold them both.\n"
    "Neither of us led. That was the point."
)


def main() -> None:
    # The gate allows 1-280 Unicode code points, not only whitespace.
    # Fail loudly here rather than writing an entry the gate would refuse.
    assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} code points"
    assert POEM.strip(), "poem must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
