# conding: utf-8

import os
import requests

from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def main():
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
    }
    params = {
        "token": os.environ.get("SlackBotToken"),
        "channel": "CCPRGV8E7",
        "text": "test",
    }

    req = requests.post(
        url,
        headers=headers,
        params=params
    )
    print(req.text)

if __name__ == '__main__': main()