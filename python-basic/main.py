import sys

def help():
    command_name = sys.argv[0]
    helpmsg = """
  ヘルプだよ
  引数を1つだけ指定してね
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