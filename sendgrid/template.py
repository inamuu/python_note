# coding: utf-8

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

MAILFROM=os.environ['MAILFROM']
MAILTO=os.environ['MAILTO']

def main():
    {
        "to": [
            MAILTO,
        ],
        "sub": {
            ":name": [
                "Alice",
                "Bob"
            ],
            ":price": [
                "$4",
                "$4"
            ]
        },
        "category": [
            "Promotions"
        ],
        "filters": {
            "templates": {
                "settings": {
                    "enable": 1,
                    "template_id": "60414495-6787-441b-8b08-3979499bba7a"
                }
            }
        }
    }
    mail = Mail()

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_APIKEY'))
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

if __name__ == '__main__': main()
