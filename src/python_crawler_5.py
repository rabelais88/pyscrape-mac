import requests
import re
import lxml.html
from python_crawler_4 import main

"""
this module does the exact same job as ./python_crawler_4.py
but the difference is that this module extracts data into dict type
"""

def scrape_detail_page(res):
  root = lxml.html.fromstring(res.content)
  ebook = {
    'url': res.url,
    'title': root.cssselect('.store_product_info'),
    'price': root.cssselect('.pbr strong')[0].text_content(),
    'content': [normalize_spaces(p.text_content())
      for p in root.cssselect('#tabs_3 .hanbit_edit_view p')
      if normalize_spaces(p.text_content()) != '']
  }
  return ebook

def normalize_spaces(s):
  return re.sub(r'\s+', ' ', s).strip()

if __name__ == '__main__':
  main()
