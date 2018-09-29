import time
import requests

"""
this code separates temporary errors from permanent errors(such as 404)
permanent errors or success would finish the program but temporary errors will keep the program running
create error handling module in this fashion or use 'retrying' library
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

def fetch(targetUrl):
  retries = 0
  while True:
    try:
      print('Retrieving {0}...'.format(targetUrl))
      response = requests.get(targetUrl)
      print('Status: {0}'.format(response.status_code))
      if response.status_code not in TEMPORARY_ERROR_CODES:
        return response
    except requests.exceptions.RequestException as ex:
      print('Exception occurred: {0}'.format(ex))
      retries += 1
      if retries >= MAX_RETRY:
        raise Exception('Too many retries')
      wait = 2**(retries - 1)
      print('Waiting {0} seconds...'.format(wait))
      time.sleep(wait)

if __name__ == '__main__':
  main()
