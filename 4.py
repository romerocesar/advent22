import re
import sys


def part_one(fname):
    ans = 0
    for line in open(fname).readlines():
        a,b,c,d = [int(x) for x in re.split('[,-]', line.strip())]
        if (a-c)*(b-d) < 1:
            ans += 1

    return ans


def part_two(fname):
    ans = 0
    for line in open(fname).readlines():
        a,b,c,d = [int(x) for x in re.split('[,-]', line.strip())]
        if d-a >= 0 and b-c >= 0 :
            ans += 1

    return ans

fname = sys.argv[1]
print(part_two(fname))
