# cofing: uft-8

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
        "DATA": {
            "type": "TYPED",
            "value": {
                "id": 123,
                "value": "hoge"
            }
        }
    }
]

<<<<<<< Updated upstream

def hiera_list(list_a: dict):
    flatten_list = {}
    for k, v in list_a.items():
        key = k.lower()
        val = v['value']
        flatten_list[key] = val
    return flatten_list
=======
def hiera_list(list_a: dict):
    key = list_a.
    value = list_a.values()
    return key, value
>>>>>>> Stashed changes


def main():
    data = list(map(hiera_list, list_a))
    return data


if __name__ == '__main__':
    main()
