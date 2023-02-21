import logging
import re
import sys

logger = logging.getLogger('advent')
logging.basicConfig(level=logging.DEBUG)


class Monkey:

    def __init__(self):
        self.n = 0
        self.inspections = 0
        self.items = None
        self.operation = None
        self.test = [0,0,0]


    def __repr__(self):
        return str(self.__dict__)


def parse(fname):
    monkeys = []
    with open(fname) as fp:
        monkey = Monkey()
        for line in fp.readlines():
            line = line.strip()
            logger.debug(f'parsing {line=}')
            if not line:
                monkeys.append(monkey)
                monkey = Monkey()
            elif m := re.match(r'Monkey (\d+):', line):
                monkey.n = int(m.group(1))
            elif m := re.match(r'Starting items: (.+)', line):
                logger.debug('parsing items')
                monkey.items = [int(x) for x in m.group(1).split(',')]
                logger.debug(monkey)
            elif m := re.match(r'Operation: new = old (.) (\d+)', line):
                o = m.group(1)
                d = int(m.group(2))
                monkey.operation = (o, d)
            elif m := re.match(r'Test: divisible by (\d+)', line):
                d = int(m.group(1))
                monkey.test[0] = d
            elif m := re.match(r'If true:.+?(\d+)$', line):
                t = int(m.group(1))
                monkey.test[1] = t
            elif m := re.match(r'If false:.+?(\d+)$', line):
                f = int(m.group(1))
                monkey.test[2] = f
        else:
             monkeys.append(monkey)

    return monkeys


logger.info(parse(sys.argv[1]))
