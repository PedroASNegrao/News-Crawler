import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

correio_data = pd.read_csv('./../Data/news_correio.csv')

data_array = correio_data.to_numpy()

all_links = []
all_dates = []
words_finded = []
i = 0
objeto = []
#print(data_array)

#Palaras para serem pesquisadas:
words = [" Polícia ", " Policiais ", " Policial ", " Bandido ", " Bandida ", " Bandidos ", " Criminoso ", " Criminosa ", " Criminosos ", " Vítima ", " Vítimas ", " Crime ", " Crimes ", " Penal ", " Penais ", " Contravenção ", " Contravenções ", " Infrações ", " Infração ", " Infrator ", " Infratora ", " Infratores ", " Contraventor ", " Contraventora ", " Contraventores ", " Delegacia ", " Boletim de ocorrência ", " Testemunhas ", " Testemunha ", " Testemunhou ", " Tribunal ", " DP ", " Preso ", " Presa ", " Presos ", " Assalto ", " Assaltante ", " Assaltantes ", " Ladra ", " Ladrão ", " Ladrões ", " Roubo ", " Rouba ", " Agressão ", " Agressor ", " Agressora ", " Estupro ", " Estuprador ", " Estupradora ", " Feminicídio ", " Feminicida ", " Morte ", " Morto ", " Morre ", " Morreu ", " Faleceu ", " Falece ", " Falecimento ", " Homicídio ", " Homicida ", " Assassino ", " Assassina ", " Assassinos ", " Traficante ", " Traficantes ", " Tráfico ", " Drogas ", " Droga ", " Arma ", " Armas ", " Incêndio ", " Incendiou ", " Incendiar ", " PCDF ", " PMDF "]
low_case_words = []

for word in words:
    low_case_words.append(word.lower())

words = words + low_case_words

#----------------

url_test = ['https://www.correiobraziliense.com.br/cidades-df/2021/02/4905821-familiares-velam-corpo-de-menina-que-morreu-em-acidente-na-br-070.html','https://www.correiobraziliense.com.br/cidades-df/2021/02/4907163-terceiro-envolvido-na-morte-de-estudante-em-planaltina-se-entrega.html','https://www.correiobraziliense.com.br/cidades-df/2021/02/4907151-gdf-vai-construir-viaduto-para-facilitar-acesso-a-vicente-pires.html', 'https://www.correiobraziliense.com.br/cidades-df/2021/02/4907152-policia-militar-prende-dois-homens-em-flagrante-de-estupro-no-paranoa.html']

#for link in url_test:
for link in data_array:
    i = i + 1
    print("Link: %d" % i)
    #url = link
    url = (link[0])
    #url = ('https://www.correiobraziliense.com.br/cidades-df/2021/02/4907151-gdf-vai-construir-viaduto-para-facilitar-acesso-a-vicente-pires.html')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    data = result.content
    data_string = str(data.decode("latin-1"))
    soup = BeautifulSoup(data_string, "lxml")

    #print(soup)

    required = False
    cont_paragrafo = 0


    for paragrafs in soup.find_all(attrs={"class": "texto"}):
        text = str(paragrafs.string)
        cont_paragrafo = cont_paragrafo + 1
        print("Checando paragrafo: %d" % cont_paragrafo)
        #print(text)
        #
        for parameter in words:
            if text.find(parameter) != -1:
                #print(text)
                print("OK")
                required = True
                objeto.append(parameter)

    if(required == True):
        words_finded.append(objeto)
        objeto = []
        all_links.append(url)
        all_dates.append(link[2])
        required = False






print(all_links)
print(words_finded)

df = pd.DataFrame({'url': all_links, 'palavras-encontradas': words_finded, 'data': all_dates})
#print(df)
df.to_excel('./../Excel/news_correio3.xls', index=False, encoding='utf-8')
#print(type(soup.p.string))
#print(soup.p.string)
#aux = soup.p.string
#print(aux.find("governo"))

#correio_data.to_excel('./../Excel/news_correio2.xls', index=False, encoding='utf-8')
