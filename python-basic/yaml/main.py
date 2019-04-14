# coding: utf-8

import yaml
import sys

def main():
    with open('test.yaml') as file:
        yml = yaml.full_load(file)

    ## コマンドライン引数
    args = sys.argv[1]

    ## Keyの存在チェック. Valueはチェックしないので注意.
    if args not in yml:
      print('not in')
      return

    val  = yml[args]
    name = yml[args]['name']
    age  = yml[args]['age']
    print(val)
    print(name)
    print(age)


if __name__ == '__main__': main()
