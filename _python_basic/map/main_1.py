# cofing: uft-8

list_a: list = [
    'りんご',
    'バナナ',
    'キウイ'
]

def hiera_list(list_a):
    val = list_a + 'はうまい'
    return val


def main():
    data = list(map(hiera_list, list_a))
    return data

if __name__ == '__main__': main()
