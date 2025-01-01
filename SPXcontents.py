import pandas as pd
import requests
from io import BytesIO
import yfinance as yf
import os
import os.path
from urllib.parse import urlparse
from datetime import datetime, timezone, timedelta

SPY_url = "https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx"




# URL of the Wikipedia page
wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

# Read the tables on the Wikipedia page
tables = pd.read_html(wiki_url)

# The first table on the page contains the S&P 500 companies
sp500_table = tables[0]

print(sp500_table)
