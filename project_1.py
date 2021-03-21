#!/usr/bin/env python
# coding: utf-8

#import the required libraries & modules
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd 

#To get the web page in soup page format
r=requests.get("https://keithgalli.github.io/web-scraping/webpage.html",verify=False)
soup=bs(r.content)

#To get the table column names
table_stats=soup.select("table.hockey-stats")[0]
col=table_stats.find('thead').find_all('th')
coulmn_names=[c.string for c in col]
coulmn_names

#To get the table data
tr=table_stats.find("tbody").find_all("tr")
l=[]
for loop1 in tr:
    td=loop1.find_all('td')
    out=[str(loop2.get_text()).strip() for loop2 in td]
    l.append(out)
output=pd.DataFrame(l,columns=coulmn_names)
output

