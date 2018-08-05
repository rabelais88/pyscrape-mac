from urllib.parse import urljoin

# getting absolute url from relative url/path
base_url = 'http://example.com/books/top.html'
joined_url = urljoin(base_url, '//cdn.example.com/logo.png')
print(joined_url)
joined_url = urljoin(base_url, '/articles')
print(joined_url)