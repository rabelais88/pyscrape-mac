import requests
import lxml.html
from settings import target_url


def main():
  """
  Crawler main
  """
  session = requests.Session()
  response = session.get(target_url)
  urls = scrape_list_page(response)
  for elUrl in urls:
    print(elUrl)


def scrape_list_page(res):
  # this function returns generator
  root = lxml.html.fromstring(res.content)
  # .cssselect(@selector) can create a generator with appropriate selector
  root.make_links_absolute(res.url)
  for a in root.cssselect('.view_box .book_tit a'):
    url = a.get('href')
    yield url

if __name__ == '__main__':
  main()
