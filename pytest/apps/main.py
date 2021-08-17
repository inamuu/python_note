# coding: utf-8

import sys

record = sys.argv[1]

def main(record: str):
    data = str('test_') + record
    return data

if __name__ == '__main__': main(record)
