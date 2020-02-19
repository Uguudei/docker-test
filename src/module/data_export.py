import math

import pandas as pd
from sqlalchemy import create_engine, types

from src.config.read_config import set_oracle_connection
from src.module.helper import timeit


def col_length(str_len):
    """Calculate column lengths"""
    # threshold = 2**(pw-1)
    pw = int(math.log(str_len, 2))
    return int(math.ceil((str_len + 2 ** (pw - 1)) / 2 ** (pw - 1)) * 2 ** (pw - 1))


def sql_col(data_frame):
    """Convert python data types to sql data types"""
    dtypes_dict = {}
    for column, dtype in zip(data_frame.columns, data_frame.dtypes):
        if "object" in str(dtype):
            str_max_len = col_length(data_frame[column].str.len().max())
            dtypes_dict.update({column: types.VARCHAR(length=str_max_len)})
        if "datetime" in str(dtype):
            dtypes_dict.update({column: types.DateTime()})
        if "float" in str(dtype):
            dtypes_dict.update({column: types.FLOAT})  # .Float(precision=3, asdecimal=True)})
        if "int" in str(dtype):
            dtypes_dict.update({column: types.INT()})
    return dtypes_dict


@timeit
def oracle_export(data_frame, table_name, index=False, if_exists='replace'):
    """Export to oracle DB"""
    engine = create_engine(set_oracle_connection())  # , convert_unicode=True, encoding='utf-8')
    output_dtypes_dict = sql_col(data_frame)
    data_frame.to_sql(table_name.lower(), con=engine, if_exists=if_exists, index=index, dtype=output_dtypes_dict)


def main():
    """Test oracle_export function"""
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    print('Test export to Oracle DB')
    print(oracle_export(df, 'oracle_export_test'))


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
