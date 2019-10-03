# coding: utf-8

import os

"""
参考URL
https://qiita.com/zaburo/items/0ba12417dfb39fcb1555#%E7%A9%BA%E3%81%98%E3%82%83%E3%81%AA%E3%81%84%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%82%92%E5%86%8D%E5%B8%B0%E7%9A%84%E3%81%AB%E5%89%8A%E9%99%A4
"""

def main():
    path = 'work_id.pos'
    if os.path.isfile(path) is False:
        f = open(path, 'w')
        f.write('0\n')
        f.close()
        return

    """
    上書き
    """
    #f = open('work_id.txt', 'w')
    #f.write('test1\ntest2\n')
    #f.close()

    """
    読み取り 
    """
    #f = open('work_id.txt', 'r')
    #for row in f:
    #    print(row.strip())
    #f.close()

    """
    読み取り（wオプションで）
    """
    f = open(path, 'r')
    for row in f:
        print(row)
        work_id_pos = row.strip()
    work_id_pos2 = int(work_id_pos) + 1
    f = open(path, 'w')
    f.write(str(work_id_pos2))
    f.close()

    f = open(path, 'r')
    for row in f:
        print(row)
        work_id_pos = row.strip()
    f.close()

if __name__ == '__main__': main()
