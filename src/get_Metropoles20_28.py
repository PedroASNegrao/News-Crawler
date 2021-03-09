import requests
import csv
import json
import sys
import numpy as np
import re
from bs4 import BeautifulSoup
import pandas as pd
import datetime

i = 0

final = 70
final_data = []

links_array = []
title_array = []
date_array = []

for index in range(30, final):
    url = ('https://www.metropoles.com/wp-json/metropoles/v1/last_news?&paged=%d&category=140&limit=12' % index)
    #url = ('https://www.metropoles.com/wp-json/metropoles/v1/last_news?&paged=1&category=140&limit=12')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    data = result.content

    json_news = json.loads(data)

    #print(json_news)
    date = json_news[0]["date"]
    #print(date)
    day = int(date[0] + date[1])
    month = int(date[3] + date[4])
    year = int(date[6] + date[7] + date[8] + date[9])

    date = datetime.datetime(year, month, day)
    date1 = datetime.datetime(2021, 2, 20)
    date2 = datetime.datetime(2021, 2, 28)

    if date > date2:
        continue
    elif (date <= date2) and (date > date1):
        for news_object in json_news:
            links_array.append(news_object['url'])
            if news_object['title'].find(',') != -1:
                aux = news_object['title'].replace(',', '')
            else:
                aux = news_object['title']
            title_array.append(aux)
            date_array.append(news_object['date'])
            i = i + 1
            print(i)
    elif(date < date1):
        break




columns = ['url', 'title', 'date']
index_data = [i for i in range(0, len(links_array))]
aux = np.array([links_array, title_array, date_array])
df = pd.DataFrame({'url': links_array, 'title': title_array, 'date': date_array})
#print(df)
df.to_csv('./../Data/news_metropoles_20_28.csv', sep=',', index=False, encoding='utf-8')

    #https://www.correiobraziliense.com.br/



#print(result_title)




