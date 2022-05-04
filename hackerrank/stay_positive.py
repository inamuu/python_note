# coding: utf-8

def minStart(arr):
    x = 5
    i = 0
    while i <= len(arr):
        r1 = arr[i] + x
        r2 = r1 + arr[i + 1]
        r3 = r2 + arr[i + 2]
        print(r1)
        print(r2)
        print(r3)
        i = i + 1


if __name__ == '__main__':
    l = [3, -6, 5, -2, 1]
    minStart(l)
