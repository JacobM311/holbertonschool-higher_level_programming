#!/usr/bin/python3
"""This script grabs the username and password from user to print the table
"""
import MySQLdb
import sys

def select_states():
    """ List all states from database hbtn_0e_0_usa """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

if __name__=="__main__":
    select_states()