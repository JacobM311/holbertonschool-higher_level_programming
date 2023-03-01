#!/usr/bin/python3
"""This script displays the table where it matches arg
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user="%s" % sys.argv[1],
                           passwd="%s" % sys.argv[2],
                           db="%s" % sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE \
        states.name LIKE BINARY %(state)s ORDER BY id ASC;",
                {'state': sys.argv[4]})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
