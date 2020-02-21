import pandas as pd
from src.module.data_export import oracle_export


def export():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    oracle_export(df, 'oracle_export_test', if_exists='append')
    print('export.py run successfully')