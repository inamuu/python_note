# coding: utf-8

import os

def main():
    dir = './testdir/'
    list = os.listdir(dir)
    i = 0
    for file in list:
        index = list.index(file)
        i = index + 1
        print(i)
        return

if __name__ == '__main__': main()

