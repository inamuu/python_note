# coding: utf-8

import sys


def main(args):
    helloa() if args == 'a' else None
    hellob() if args == 'b' else None


def helloa():
    print('a')


def hellob():
    print('b')


def helloc():
    print('c')


if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
