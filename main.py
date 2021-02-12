import requests
import json
url = 'https://www.metropoles.com/wp-json/metropoles/v1/last_news?&paged=1&category=182&limit=100'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
data = json.loads(result.content)

print(len(data))

for news in data:
    x = news['excerpt'].find("Segundo")
    if(x!=-1):
        print(news['url'])

