"""THE WORLD — the front page of Thursday, 19 November 2026.

One broadsheet, one day. This program does a single job: it carries
the finished page into the harness output folder exactly as drawn.
It fetches nothing, draws nothing, reads no clock and rolls no dice.

Thursday's page is led by a first: Trump, Xi and Putin sitting down
together, three-way, at the APEC summit in Shenzhen, for eighty
minutes of talk about nuclear risk, fuel supply and reforming the
United Nations. Trump put it this way: no problems were ever solved
by refusing to discuss them. Inside the paper, the world court at
The Hague finds Myanmar guilty of genocide against the Rohingya in
2017, by nine votes to six. Cyclone Akvan bears down on India's
eastern coast, driving 72,000 people from their homes in Andhra
Pradesh and Odisha ahead of a Friday noon landfall. And Nvidia
reports a record quarter — $115.8 billion of revenue, more than
double a year earlier — while its board shuts the door on Jensen
Huang's return as chief executive. Down the page, in brief: India
and Japan hold their 2+2 talks in Tokyo; the Prince and Princess of
Wales meet Prime Minister Modi in Delhi; Ukraine hits the Kerch
Bridge rail link for a third time in four days; Russian strikes
kill five in Ukraine; France sends soldiers to Ukraine for
training; and Japan's prime minister meets Putin for the first
time in seven years.

Every item carries its own bold meme cartoon — the three leaders
mid-handshake, the judge's gavel, the cyclone's spiral, the giant
glowing chip, and a small picture beside each brief.
"""

import os
import shutil
from pathlib import Path

SOURCE_NAME = "news.png"
DEST_NAME = "entry.png"


def main() -> None:
    """Hand the bundled front page to the harness output folder."""
    output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    output_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / SOURCE_NAME
    target = output_dir / DEST_NAME
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("entry.png does not match news.png")


if __name__ == "__main__":
    main()
