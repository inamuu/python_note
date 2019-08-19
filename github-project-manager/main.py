# coding: utf-8

import os, sys
import click
from os.path import join, dirname
from dotenv import load_dotenv
from github import Github

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
g = Github(os.environ.get("github_access_token"))

@click.group()
def subcommand():
    pass

@subcommand.command(help='リポジトリ一覧')
def repos():
    for repo in g.get_user().get_repos():
        print(repo.name)

@subcommand.command(help='オーガニゼーション')
def orgsrepos():
    for repo in g.get_organization(os.environ.get("github_orgs")).get_repos():
        print(repo.name)

@subcommand.command(help='projects')
def projects():
    for repo in g.get_user().get_project(1640570):
        print(repo.name)

def main():
    subcommand()

if __name__ == '__main__': main()
