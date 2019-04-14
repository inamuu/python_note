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
      print('そのKeyは存在しないよ')
      return

    student = yml[args]
    name    = yml[args]['name']
    age     = yml[args]['age']
    print('配列: %s' % student)
    print('名前: %s' % name)
    print('年齢: %s' % age)


if __name__ == '__main__': main()
