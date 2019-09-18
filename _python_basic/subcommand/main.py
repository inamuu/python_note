# coding: utf-8

import boto3
import argparse

def helloworld(args):
    print('Hello World!')
    print(args)

def konnichiwa(args):
    print('こんにちは!')
    print(args)

def main():
    parser = argparse.ArgumentParser(
        prog='サブコマンド',
        usage='python main.py [helloworld] [-r/--role] var',
        description='サブコマンドを実装するスクリプトです。',
        add_help=True,
    )

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    subparsers = parser.add_subparsers(dest='parser', title='subcomands')
    subparsers.required = True
    
    parser_helloworld = subparsers.add_parser('helloworld', help='Hello Worldを出力します。')
    parser_helloworld.add_argument('-a', '--args', required=True)
    parser_helloworld.set_defaults(handler=helloworld)
    
    parser_konnichiwa = subparsers.add_parser('konnichiwa', help='こんにちはを出力します')
    parser_konnichiwa.add_argument('-a', '--args', required=True)
    parser_konnichiwa.set_defaults(handler=konnichiwa)
    
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()

if __name__ == '__main__': main()