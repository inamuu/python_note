# coding: utf-8

import json


def main():
    d1 = {'k1': 1, 'k2': 2}
    d2 = {'k3': 100, 'k4': 3, 'k5': 4}
    d1.update(d2)
    print(d1)


if __name__ == '__main__':
    main()
