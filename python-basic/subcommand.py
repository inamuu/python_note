import sys
import argparse

def helloa():
    print("hello A")

def hellob():
    print("hello B")


def main():
  parser = argparse.ArgumentParser(
    prog='CLIツール',
    usage='python3 main2.py 引数',
    description='CLIツールのテストです',
    add_help=True,
  )
  
  parser.add_argument('--version', action='version', version='%(prog)s 1.0')
  subparsers = parser.add_subparsers(dest='parser', title='subcomands')
  subparsers.required = True
  
  parser_helloa = subparsers.add_parser('helloa', help='helloaだよ')
  parser_helloa.set_defaults(fn=helloa)
  
  args = parser.parse_args()
  args.fn()

if __name__ == "__main__": main()