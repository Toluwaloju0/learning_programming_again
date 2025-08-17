import MySQLdb
import sys

if __name__ == "__main__":
    uname, pword, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    cursor = MySQLdb.connect(user=uname, password=pword, database=dbname).cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    for city in cursor.fetchall():
        print(city)
