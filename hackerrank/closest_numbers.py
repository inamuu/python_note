# coding: utf-8

def closestNumbers(numbers):
    l = sorted(numbers, reverse=True)
    i = 0
    while i <= len(numbers):
        item = i + 1
        result = int(l[i]) - int(l[item])
        print(result)
        if i == 3:
            break
        else:
            i = i + 1


if __name__ == '__main__':
    l = [6, 2, 4, 10]
    closestNumbers(l)
