# coding: utf-8

import click

@click.group()
def subcommand():
    pass

@subcommand.command(help='hello Aだよ')
def helloa():
    print('Hello A')

@subcommand.command(help='hello Bだよ')
def hellob():
    print('Hello B')

def main():
    subcommand()

if __name__ == '__main__': main()
