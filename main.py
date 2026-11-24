#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one fresh one-line developer excuse to /output/entry.txt.
"""
import os
import shutil

LINE = "It worked in staging because staging has the same bug \u2014 nobody's clicked that button since March."
# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
# whitespace. This line is written with no trailing newline, so its char count
# is the line length itself.

def main():
    os.makedirs("/output", exist_ok=True)
    # Clear only the contents of /output, never the directory itself.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
