# coding=utf8

def main():
    while True:
        choice = raw_input('please input [y/n]')
        if choice == 'y':
            print('yes')
            return True
        elif choice == 'n':
            print('no')
            return True

if __name__ == '__main__': main()