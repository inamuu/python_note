# coding: utf-8

import os, sys
from os.path import join, dirname
from dotenv import load_dotenv
from github import Github

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
g = Github(os.environ.get("github_access_token"))

def repos():
    for repo in g.get_user().get_repos():
        print(repo.name)

def orgsrepos():
    for repo in g.get_organization(os.environ.get("github_orgs")).get_repos():
        print(repo.name)

def main(args):
    if args == 'repos':
        repos()
    elif args == 'orgsrepos':
        orgsrepos()
    else:
        print('そんな関数ないよ')
        return

if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
