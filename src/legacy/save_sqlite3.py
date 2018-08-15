# sqlite3 is basic python package(only on windows)
# on Ubuntu, sudo apt-get install -y sqlite3

import sqlite3
import random
conn = sqlite3.connect('top_cities.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS cities')

c.execute('''
CREATE TABLE cities (
  rank integer,
  city text,
  population integer
)
''')

c.execute('INSERT INTO cities VALUES (?, ?, ?)', (1, 'testcity', 304040))
c.execute('INSERT INTO cities VALUES (:rank, :city, :population)', {'rank': 2, 'city': 'testcity2', 'population': 4559})

rndgen = lambda min, max: random.randint(min, max)
cities = ['incheon', 'seoul', 'busan', 'bucheon', 'jeonnam']
rowsdata = list(map(lambda x: {'rank': x, 'city': cities[x], 'population': rndgen(100, 50000)}, range(3, 5)))

print(rowsdata)
c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)', rowsdata)

conn.commit()

c.execute('SELECT * FROM cities')

for row in c.fetchall():
  print(row)

conn.close()