import logging
import string
import sys

logger = logging.getLogger()

letters = string.ascii_lowercase+string.ascii_uppercase
priorities = dict(zip(letters, range(1, len(letters)+1)))


def part_one(fname):
    ans = 0
    for line in open(fname).readlines():
        items = line.strip()
        n = len(items)
        left = set(items[:n//2])
        right = set(items[n//2:])
        common = left.intersection(right)
        ans += priorities[common.pop()]
    return ans


def part_two(fname):
    ans = 0
    group = []
    for line in open(fname).readlines():
        if items := line.strip():
            group.append(items)
            if len(group) < 3:
                continue
            sets = [set(x) for x in group]
            common = sets[0].intersection(sets[1]).intersection(sets[2]).pop()
            ans += priorities[common]
            group.clear()
    return ans

fname = sys.argv[1]
print(part_one(fname))
print(part_two(fname))
