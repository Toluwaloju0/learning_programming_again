#!/usr/bin/env python3

import MySQLdb
import sys

if __name__ == "__main__":
    uname, pword, dbname, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    cursor = MySQLdb.connect(user=uname, password=pword, database=dbname).cursor()

    cursor.execute(f"SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name LIKE '{state}'")

    cities = cursor.fetchall()
    for a in range(len(cities)):
        if a != len(cities) - 1:
            print("{}, ".format(cities[a][0]), end="")
        else:
            print("{}".format(cities[a][0]), end="")
    print("")
