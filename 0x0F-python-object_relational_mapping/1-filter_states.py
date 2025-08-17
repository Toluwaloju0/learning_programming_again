import MySQLdb
import sys

if __name__ == "__main__":
    uname = sys.argv[1]
    pword = sys.argv[2]
    dbname = sys.argv[3]

    cursor = MySQLdb.connect(user=uname, password=pword, database=dbname).cursor()

    dbname = sys.argv[3]
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for state in cursor.fetchall():
        print(state)
