import logging
import sys

logger = logging.getLogger('advent')
logging.basicConfig(level=logging.DEBUG)


class Node:


    def __init__(self, parent=None, children=None, name=None, size=0):
        self.parent=parent
        self.children=children or {}
        self.name=name
        self.size=size


    def post_order(self):
        global total
        logger.debug(f'post_order({self})')
        if not self.children:
            return self.size
        else:
            self.size = sum([c.post_order() for c in self.children.values()])
            logger.info(f'{self.name=} has {self.size=}')
            if self.size < 100000:
                total += self.size
            return self.size


    def __repr__(self):
        return f'Node({self.name=}, {self.size=}, {self.children.keys=})'


def find_candidate(node, th=0):
    logger.debug(f'looking for {th=} starting from {node.name=} which is {node.size=}')
    ans = node
    if node.size < th:
        logger.info(f'discarding {node.name=}. too small {node.size=} < {th=}')
        return None
    elif not node.children:
        logger.info(f'found leaf {node.name=} with {node.size=}')
        return None
    else:
        for k, v in node.children.items():
            candidate = find_candidate(v, th)
            if candidate and candidate.size < ans.size:
                ans = candidate
        logger.info(f'found candidate {node.name=} which is {node.size=}')
        return ans


def parse(fname):
    root = Node(name='/')
    current = root
    for line in open(fname).readlines():
        line = line.strip()
        logger.debug(line)
        if line.endswith('..'):
            current = current.parent
        elif line[:4] == '$ cd':
            dirname = line.split(' ')[2]
            if dirname == '/':
                continue
            current = current.children[dirname]
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            name = line.split(' ')[1]
            node = Node(parent=current, name=name)
            current.children[name] = node
        else:
            size, name = line.split(' ')
            size = int(size)
            node = Node(parent=current, name=name, size=size)
            current.children[name] = node

    return root


fname = sys.argv[1]
root = parse(fname)
total = 0
root.post_order()
logger.info(f'{total=}')
directory = find_candidate(root, th=root.size-4e7)
logger.info(f'{directory.name=}')


        
