# coding: utf-8
​
import json
import os
import re
import requests

SENDGRID_GID = os.environ['SENDGRID_GID']
SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']

def add_contact_sendgrid(mail, firstname, lastname, tel, sex):
    '''
    w2_T department
    w4_T companyname
    '''
    headers = { 
        "Content-Type": "application/json",
        "Authorization": "Bearer " + SENDGRID_API_KEY
    }
    payload = {
        "list_ids": [ SENDGRID_GID ],
        "contacts": [ 
            {
                "email": mail,
                "first_name": firstname,
                "last_name": lastname,
                "custom_fields":
                    {
                        "w1_T": tel,
                        "w4_T": sex
                    }
            }     
        ]
    }
​
    ENDPOINT_URL = "https://api.sendgrid.com/v3/marketing/contacts"
    response = requests.put(ENDPOINT_URL, data=json.dumps(payload), headers=headers)    
    print(response)
    return response.status_code
