import scrapy
import requests
import json

url = 'https://www.metropoles.com/wp-json/metropoles/v1/last_news?&paged=1&category=182&limit=12'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
data = json.loads(result.content)

i = (len(data))
j = 0
final_data = []
text_to_analyse = ""
result = []
ind = 0

#print(data[0]['url'])

for news in data:
    x=1
    #x = news['excerpt'].find("Preso")
    if(x!=-1):
        final_data.append(news['url'])
    #print("Loading: ", j, " out of: ", i)
    j = j + 1

#print("Finded: ", len(final_data))

class ExampleSpider(scrapy.Spider):
    for index in data:
        name = 'example'
        allowed_domains = ['example.com']
        start_urls = [data[ind]['url']]
        #print("TEST")

        def parse(self, response):
            all_text = {}
            article_text = response.css("article")
            all_text['text'] = article_text.css("p::text").getall()
            print("TESTE NO FOR: ", all_text)
            # print("THIS IS THE TEXT FORMAT: ", str1.join(news_list["text"]))
            str1 = " "
            str2 = str1.join(all_text["text"])
            print("STRING1: ", all_text["text"])
            print("STRING2: ", str2)
            y = str2.find("declarou")
            if (y != -1):
                print("um")
                result.append(data[ind]['url'])
            print("RESULTADO: ", result)
            yield result




"""
for article in news:
        aux = article.css("div.m-box-text p.m-resume::text").extract_first()
        #x = aux.find('Felipe Cesarano')
        x = 1
        if (x != (-1)):
          data['descricao'] = article.css("div.m-box-text p.m-resume::text").extract_first()
          #link.append(article.css("a::attr(href)").extract_first())
          data['link'] = article.css("a::attr(href)").extract_first()
          if (article.css("div.m-box-text h6.m-title a::text").extract_first() == None):
            data['titulo'] = article.css("div.m-box-text h2.m-title a::text").extract_first()
            #titulo.append(article.css("div.m-box-text h2.m-title a::text").extract_first())
          else:
            data['titulo'] = article.css("div.m-box-text h6.m-title a::text").extract_first()
            #titulo.append(article.css("div.m-box-text h6.m-title a::text").extract_first())
          data['tema'] = article.css("div.m-box-text div.m-category-label a::text").extract_first()
          #tema.append(article.css("div.m-box-text div.m-category-label a::text").extract_first())
          i = i+1
          data['id_noticia'] = i
          final_data.append(data)
"""