# coding: utf=8

dataA = {
    "tableA": "apple",
    "tableB": "banana",
    "tableC": "orange"
}


def main():
    dataB = 'tableB'
    if dataB in dataA:
        print(dataA[dataB])


if __name__ == '__main__':
    main()
