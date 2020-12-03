import logging

from src.main import run

logging.basicConfig(
    filename='logs/basic.log',
    format='%(asctime)-20s %(levelname)-8s L:%(lineno)-4d %(name)-32s M:%(module)-32s F:%(funcName)-20s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)
logger.info('start---------------------------------------------------------')

if __name__ == '__main__':
    # run(sys.argv)
    run(['test', 'export'])
    logger.info('volume working')

logger.info('end-----------------------------------------------------------')
