import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
import sqlite3
from conecction import *


banco = 'database.db'
conexao = sqlite3.connect(banco)
cursor = conexao.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS noticias (noticia TEXT, hora TEXT, data TEXT);')
conexao.close()

def autenticacao():
    pass

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

def data():
    return datetime.today().strftime("%d/%m/%y")
def hora():# cursor
    return datetime.now().strftime("%H:%M:%S")

while 1 != 2:

    links = encontra_links(g1())

    titulos = listagem_de_titulos(links)


    try:
        links = encontra_links(g1())

        titulos = listagem_de_titulos(links)

        titulo = ", ".join(titulos)

   
        criar_sqlite3()
        inserir_sqlite3(titulo, hora(), data())
        listar_sqlite3()
        # conexao = sqlite3.connect(banco)
        # cursor = conexao.cursor()
        # cursor.execute(f'insert into noticias values("{titulo}","{data_e_hora_atual[0]}","{data_e_hora_atual[1]}")')
        # sqlite3.connect(banco).commit()
        # cursor.execute("select * from noticias")
        # print(cursor.fetchall())
        # conexao.commit()
        # conexao.close()

    except sqlite3.Error as error:
        print(error)


    
    sleep(3)
