# coding: utf-8

import sys


def main(args):
    helloa() if args == 'a': else helloc()
    hellob() if args == 'b': else helloc()


def helloa():
    print('a')


def hellob():
    print('b')


def helloc():
    print('c')


if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
