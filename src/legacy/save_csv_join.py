import random
import csv

genrnd = lambda min, max: str(random.randint(min, max))
print('rank,city,population')
cities = ['shanghai', 'karachi', 'beijing', 'shenzhen', 'tianjin']
rows = []

for idx, city in enumerate(cities):
  rowdata = [idx, city, genrnd(100, 20000)]
  print(','.join([str(rowdata[0]), rowdata[1], str(rowdata[2])]))
  rows.append(rowdata)

# write in a file format
with open('top_cities.csv', 'w', newline='', encoding='utf-8-sig') as f:
  writer = csv.writer(f)
  # first row
  writer.writerow(['rank', 'city', 'population'])

  for row in rows:
    writer.writerow(row)