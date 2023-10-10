import requests
from bs4 import BeautifulSoup

response = requests.get("https://g1.globo.com")

content = response.content

site = BeautifulSoup(content, "html.parser")

noticias = site.find_all('div', attrs={'class':'feed-post-body'})

for noticia in noticias:
    titulo = noticia.find('a', attrs={'class':'feed-post-link'})
    print(titulo.text)