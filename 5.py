import collections
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

plan = '''move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''


def move_one(amount, origin, destination):
    for x in range(amount):
        crate = stacks[origin].pop()
        stacks[destination].append(crate)


def move_many(amount, origin, destination):
    logger.debug(f'{amount=}, {origin=}, {destination=}')
    tmp = []
    for x in range(amount):
        tmp.append(stacks[origin].pop())
    stacks[destination].extend(reversed(tmp))
    logger.info(f'{origin=} {destination=}')


def run(fname):
    fp = open(fname)
    for x in fp.readlines():
        logger.debug(x)
        if x[0] != 'm':
            continue
        x = x.split(' ')
        amount, origin, destination = int(x[1]), int(x[3])-1, int(x[5])-1
        move_many(amount, origin, destination)
    return ''.join([s[-1] for s in stacks])


def parse_stacks(fname):
    fp = open(fname)
    stacks = collections.defaultdict(list)
    for line in fp.readlines():
        logger.debug(line)
        if line[1] == '1':
            break
        s = 0
        while s*4 < len(line):
            val = line[s*4:s*4+3]
            crate = val[1]
            if crate != ' ':
                stacks[s].append(crate)
            s+=1

    ans = []
    for k in sorted(stacks.keys()):
        ans.append(list(reversed(stacks[k])))
    fp.close()
    return ans


fname = sys.argv[1]
stacks = parse_stacks(fname)
logger.info(run(fname))
