# coding: utf-8

import os, sys
from os.path import join, dirname
from dotenv import load_dotenv
from github import Github

def main():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    g = Github(os.environ.get("github_access_token"))

    for repo in g.get_user().get_repos():
        print(repo.name)

if __name__ == '__main__': main()
