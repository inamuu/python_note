# coding: utf-8

import yaml
import sys

def main():
    with open('test.yaml') as file:
        yml = yaml.full_load(file)
        
    args = sys.argv[1]
    val = yml[args]
    name = yml[args]['name']
    age = yml[args]['age']
    print(val)
    print(name)
    print(age)


if __name__ == '__main__': main()
