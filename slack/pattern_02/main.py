# conding: utf-8

import os
import requests


def main():
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer {0}".format(os.environ.get("SlackBotToken"))
    }
    params = {
        "token": os.environ.get("SLACK_VERIFY_TOKEN"),
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