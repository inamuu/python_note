# coding=utf8

def main():
    while True:
        choice = raw_input('please input [y/n] ')
        if choice in ['y', 'yes']:
            print('yes!')
            return True
        elif choice in ['n', 'no']:
            print('No!')
            return False

if __name__ == '__main__': main()