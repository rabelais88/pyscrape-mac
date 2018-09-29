import requests
from retrying import retry # pip install retrying

"""
this code does the exactly same thing with ./error_handling.py
the difference is that this code utilizes external library called 'retrying'
"""

TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)
TEST_URL = 'http://httpbin.org/status/200,404,503'
MAX_RETRY = 3

def main():
  response = fetch(TEST_URL)
  if 200 <= response.status_code < 300:
    print('Success!')
  else:
    print('error!')

@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000)
def fetch(targetUrl):
  print('Retrieving {0}...'.format(targetUrl))
  response = requests.get(targetUrl)
  print('Status: {0}'.format(response.status_code))
  if response.status_code not in TEMPORARY_ERROR_CODES:
    return response
  raise Exception('Temporary Error: {0}'.format(response.status_code))

if __name__ == '__main__':
  main()