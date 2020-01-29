# coding: utf-8

import os
import sys
import mysql.connector

DBUSER = os.environ['user']
DBPASS = os.environ['passwd']
DBHOST = os.environ['host']
DBPORT = os.environ['port']
DBNAME = os.environ['db']

def main():
    try:
        conn = mysql.connector.connect(
            user = DBUSER,
            passwd = DBPASS,
            host = DBHOST,
            port = DBPORT,
            database = DBNAME,
            connect_timeout=30
        )
        print('connection ok')
        cur = conn.cursor()
        cur.close()
        conn.close()
    except Exception as e:
        print(e)

if __name__ == '__main__': main()
