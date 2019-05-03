# coding: utf-8

import click

@click.command()
@click.option('--count', default=1, help='繰り返すメッセージの数だよ')
@click.option('--msg', prompt='メッセージを入力してください', help='表示するメッセージの内容だよ')
def main(count, msg):
    for i in range(count):
        print('メッセージ: %s' % msg)

if __name__ == '__main__': main()
