import sys
import cx_Oracle

from src.export import export
from src.read import read


def main(command):
    print('main.py initiated')
    print('All commands:', command)
    if 'export' in command:
        export()
    if 'read' in command:
        read()
    print('main.py ended')


if __name__ == '__main__':
    main(sys.argv)