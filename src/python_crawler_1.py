import requests
import lxml.html
from settings import target_url

r = requests.get(target_url)
root = lxml.html.fromstring(r.content)

for a in root.cssselect('.view_box a'):
  url = a.get('href')
  print(url)
