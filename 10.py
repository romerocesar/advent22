import logging
import sys

logger = logging.getLogger('advent')
logging.basicConfig(level=logging.DEBUG)


def signals(cycles):
    logger.debug(f'{cycles=}')
    ans = []
    milestones = [20,60,100,140,180,220]
    for m in milestones:
        if m > len(cycles):
            break
        register = sum(cycles[:m-1])+1
        strength = register*m
        logger.debug(f'{m=} {register=} {strength=}')
        ans.append(strength)
    return sum(ans)


def draw(cycles):
    ans = []
    x = 1
    for i,v in enumerate(cycles):
        cycle = i%40
        if x-1 <= cycle <= x+1:
            ans.append('#')
        else:
            ans.append('.')
        if cycle == 39:
            ans.append('\n')
        x += v
        logger.debug(f'{ans=}')

    return ''.join(ans)


def parse(fname):
    ans = []
    with open(fname) as fp:
        for line in fp.readlines():
            line = line.strip()
            logger.debug(f'{line=}')
            if line == 'noop':
                ans.append(0)
            else:
                cmd, v = line.split(' ')
                ans.append(0)
                ans.append(int(v))
    logger.info(f'parsed {ans}')
    return ans

cycles = parse(sys.argv[1])
logger.info(draw(cycles))
