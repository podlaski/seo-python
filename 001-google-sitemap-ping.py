# The script pings Google about the sitemap. Add your sitemap to sitemap_url variable.
# Source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap

import urllib.request
from bs4 import BeautifulSoup

sitemap_url = 'https://your-domain.com/example-sitemap.xml' # add your sitemap
ping = 'https://www.google.com/ping?sitemap=' + sitemap_url
response = urllib.request.urlopen(ping)
soup = BeautifulSoup(response.read(), "html.parser")

print('\nSitemap URL:', sitemap_url)
print('Ping: ', ping)
print('Google Answer:', soup.find("body").text, '\n')
