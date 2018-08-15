# must 'pip install requests'
import requests

r = requests.get('http://hanbit.co.kr')
print(type(r))
res = {
  'statuscode': r.status_code,
  'headers': r.headers['content-type'],
  'encoding': r.encoding,
  'text': r.text
}
"""
r.content === tuple,
returns content in bytes type
"""
print(res)

"""
r.get()
r.post()
r.head()
r.delete()...

# all http requests can be sent using requests
r = requests.post('http://httpbin.org/post', data={'key1':'value1'})

# when http headers are used multiple times, use session object
s = request.Session()
s.headers.update({'user-agent':'my-crawler/1.0 (+foo@example.com)'})

# usage is identical to request
r = s.get('http://example.com')

"""
