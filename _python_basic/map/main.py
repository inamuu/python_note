# coding: utf-8

list_a: list = [
    {
        "RECORD_NO": {
            "type": "RECORD_NUMBER",
            "value": "1"
        },
        "UPDATED_USER": {
            "type": "TYPEB",
            "value": {
                "code": "test@example.com",
                "name": "test_name"
            }
        },
        "REGION": {
            "type": "TYPEC",
            "value": [
                "null"
            ]
        },
    }
]


def hiera_list(dict_a: dict):
    dict_a_2 = {}
    for key, value in dict_a.items():
        if type(value['value']) == str:
            dict_a_2[str(key.lower())] = value['value']
        if type(value['value']) == list:
            dict_a_2[str(key.lower())] = value['value']
        if type(value['value']) == dict:
            for key2, value2 in value['value'].items():
                dict_a_2[str(key.lower()) + "_" + str(key2)] = value2
    return dict_a_2


def main():
    for dict_a in list_a:
        list_dict = hiera_list(dict_a)

    print(list_dict)


if __name__ == '__main__':
    main()
