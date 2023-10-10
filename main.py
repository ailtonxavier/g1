import requests
from bs4 import BeautifulSoup
import time


i = 0
while i != 1:
    response = requests.get("https://g1.globo.com")

    content = response.content

    site = BeautifulSoup(content, "html.parser")

    noticias = site.find_all('div', attrs={'class':'feed-post-body'})
    links = []
    conteudo_bd = []
    for noticia in noticias:
        titulo = (noticia.find('a', attrs={'class':'feed-post-link'}))
        links += [titulo.get('href')]
        
    for link in links:
        request_lista = requests.get(link).text
        titulo_sub_link = (request_lista.find('a', attrs={'class':'feed-post-link'}))
        
        conteudo_bd.append(request_lista)

    print(conteudo_bd)
    time.sleep(5)