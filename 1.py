from pathlib import Path
import sys


def parse_input(fname):
    ans = []
    cals = 0
    for line in open(fname).readlines():
        if line := line.strip():
            cals += int(line)
        else:
            ans.append(cals)
            cals = 0

    return ans


fname = sys.argv[1]
calories = parse_input(fname)
print(sum(list(sorted(calories))[-3:]))
