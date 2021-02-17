import requests
import csv
import json
import sys
import numpy as np
import re
from bs4 import BeautifulSoup
import pandas as pd


i = 0

final = 3
final_data = []

#Create the csv file
#with open('Data/news_correio.csv', 'w', newline='', encoding='utf-8') as file:
    #writer = csv.writer(file)
links_array = []
title_array = []
date_array = []

for index in range(1, final):
    url = ('https://www.correiobraziliense.com.br/webparts/1/1/%d/' % index)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    data = result.content

    data_string = str(data.decode("utf-8"))

    soup = BeautifulSoup(data_string, "lxml")

    for link in soup.find_all('a'):
        #print(link.get('href'))
        links_array.append("https://www.correiobraziliense.com.br%s" % link.get('href'))

        #writer.writerow([final_data])
    for title in soup.find_all('h2'):
        title_array.append(title.string)
        #final_data_title = title.string
        #writer.writerow([final_data_title])
    for date in soup.find_all('small'):
        parse_date = date.string
        parse_date = re.sub("postado em ", "", parse_date)
        date_array.append(parse_date)

    #print(links_array)
    #print(title_array)
    #print(date_array)

    #for title in soup.find_all({'class':'box-text'}):
        #print(title)

    #print(index)

columns = ['url', 'title', 'date']

#aux = np.array([[links_array], [title_array], [date_array]])
index_data = [i for i in range(0, len(links_array))]
#print(index_data)

aux = np.array([links_array, title_array, date_array])

df = pd.DataFrame({'url': links_array, 'title': title_array, 'date': date_array})
print(df)

    #https://www.correiobraziliense.com.br/

#print(result_title)




