# coding=utf-8

def main(args):
    print(args)
    for key, value in args.items():
        print("%s: %s" % (key, value))
    print(args['id'])
    print(args['name'])

if __name__ == '__main__':
    args = { 'id': '01', 'name': 'taro' }
    main(args)