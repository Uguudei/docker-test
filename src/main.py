from src.module.data_export import oracle_export
from src.module.data_loader import oracle_import


def main():
    print('Test Oracle DB connection from main.py')
    # print(oracle_import('SELECT sysdate FROM dual'))
    print('working')


if __name__ == '__main__':
    main()