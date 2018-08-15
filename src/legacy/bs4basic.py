from bs4 import BeautifulSoup
import requests

r = requests.get('http://hanbit.co.kr')
"""
beautifulsoup 4 parsers

html.parser - standard html parser
xml - quick parser
lxml-xml - faster xml parser
html5lib - html5 style parser
"""
soup = BeautifulSoup(r.text, 'xml')
print('h1 element :' + str(soup.h1))
print('type of this element: ' + str(type(soup.h1)))
print('name : ' + soup.h1.name)
print('parent of this element: ')
print(soup.h1.parent)

"""
list all <li> elements
soup.find_all('li')
"""
print('printing all <a> elements')
allLinks = map(lambda x: x.text, soup.find_all('a'))
allLinks = filter(lambda x: x != '', allLinks)
print(list(allLinks))

for link in soup.find_all('a'):
  if(link != ''):
    print(link.text)