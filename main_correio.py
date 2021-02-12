import requests
import csv
import json
import sys
import numpy as np
import re

i = 0
contador = 1
final = 213
final_data = []

with open('news_correio.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for index in range(final):
        url = ('https://www.correiobraziliense.com.br/webparts/1/1/(%d)/' % contador)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        data = result.content

        data_string = str(data.decode("utf-8"))

        result_link = re.findall(r'<a href=.+?html', data_string)
        result_title = re.findall('<h2>.+?</h2>', data_string)

        final_data.append([])
        final_data[i].append(contador)
        final_data[i].append(result_link)
        final_data[i].append(result_title)

        writer.writerow([final_data])

        contador = contador + 1
        print(contador)

print(len(final_data))
#print(result_title)

