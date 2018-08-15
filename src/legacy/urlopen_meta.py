# getting decoded html text using meta tag

import re
import sys
from urllib.request import urlopen

f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

bytes_content = f.read()

scanned_text = bytes_content[:1024].decode('ascii', errors='replace')

match = re.search(r'charset=["\']?([\w-]+)', scanned_text)

if match:
  encoding = match.group(1)
else:
  encoding = 'utf-8'

print('encoding:', encoding, file=sys.stderr)

text = bytes_content.decode(encoding)

print(text)
