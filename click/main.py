# coding: utf-8

import click

@click.group()
def subcommand():
    pass

@subcommand.command()
def helloa():
    print('Hello A')

def main():
    subcommand()

if __name__ == '__main__': main()
