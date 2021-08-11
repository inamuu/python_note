# coding: utf-8

import json
from jinja2 import Template

import os

def main():

    """入力データ"""
    json_file_open = open(os.path.dirname(__file__) + '/event.json', 'r')
    json_data = json.load(json_file_open)

    """出力用テンプレート"""
    template_data = "氏名: {{first_name}} {{last_name}}"

    template = Template(template_data)
    payload = template.render(json_data)
    print(payload)

if __name__ == '__main__': main()
