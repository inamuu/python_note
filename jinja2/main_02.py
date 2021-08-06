# coding: utf-8

import json
from jinja2 import Template

def main():

    json_file_open = open('event.json', 'r')
    json_data = json.load(json_file_open)
    print(json_data['last_name'])

    #template_json = open('templates/slack.json.j2', 'r')
    #template_data = json.load(template_json)
    template_data = "氏名: {{first_name}} {{last_name}}"

    template = Template(template_data)
    payload = template.render(json_data)
    print(payload)

if __name__ == '__main__': main()
