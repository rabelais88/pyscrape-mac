from xml.etree import ElementTree
from getweb import getxss
xmlcontent = getxss('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109')

# read this for more : https://docs.python.org/2/library/xml.etree.elementtree.html

tree = ElementTree.fromstring(xmlcontent)
# root = tree.getroot()  # get XML root

for item in tree.findall('channel/item/description/body/location/data'):
  tm_ef = item.find('tmEf').text
  tmn = item.find('tmn').text
  tmx = item.find('tmx').text
  wf = item.find('wf').text
  print(tm_ef, tmn, tmx, wf)
