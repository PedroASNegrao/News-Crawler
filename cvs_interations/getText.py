import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

url =('https://www.correiobraziliense.com.br/politica/2021/02/4907689-conselho-de-etica-vai-analisar-processo-contra-daniel-silveira-na-terca.html')
#url = ('https://www.metropoles.com/brasil/convite-a-israelenses-cria-crise-diplomatica-com-comunidade-arabe-na-unb')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
try:
    result = requests.get(url, headers=headers, timeout=5)
except requests.Timeout:
    print('The request timed out')
data = result.content
#data_string1 = str(data.decode("iso8859-1"))
data_string = str(data.decode(encoding="utf-8", errors='replace'))
soup = BeautifulSoup(data_string, "lxml")

text_array = []
cont_paragrafo = 0

for paragrafs in soup.find_all("article", class_="article"): #Correio
#for paragrafs in soup.find_all("article", class_="m-content"): #Metropoles
    text = str(paragrafs)
    if text.find('tradição') != -1:
        print("OK")
    text_array.append(text)
    cont_paragrafo = cont_paragrafo + 1
    print("Correio--Checando paragrafo: %d" % cont_paragrafo)

print(text_array)