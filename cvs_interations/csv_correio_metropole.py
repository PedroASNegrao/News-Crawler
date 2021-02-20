import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time

def main():
    print("TESTE")
    #Palaras para serem pesquisadas:
    words = []
    lowcase_lista = []
    lista = open("./../Lista/list.txt", "r", encoding='utf-8')

    for line in lista:
        aux = line.replace('\n', '')
        #aux = aux + ' '
        words.append(aux)

    for params in words:
        low = params.lower()
        #low = ' ' + low + ' '
        lowcase_lista.append(low)

    words = words + lowcase_lista

    inicio_correio = time.time()
    #excel_correios(words)
    fim_correio = time.time()
    tempo_correio = (fim_correio - inicio_correio)/60

    inicio_metropoles = time.time()
    excel_metropoles(words)
    fim_metropoles = time.time()
    tempo_metropoles = (fim_metropoles - inicio_metropoles)/60


    print("Tempo de execução pro Correio foi: %d" % tempo_correio)
    print("Tempo de execução pro Metropoles foi: %d" % tempo_metropoles)
    print("Tempo Total: %d" % (tempo_correio + tempo_metropoles))

    #----------------

def excel_metropoles(words):

    print("entrou")

    metropoles_data = pd.read_csv('./../Data/news_metropoles.csv')

    data_array = metropoles_data.to_numpy()

    all_links = []
    all_dates = []
    all_titles = []
    words_finded = []
    i = 0
    objeto = []
    #print(data_array)

    url_test = ['https://www.metropoles.com/distrito-federal/pcdf-prende-falso-policial-que-sequestrava-e-extorquia-traficantes']

    #for link in url_test:
    for link in data_array:
        i = i + 1
        print("Link: %d" % i)
        #url = link
        url = (link[0])
        #url = ('https://www.metropoles.com/distrito-federal/pcdf-prende-falso-policial-que-sequestrava-e-extorquia-traficantes')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        try:
            result = requests.get(url, headers=headers, timeout=5)
        except requests.Timeout:
            print('The request timed out')
            continue
        data = result.content
        data_string = str(data.decode(encoding="utf-8", errors='replace'))
        soup = BeautifulSoup(data_string, "lxml")

        #print(soup)

        required = False
        required2 = False
        cont_paragrafo = 0


        for paragrafs in soup.find_all("article", class_="m-content"):
            text = str(paragrafs)
            #cont_paragrafo = cont_paragrafo + 1
            #print("Metropoles--Checando paragrafo: %d" % cont_paragrafo)
            #print(text)
            #
            #debug1 = 0
            for parameter in words:
                #print(debug1)
                #debug1 = 1 + debug1
                if text.find(parameter) != -1:
                    init = text.find(parameter)
                    end = init + len(parameter)
                    if end < len(text):
                        if not text[end].isalpha():
                            required = True
                        else:
                            required = False
                    else:
                        required = True

                    if init != 0:
                        if not text[init - 1].isalpha():
                            required2 = True
                        else:
                            required2 = False
                    else:
                        required2 = True

                    if required and required2:
                        print("OK")
                        objeto.append(parameter)

        if objeto:
            words_finded.append(objeto)
            objeto = []
            all_links.append(url)
            all_dates.append(link[2])
            all_titles.append(link[1])
            required = False
            required2 = False


    #print(all_links)
    #print(words_finded)
    #print(all_dates)

    df = pd.DataFrame({'Data': all_dates, 'Titulo': all_titles, 'url': all_links, 'palavras-encontradas': words_finded})
    #print(df)
    df.to_excel('./../Excel/news_metropoles_excel2.xlsx', index=False, encoding='utf-8')

def excel_correios(words):

    print("entrou")

    correio_data = pd.read_csv('./../Data/news_correio.csv')

    data_array = correio_data.to_numpy()

    all_links = []
    all_dates = []
    words_finded = []
    all_titles = []
    i = 0
    objeto = []
    #print(data_array)

    #url_test = ['https://www.correiobraziliense.com.br/cidades-df/2021/02/4905821-familiares-velam-corpo-de-menina-que-morreu-em-acidente-na-br-070.html','https://www.correiobraziliense.com.br/cidades-df/2021/02/4907163-terceiro-envolvido-na-morte-de-estudante-em-planaltina-se-entrega.html','https://www.correiobraziliense.com.br/cidades-df/2021/02/4907151-gdf-vai-construir-viaduto-para-facilitar-acesso-a-vicente-pires.html', 'https://www.correiobraziliense.com.br/cidades-df/2021/02/4907152-policia-militar-prende-dois-homens-em-flagrante-de-estupro-no-paranoa.html']

    #for link in url_test:
    for link in data_array:
        i = i + 1
        print("Link: %d" % i)
        #url = link
        url = (link[0])
        #url = ('https://www.correiobraziliense.com.br/cidades-df/2021/02/4907151-gdf-vai-construir-viaduto-para-facilitar-acesso-a-vicente-pires.html')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        try:
            result = requests.get(url, headers=headers, timeout=5)
        except requests.Timeout:
            print('The request timed out')
            continue
        data = result.content
        data_string = str(data.decode(encoding="utf-8", errors='replace'))
        soup = BeautifulSoup(data_string, "lxml")

        #print(soup)

        required = False
        required2 = False
        cont_paragrafo = 0


        for paragrafs in soup.find_all("article", class_="article"):
            text = str(paragrafs)
            #cont_paragrafo = cont_paragrafo + 1
            #print("Correio--Checando paragrafo: %d" % cont_paragrafo)
            #print(text)
            #
            for parameter in words:
                if text.find(parameter) != -1:
                    init = text.find(parameter)
                    end = init + len(parameter)
                    if end < len(text):
                        if not text[end].isalpha():
                            required = True
                        else:
                            required = False
                    else:
                        required = True

                    if init != 0:
                        if not text[init - 1].isalpha():
                            required2 = True
                        else:
                            required2 = False
                    else:
                        required2 = True

                    if required and required2:
                        print("OK")
                        objeto.append(parameter)

        if objeto:
            words_finded.append(objeto)
            objeto = []
            all_links.append(url)
            all_dates.append(link[2])
            all_titles.append(link[1])
            required = False
            required2 = False


    df = pd.DataFrame({'Data': all_dates, 'Titulo': all_titles, 'url': all_links, 'palavras-encontradas': words_finded})
    #print(df)
    df.to_excel('./../Excel/news_correio_excel2.xlsx', index=False, encoding="utf-8")

if __name__ == "__main__":
    main()