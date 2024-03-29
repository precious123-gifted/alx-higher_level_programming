#!/usr/bin/python3
'''script to list all cities passed as argument'''

import MySQLdb
import sys


def list_by_state():
    '''lists all cities of a state passed as argument to the script'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute('SELECT cities.name FROM cities' +
                ' INNER JOIN states ON cities.state_id = states.id' +
                ' WHERE CAST(states.name AS BINARY) = %s' +
                ' ORDER BY cities.id ASC;',
                [state_name])
    result = cur.fetchall()
    cur.close()
    db.close()

    print(', '.join(map(lambda x: x[0], result)))


if __name__ == '__main__':
    list_by_state()
