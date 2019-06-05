# coding: utf-8

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

MAILFROM=os.environ['MAILFROM']
MAILTO=os.environ['MAILTO']

def main():
    message = Mail(
        from_email=MAILFROM,
        to_emails=MAILTO,
        subject='Test from sendgrid',
        html_content='<strong>Test From Sendgrid</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_APIKEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

if __name__ == '__main__': main()
