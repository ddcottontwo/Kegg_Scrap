#lib import
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#url set & ping
url = 'https://www.genome.jp/dbget-bin/www_bget?sce:YKL127W+sce:YMR105C+sce:YMR278W'
response = requests.get(url)
