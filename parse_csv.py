import pandas as pd
import numpy as np
import re

# Read csv

metropoles_data = pd.read_csv('./Data/news_metropoles_old.csv')

data_array = metropoles_data.to_numpy()

old_links_array = []
links_array = []
old_title_array = []
title_array = []
date_array = []

print(data_array[0])

for lines in data_array:
    if lines[5].startswith("https"):
        links_array.append(lines[5])
        old_title_array.append(lines[2])
        date_array.append(lines[3])

#print(links_array)
for linha_titulo in old_title_array:
    if linha_titulo.find(',') != -1:
        aux = linha_titulo.replace(',', '')
    else:
        aux = linha_titulo
    title_array.append(aux)
        #print("ACHOU")

for linha_titulo2 in title_array:
    if linha_titulo2.find(',') != -1:
        print(linha_titulo2.find(','))
        print(linha_titulo2)
        print("|---------------|")

columns = ['url', 'title', 'date']

index_data = [i for i in range(0, len(links_array))]

aux = np.array([links_array, title_array, date_array])

df = pd.DataFrame({'url': links_array, 'title': title_array, 'date': date_array})

df.to_csv('./Data/news_metropoles.csv', sep=',', index=False, encoding='utf-8')


# Parse csv

# Write new csv

