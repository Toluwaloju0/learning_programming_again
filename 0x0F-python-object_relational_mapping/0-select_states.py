import MySQLdb
import sys

if __name__ == "__main__":
    UName = sys.argv[1]
    PWord = sys.argv[2]
    DBname = sys.argv[3]

    db = MySQLdb.connect(database=DBname, user=UName, password=PWord)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    for state in cursor.fetchall():
        print(state)
