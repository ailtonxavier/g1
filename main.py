import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

while 1 != 2:
    data_atual = datetime.now().strftime("%H:%M:%S")
    hora_atual = datetime.today().strftime("%d/%m/%y")
    request = requests.get("https://g1.globo.com").content
    soup = BeautifulSoup(request, 'html.parser')
    links = []
    titulos = []
    data_base = []

    for link in soup.find_all('a', attrs={'class':'feed-post-link'}):
        # adicionando o link das paginas na lista de links e evitando exceção em caso de retorno None do link
        if link.get('href') != None: 
            links.append(link.get('href'))

    for link in links:
        request2 = requests.get(links[links.index(link)]).content
        soup2 = BeautifulSoup(request2, 'html.parser')
        titulo = soup2.find('h1', attrs={'class':'content-head__title'})
        if titulo != None: 
            titulos.append(titulo.text)
    
    lista = [titulos, data_atual, hora_atual]
    data_base.append(lista)
    print()
    print(data_base)
    sleep(3)

"""
1 - autenticar
2 - popular o banco
2.1 (Título das notícias, data, hora)
3 - plotar em graph
"""