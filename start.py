import urllib.request
from _ast import Is

from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site =site

    def scrape(self):
        r=urllib.request.urlopen(self.site)
        html=r.read()
        parser="html.parser"
        sp = BeautifulSoup(html, parser)

new = Scraper("https://news.google.ru/")
new.scrape()