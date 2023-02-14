import logging
import sys


logger = logging.getLogger('advent')
logging.basicConfig(level=logging.INFO)

def parse(fname):
    ans = []
    with open(fname) as fp:
        for line in fp.readlines():
            d, n = line.strip().split()
            for i in range(int(n)):
                ans.append(d)

    return ans


d = {'R':(1,0),'U':(0,1),'L':(-1,0),'D':(0,-1)}
def move_knot(prev, knot, direction):
    logger.debug(f'{prev=} {knot=} {direction=}')
    if prev is None:
        delta = d[direction]
    else:
        if dist(prev,knot) > 1:
            dx = prev[0]-knot[0]
            dx = dx/abs(dx) if dx else 0
            dy = prev[1]-knot[1]
            dy = dy/abs(dy) if dy else 0
            delta = dx,dy
        else:
            delta = (0,0)

    ans = knot[0]+delta[0],knot[1]+delta[1]
    logger.info(f'moved to {ans}')
    return ans


def move_rope(rope, d):
    prev = None
    for i, knot in enumerate(rope):
        pos = move_knot(prev, knot, d)
        rope[i] = pos
        prev = pos


def dist(p, q):
    ans = max(abs(p[0]-q[0]), abs(p[1]-q[1]))
    logger.debug(f'dist({p=}, {q=}) = {ans}')
    return ans


def count_tail_positions(moves, knots=2):
    visited = set()
    rope = [(0,0) for k in range(knots)]
    for d in moves:
        move_rope(rope, d)
        visited.add(rope[-1])

    return len(visited)


moves = parse(sys.argv[1])
logger.info(count_tail_positions(moves, knots=10))
