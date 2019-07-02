# coding: utf-8

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

MAILFROM=os.environ['MAILFROM']
MAILTO=os.environ['MAILTO']

def main():
    mail = Mail()
    mail.from_email = Email(MAILFROM)
    mail.template_id = 'd-your-dynamic-template-uid'
    p = Personalization()
    p.add_to(Email('user@example.com'))
    p.dynamic_template_data = {
        'name': 'Bob',
        'balance': 42
    }
    mail.add_personalization(p)

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_APIKEY'))
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.mail)

if __name__ == '__main__': main()
