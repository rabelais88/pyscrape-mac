import time
import re
import requests
import lxml.html
from settings import target_url
from python_crawler_5 import scrape_detail_page
from python_crawler_4 import scrape_list_page

def main():
  session = requests.Session()
  res = session.get(target_url)
  urls = scrape_list_page(res)
  for url in urls:
    time.sleep(1)
    res = session.get(url)
    ebook = scrape_detail_page(res)
    print(ebook)

if __name__ == '__main__':
  main()