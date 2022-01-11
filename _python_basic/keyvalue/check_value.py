# coding: utf-8

def main():
    test_data = {
        "name": "Test Taro",
        "tel": "090-1234-5678",
        "age": "30",
        "sex": "male",
        "address": ""
    }

    mapping_data = [
        "name",
        "tel",
        "age",
        "sex",
        "address"
    ]

    for k, v in test_data.items():
        if v != "":
            print(k + " : " + v)
        else:
            print(k + " : None")


if __name__ == '__main__':
    main()
