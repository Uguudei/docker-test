import logging
import sys

from src.main import run

logging.basicConfig(
    # filename='logs/basic.log',
    format='%(asctime)-20s %(levelname)-8s L:%(lineno)-4d %(name)-30s M:%(module)-30s F:%(funcName)-20s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # run(sys.argv)
    run(['test', 'export'])
