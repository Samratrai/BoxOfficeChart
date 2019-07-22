# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:21:00 2019

@author: dell
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
pd.set_option('display.max_columns',15)
pd.set_option('display.max_rows',100)
xmasbo_raw = requests.get('https://www.the-numbers.com/box-office-chart/daily/2018/12/25').text
xmasbo_html = BeautifulSoup(xmasbo_raw,'html.parser')
xmasbo_table = xmasbo_html.find_all('table')
xsmasbo_table1 = xmasbo_table[1].find_all('tr')
#Shows Value 0
#print(xsmasbo_table1[0])

#Shows value 1
#print(xsmasbo_table1[1])

#Shows all the contents in a list of value 1
#print(xsmasbo_table1[1].contents)

#Returns Only Values no other things
#print(xsmasbo_table1[1].text)

#Returns the Proper list Values
#print(xsmasbo_table1[1].text.split('\n')) 

cleaned_xsmasbo_row = []
for row in xsmasbo_table1[1:]:
    cleaned_row = row.text.split('\n')
    cleaned_xsmasbo_row.append(cleaned_row)
#print(cleaned_xsmasbo_row[:10])    

xsmasbo_df = pd.DataFrame(cleaned_xsmasbo_row)
#print(xsmasbo_df.head(10))

xsmasbo_df = xsmasbo_df.drop(columns = [0,11])
xsmasbo_df.columns = ['Rank','LastRank','Movie','Distributor','Gross','Change',
                      'Theatre','Per Theater','TotalGross','Days']
print(xsmasbo_df)

#xsmasbo_df.to_csv(r'''D:\xsmasbo.csv''')
    