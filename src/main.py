import logging
import sys

from src.export import export
from src.module.helper import logging_timer
from src.read import read

# Define logger for a app
logger = logging.getLogger(__name__)


@logging_timer
def run(command):
    logger.info('function initiated')
    logger.info(f'All commands:{command}')
    if 'export' in command:
        export()
        logger.debug('command 1')
    elif 'read' in command:
        read()
        logger.debug('command 2')
    elif len(command) == 1:
        logger.debug('command 2')
    logger.warning('test warning')
    logger.debug('ended')


if __name__ == '__main__':
    run(sys.argv)
