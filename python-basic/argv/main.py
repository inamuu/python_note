# coding: utf-8

import sys

def help():
    helpmsg = """
    [ヘルプ]
      # 引数を1つだけ指定してね
      python main.py [VARIABLE]
"""
    print(helpmsg)

def checkarg():
    if len(sys.argv) == 2:
      args = sys.argv[1]
      return args
    else:
      help()
      exit()

def main():
    msg = checkarg()
    print(msg)

if __name__ == "__main__": main()
