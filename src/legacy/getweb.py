import re
import sys
from urllib.request import urlopen


def gethtml(url):
  # urlopen treats return value as file type
  f = urlopen(url)
  bytes_content = f.read()
  scanned_text = bytes_content[:1024].decode('ascii', errors='replace')
  match = re.search(r'charset=["\']?([\w-]+)', scanned_text)

  if match:
    encoding = match.group(1)
  else:
    encoding = 'utf-8'

  print('encoding:', encoding, file=sys.stderr)
  return bytes_content.decode(encoding)


def getxss(url):
  # get encoding from HTTP header, not HTML
  f = urlopen(url)

  encoding = f.info().get_content_charset(failobj="utf-8")
  # print('encoding:', encoding, file=sys.stderr)
  return f.read().decode(encoding)
