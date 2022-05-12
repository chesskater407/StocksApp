


from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
import requests

import html.parser

pd.set_option('display.max_columns', 1000)  # or 1000
pd.set_option('display.max_rows', 1000)  # or 1000
pd.set_option('display.max_colwidth', 199)  # or 199





r = requests.get("https://api.scrapingdog.com/scrape?api_key=61b050f099abf37c9f44c0df&url=https://finance.yahoo.com/quote/AMZN/history?period1=863654400&period2=1638921600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true").text
soup = BeautifulSoup(r,"html.parser")
df = pd.read_html(str(soup), flavor="bs4")



date_MN = pd.read_html(r, match='Date')
open_MN = pd.read_html(r, match='Open')
print (date_MN)
print (open_MN)
