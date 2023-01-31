import sys

shapes = {'X':1, 'Y':2, 'Z':3}
outcome = {'X':{'A':3, 'B':0, 'C':6}, 'Y':{'A':6, 'B':3, 'C':0}, 'Z':{'A':0, 'B':6, 'C':3}}


def part_one(fname):
    ans = 0
    for line in open(fname).readlines():
        a, b = line.strip().split(' ')
        ans += shapes[b] + outcome[b][a]
    return ans


def part_two(fname):
    outcome = {'X':{'A':3, 'B':1, 'C':2}, 'Y':{'A':4, 'B':5, 'C':6}, 'Z':{'A':8, 'B':9, 'C':7}}
    ans = 0
    for line in open(fname).readlines():
        a, b = line.strip().split(' ')
        ans += outcome[b][a]
    return ans

fname = sys.argv[1]
print(part_one(fname))
print(part_two(fname))
