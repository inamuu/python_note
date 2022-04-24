# cofing: utf-8


def fizzBuzz(n):
    i = 0
    while i <= 15:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
        i = i + 1


if __name__ == '__main__':
    fizzBuzz(15)
