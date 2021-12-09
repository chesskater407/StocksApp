from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
import requests


r = requests.get("https://api.scrapingdog.com/scrape?api_key=61b050f099abf37c9f44c0df&url=https://finance.yahoo.com/quote/AMZN/history?period1=863654400&period2=1638921600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true").text
soup = BeautifulSoup(r,'HTMLparser')

table=soup.findAll('table')

rows=soup.findAll('tr')

columns=soup.findAll('td')

date_MN = pd.read_html(r, match='Date')



#Data Selector


    '''
    class LinksParser(HTMLParser.HTMLParser):
  def __init__(self):
    HTMLParser.HTMLParser.__init__(self)
    self.recording = 0
    self.data = []

  def handle_starttag(self, tag, attributes):
    if tag != 'div':
      return
    if self.recording:
      self.recording += 1
      return
    for name, value in attributes:
      if name == 'id' and value == 'remository':
        break
    else:
      return
    self.recording = 1

  def handle_endtag(self, tag):
    if tag == 'div' and self.recording:
      self.recording -= 1

  def handle_data(self, data):
    if self.recording:
      self.data.append(data)