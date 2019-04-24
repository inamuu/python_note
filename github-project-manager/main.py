# coding: utf-8

import os, sys
from os.path import join, dirname
from dotenv import load_dotenv
from github import Github

def main():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    g = Github(os.environ.get("github_access_token"))
    print(g)

if __name__ == '__main__': main()
