import requests
import lxml.html
from settings import target_url


def main():
  session = requests.Session()
  response = session.get(target_url)
  urls = scrape_list_page(response)
  for elUrl in urls:
    response = session.get(elUrl)
    ebook = scrape_detail_page(response)
    print(ebook)
    break  # just for testing...print out only 1 line out of the whole list


def scrape_list_page(res):
  root = lxml.html.fromstring(res.content)
  root.make_links_absolute(res.url)
  for a in root.cssselect('.view_box .book_tit a'):
    url = a.get('href')
    yield url


def scrape_detail_page(res):
  """
  get the book info from response, using dict
  """
  root = lxml.html.fromstring(res.content)
  ebook = {
    'url': res.url,
    'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
    'price': root.cssselect('.pbr strong')[0].text_content(),
    'content': [p.text_content()\
      for p in root.cssselect('#tabs_3 .hanbit_edit_view p')]
  }
  return ebook

if __name__ == '__main__':
  main()