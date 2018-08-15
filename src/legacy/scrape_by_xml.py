import lxml.html
from getweb import gethtml

rawhtml = gethtml('http://hanbit.co.kr/store/books/full_book_list.html')

# notice the difference!!
# most xml parsers support url/file direct parsing ( .parse() )
# but if just a plain text is used, use .fromstring()
# return value of direct parsing from URL/file ---> need to state getroot()
# return value of text parsing ---> no need to state getroot()
html = lxml.html.fromstring(rawhtml)

for a in html.cssselect('a'):
  print(a.get('href'), a.text)