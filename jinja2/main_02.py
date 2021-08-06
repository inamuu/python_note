# coding: utf-8

import json
from jinja2 import Environment, FileSystemLoader, Template

def main():

    json_file_open = open('event_02.json', 'r')
    json_data = json.load(json_file_open)

    env = Environment(loader = FileSystemLoader('./templates'))
    template = env.get_template('slack.json.j2')

    payload = template.render(json_data)
    print(payload)

if __name__ == '__main__': main()
