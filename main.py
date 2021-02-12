import requests
import csv
import json
import sys
import numpy as np

url = 'https://www.metropoles.com/wp-json/metropoles/v1/last_news?&paged=1&category=182&limit=10000'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
data = json.loads(result.content)

i = (len(data))
j = 0
final_data = []
print(data[90]['url'])

with open('news.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for news in data:
        #x = news['excerpt'].find("Preso")
        #if(x!=-1):
        #    final_data.append(news['url'])
        result = news.items()

        news_array = list(result)

        an_array = np.array(news_array)

        writer.writerow([an_array])
        print("Loading: ", j, " out of: ", i)
        j = j + 1

print(type(news))
print("Finded: ", len(final_data))

