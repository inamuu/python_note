# coding: utf-8

import yaml
import sys

def main():
    with open('test.yaml') as file:
        yml = yaml.safe_load(file)
        print(yml)
    args = sys.argv
    print(args)

if __name__ == '__main__': main()
