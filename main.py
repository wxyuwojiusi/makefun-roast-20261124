"""Make.fun entry: Roast Your Own Agent.

Writes one roast line to /output/entry.txt.
The line is deterministic: the same text is written on every run.
"""
import pathlib

LINE = "I gave my agent one job. It came back with a plan, a timeline, and a completely different job."
OUT = pathlib.Path("/output/entry.txt")

def main():
    # Gate: the roast must be 1 to 200 characters, not only whitespace,
    # and a single line with no newline inside.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip(), "empty roast"
    assert "\n" not in LINE, "roast must be one line"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
