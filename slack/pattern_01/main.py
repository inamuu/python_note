# coding: utf-8

import os
import slackweb

slack_webhook_url = os.environ["slack_webhook_url"]

def main():
    slack = slackweb.Slack(url=slack_webhook_url)
    slack.notify(text="This is test notify")

if __name__ == '__main__': main()
