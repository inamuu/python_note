# coding: utf-8

import slackweb

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
slack_webhook_url = os.environ.get("slack_webhook_url")

def main():
    slack = slackweb.Slack(url="コピーしたWebhookのURL")
    slack.notify(text="pythonからslackさんへ")

if __name__ == '__main__': main()
