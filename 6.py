import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def part_one(s):
    logger.debug(s)
    left, right = 0, 0
    seen = {}
    while True:
        logger.debug(f'{left=} {right=} {seen=}')
        if s[right] in seen:
            while s[right] in seen and left <= seen[s[right]]:
                del seen[s[left]]
                left += 1
        seen[s[right]] = right
        right += 1
        if right-left == 14:
            logger.debug(f'{left=} {right=} {seen=}')
            return right


s = sys.argv[1]
logger.info(part_one(s))
