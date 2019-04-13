# coding: utf-8

import yaml

def main():
    with open('test.yaml') as file:
        yml = yaml.load(file)
        print(yml)

if __name__ == '__main__': main()
