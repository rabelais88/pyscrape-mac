import json
import random

rndgen = lambda min, max: str(random.randint(min, max))
cities = ['incheon', 'seoul', 'busan', 'bucheon', 'jeonnam']
rowsdata = list(map(lambda x: {'rank': x, 'city': cities[x], 'population': rndgen(100, 50000)}, range(5)))
with open('top_cities.json', 'w') as f:
  json.dump(rowsdata, f)

with open('top_cities.json', 'r') as f:
  print(f.read())