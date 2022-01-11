# coding: utf-8

import sys


def main(args):
    test_data = {
        "name": "Test Taro",
        "tel": "090-1234-5678",
        "age": "30",
        "sex": "male",
        "address": args
    }

    if __check_value(test_data):
        return {"status_code": 200, "body": "success"}


def __check_value(test_data):
    """check each value if exists or not"""
    for k, v in test_data.items():
        if v != "":
            print(k + " : " + v)
        else:
            raise ValueError(k + " is None")
    return True


if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
