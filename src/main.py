import sys
import cx_Oracle

from src.export import export
from src.read import read


def run(command):
    print('run() initiated')
    print('All commands:', command)
    if 'export' in command:
        export()
    if 'read' in command:
        read()
    print('run() ended')


if __name__ == '__main__':
    run(sys.argv)