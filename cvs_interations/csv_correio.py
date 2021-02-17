import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

correio_data = pd.read_csv('./../Data/news_correio.csv')

data_array = correio_data.to_numpy()

all_links = []
words_finded = []
i = 0
objeto = []
#print(data_array)

#Palaras para serem pesquisadas:
words = ["Polícia", "Policiais", "Policial", "Bandido", "Bandida", "Bandidos", "Criminoso", "Criminosa", "Criminosos", "Vítima", "Vítimas", "Crime", "Crimes", "Lei", "Legislação", "Penal", "Penais", "Contravenção", "Contravenções", "Infrações", "Infração", "Infrator", "Infratora", "Infratores", "Contraventor", "Contraventora", "Contraventores", "Advogado", "Advogada", "Advogados", "Juiz", "Juiza" ,"Juízo", "Ministério Público", "MP", "Delegacia", "Boletim de ocorrência", "Testemunhas", "Testemunha", "Testemunhou", "Tribunal", "Justiça", "DP"]
low_case_words = []

for word in words:
    low_case_words.append(word.lower())

words = words + low_case_words

#----------------

#url_test = ['https://www.correiobraziliense.com.br/cidades-df/2021/02/4907151-gdf-vai-construir-viaduto-para-facilitar-acesso-a-vicente-pires.html','https://www.correiobraziliense.com.br/cidades-df/2021/02/4907151-gdf-vai-construir-viaduto-para-facilitar-acesso-a-vicente-pires.html', 'https://www.correiobraziliense.com.br/cidades-df/2021/02/4907152-policia-militar-prende-dois-homens-em-flagrante-de-estupro-no-paranoa.html']

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
    objeto.clear()

    for paragrafs in soup.find_all('p'):
        text = str(paragrafs.string)
        cont_paragrafo = cont_paragrafo + 1
        print("Checando paragrafo: %d" % cont_paragrafo)
        #print(text)
        for parameter in words:
            if text.find(parameter) != -1:
                #print(text)
                required = True
                objeto.append(parameter)

    words_finded.append(objeto)
    if(required == True):
        all_links.append(url)
        required = False



print(all_links)
print(words_finded)

df = pd.DataFrame({'url': all_links, 'palavras-encontradas': words_finded})
#print(df)
df.to_excel('./../Excel/news_correio2.xls', index=False, encoding='utf-8')
#print(type(soup.p.string))
#print(soup.p.string)
#aux = soup.p.string
#print(aux.find("governo"))

#correio_data.to_excel('./../Excel/news_correio2.xls', index=False, encoding='utf-8')
