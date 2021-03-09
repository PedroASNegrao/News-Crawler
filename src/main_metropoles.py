import requests
import csv
import json
import sys
import numpy as np
import re
from bs4 import BeautifulSoup
import pandas as pd

i = 0

final = 355
final_data = []

links_array = []
title_array = []
date_array = []

for index in range(1, final):
    url = ('https://www.metropoles.com/wp-json/metropoles/v1/last_news?&paged=%d&category=140&limit=12' % index)
    #url = ('https://www.metropoles.com/wp-json/metropoles/v1/last_news?&paged=1&category=140&limit=12')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    data = result.content

    json_news = json.loads(data)

    print(len(json_news))

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


    #print(links_array)
    #print(title_array)
    #print(date_array)

    #for title in soup.find_all({'class':'box-text'}):
        #print(title)

    #print(index)


columns = ['url', 'title', 'date']
index_data = [i for i in range(0, len(links_array))]
aux = np.array([links_array, title_array, date_array])
df = pd.DataFrame({'url': links_array, 'title': title_array, 'date': date_array})
#print(df)
df.to_csv('Data/news_metropoles.csv', sep=',', index=False, encoding='utf-8')

    #https://www.correiobraziliense.com.br/



#print(result_title)




