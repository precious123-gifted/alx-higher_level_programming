#!/usr/bin/python3
'''print all cities from db'''

import MySQLdb
import sys


def list_all():
    '''lists all cities from db'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities' +
                ' INNER JOIN states ON cities.state_id = states.id' +
                ' ORDER BY cities.id ASC;')
    result = cur.fetchall()
    cur.close()
    db.close()

    if result:
        for row in result:
            print(row)


if __name__ == '__main__':
    list_all()
