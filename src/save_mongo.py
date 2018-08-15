import lxml.html
from pymongo import MongoClient
tree = lxml.html.parse('full_book_list.html')
html = tree.getroot()

client = MongoClient('localhost', 27017)  # default setting is localhost:27017 -> can be omitted
db = client.scraping  # connect to db named 'scraping'
collection = db.links  # reaching collection named 'links' under 'scraping'
collection.delete_many({})  # intialize by removing all existing elements

for a in html.cssselect('a'):
  collection.insert_one({
    'url': a.get('href'),
    'title': a.text,  # text.strip() has gone away for newest lxml.html
  })

for link in collection.find().sort('_id'):
  print(link['_id'], link['url'], link['title'])
