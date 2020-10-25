import sqlite3

conn = sqlite3.connect('AgesDB.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Ages'''
)

cur.execute('''
CREATE TABLE Ages (name VARCHAR(128), age INTEGER)'''
)

cur.execute('DELETE FROM Ages;')
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Claire', 28);''')
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Angelika', 16);''')
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Rosalin', 25);''')
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Danys', 13);''')
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Faith', 39);''')

sqlstr = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X'

for row in cur.execute(sqlstr):
    print(row[0])

cur.close()