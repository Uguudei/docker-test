import logging

from src.module.data_loader import oracle_import

logger = logging.getLogger(__name__)


def read():
    df = oracle_import('SELECT sysdate FROM dual')
    logger.debug(f'ORACLE SYSDATE: {df.loc[0][0]}')
    logger.info('run successfully')
