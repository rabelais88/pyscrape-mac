# the user has to modify header by him/herself to use cache
# header setup routine for cache is very complex by its nature,
# but this time the script uses external library 
import requests
# pip install CacheControl
from cachecontrol import CacheControl
target_url = 'https://docs.python.org/3'

session = requests.session()
cached_session = CacheControl(session)

response = cached_session.get(target_url)
print('is it cached?', response.from_cache)

response = cached_session.get(target_url)
print('is it cached?', response.from_cache)