#!/usr/bin/python3
"""This script lists cities and states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user="%s" % sys.argv[1],
                           passwd="%s" % sys.argv[2],
                           db="%s" % sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities,\
        states WHERE cities.state_id = states.id ORDER BY cities.id;")
    query_rows = cur.fetchall()

    result = ""

    for row in query_rows:
        if row[2] == sys.argv[4]:
            result += "{}, ".format(row[1])
    result_strip = result[:-2]
    print(result_strip)
    cur.close()
    conn.close()
