import MySQLdb

conn = MySQLdb.connect(db='scraping', user='scraper', passwd='password', charset='utf8mb4')

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS cities')

c.execute('''
  CREATE TABLE cities (
    rank integer,
    city text,
    population integer
    )
''')

c.execute('INSERT INTO cities VALUES (%s, %s, %s)', (1, 'shanghai', 2415000))

c.execute('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',
  {'rank':2, 'city':'kharachi', 'population':2350000})

c.executemany('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',[
  {'rank':3,'city':'seoul','population':300000}
])

conn.commit()

c.execute('SELECT * FROM cities')

for row in c.fetchall():
  print(row)

conn.close()