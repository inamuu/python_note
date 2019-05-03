# coding: utf-8

import click

@click.group()
def subcommand():
    pass

@subcommand.command()
def helloa():
    print('Hello A')

@subcommand.command()
def hellob():
    print('Hello B')

def main():
    subcommand()

if __name__ == '__main__': main()
