# coding: utf-8

import sys
import urllib
import random
import requests

def main():
    url = 'https://inamuu.com'
    with open('useragent.txt', "r") as f:
        useragent = [v.rstrip() for v in f.readlines()]

    r = urllib.request.Request(url)
    r.add_header('User-Agent', random.choice(useragent))
    urllib.request.urlopen(r)

if __name__ == '__main__': main()
