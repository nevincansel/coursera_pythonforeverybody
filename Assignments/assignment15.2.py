import sqlite3

conn = sqlite3.connect('orgDB.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts'''
)

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)'''
)

fname = input('Enter a file name: ')
file = open(fname)
for line in file:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    host = email.split('@')
    org = host[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))  
    row = cur.fetchone()    
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()



