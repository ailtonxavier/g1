import requests
from bs4 import BeautifulSoup
from datahora import data, hora
from time import sleep
from conecction import *
from auth import *

def g1():
    return BeautifulSoup(requests.get("https://g1.globo.com").content, 'html.parser')

def encontra_links(g1):
    links = []
    for link in g1.find_all('a', attrs={'class':'feed-post-link'}):
        if link.get('href') != None: 
            links.append(link.get('href'))
    return links

def listagem_de_titulos(links):
    titulos = []
    for link in links:
        titulo = (BeautifulSoup(requests.get(links[links.index(link)]).content, 'html.parser')).find('h1', attrs={'class':'content-head__title'})
        if titulo != None: 
            titulos.append(titulo.text)
    return titulos


criar_sqlite3()

while 1 != 2:

    # links = encontra_links(g1())

    # titulos = listagem_de_titulos(links)


    # links = encontra_links(g1())

    # titulos = listagem_de_titulos(links)

    # titulo = ", ".join(titulos)

    titulo = ''
    inserir_sqlite3(titulo, hora(), data())
    listar_sqlite3()
    sleep(5)
