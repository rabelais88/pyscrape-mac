import re
from html import unescape

import getweb
html = getweb.gethtml('http://www.hanbit.co.kr/store/books/full_book_list.html')

for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
  url = re.search(r'<a href="(.*?)">', partial_html).group(1)
  url = 'http://www.hanbit.co.kr' + url
  title = re.sub(r'<.*?>', '', partial_html)
  title = unescape(title)
  print('url:', url)
  print('title:', title)
  print('---')
