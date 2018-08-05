import requests
import lxml.html
from settings import target_url

response = requests.get(target_url)
root = lxml.html.fromstring(response.content)
root.make_links_absolute(response.url)

for a in root.cssselect('.view_box .book_tit a'):
  url = a.get('href')
  print(url)
