import sqlite3
conn = sqlite3.connect('testDB.sqlite')
c = conn.cursor()
ids = [1, 2]
for i in ids:
    c.execute("SELECT * FROM people WHERE id = ?", (i,))
    print c.fetchone()
