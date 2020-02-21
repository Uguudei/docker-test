from src.module.data_loader import oracle_import


def read():
    print(oracle_import('SELECT sysdate FROM dual'))
    print('import.py run successfully')