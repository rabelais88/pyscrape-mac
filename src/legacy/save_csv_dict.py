import csv
import random

genrnd = lambda min, max: str(random.randint(min, max))
cities = ['shanghai', 'seoul', 'beijing', 'tianjin', 'shenzhen']
rowsdata = list(map(lambda x: {'rank': x, 'city': cities[x], 'population': genrnd(2000,10000)}, range(5)))

with open('top_cities.csv', 'w', newline='') as f:
  writer = csv.DictWriter(f, ['rank', 'city', 'population'])
  writer.writeheader()
  writer.writerows(rowsdata)

with open('top_cities.csv', 'r') as f:
  print(f.read())