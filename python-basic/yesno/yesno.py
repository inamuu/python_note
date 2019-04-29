# coding=utf8

def main():
    while True:
        choice = input('please input [y/n]: ').lower()
        if choice == ['y']:
            print('yes!')
            return True
        elif choice in ['n', 'no']:
            print('No!')
            return False

if __name__ == '__main__': main()