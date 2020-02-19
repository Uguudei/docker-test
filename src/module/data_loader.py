import pandas as pd
from sqlalchemy import create_engine

from src.config.read_config import set_oracle_connection
from src.module.helper import timeit


@timeit
def oracle_import(query):
    """Import from oracle DB"""
    engine = create_engine(set_oracle_connection())
    data_frame = pd.read_sql(query, engine)
    return data_frame


def main():
    """Test oracle_import function"""
    print('Test import from Oracle DB')
    print(oracle_import('SELECT sysdate FROM dual'))


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
