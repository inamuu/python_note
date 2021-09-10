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
    }
]

def hiera_list(list_a: list):
    print(key)


def main():
    data = list(map(hiera_list, list_a))
    return data

if __name__ == '__main__': main()
