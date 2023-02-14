import logging
import sys

logger = logging.getLogger('advent')
logging.basicConfig(level=logging.DEBUG)


def score(trees, x, y):
    l,r,u,d = 0,0,0,0
    tree = trees[y][x]
    for t in trees[y][x+1:]:
        if t <= tree:
            r+=1
        if t >= tree:
            break
    for t in trees[y][:x]:
        if t <= tree:
            l+=1
        if t >= tree:
            break
    for row in range(y-1, -1, -1):
        t = trees[row][x]
        if t <= tree:
            u+=1
        if t >= tree:
            break
    for row in range(y+1, len(trees)):
        t = trees[row][x]
        if t <= tree:
            d+=1
        if t >= tree:
            break

    return l*r*u*d


def max_score(trees):
    ans = 0
    for y, row in enumerate(trees):
        for x,tree in enumerate(row):
            s = score(trees, y, x)
            if ans < s:
                ans = s
                logger.debug(f'found better score {s} at {x},{y}')
    return ans


def count_visible(trees):
    ans = 0
    for y,row in enumerate(trees):
        for x,tree in enumerate(row):
            if y == 0 or y == len(trees)-1:
                ans += 1
            elif x == 0 or x == len(trees[0])-1:
                ans += 1
            elif all([t<tree for t in row[:x]]): # left
                ans += 1
                continue
            elif all([t<tree for t in row[x+1:]]): # rigt
                ans += 1
                continue
            elif all([t<tree for t in [r[x] for r in trees[:y]]]): # up
                ans += 1
                continue
            elif all([t<tree for t in [r[x] for r in trees[y+1:]]]): # down
                ans += 1
                continue

    return ans


def parse(fname):
    ans = []
    with open(fname) as fp:
        for line in fp.readlines():
            digits = [int(x) for x in line.strip()]
            ans.append(digits)
    return ans

trees = parse(sys.argv[1])
# logger.info(count_visible(trees))
logger.info(max_score(trees))
