import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
import sqlite3


# conexao database
banco = 'database.db'
conexao = sqlite3.connect(banco)
connection = conexao.cursor()
connection.execute('CREATE TABLE IF NOT EXISTS noticias (noticia TEXT, hora TEXT, data TEXT);')
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

def data_e_hora():# cursor
    return [datetime.now().strftime("%H:%M:%S"), datetime.today().strftime("%d/%m/%y")]

while 1 != 2:

    links = encontra_links(g1())

    titulos = listagem_de_titulos(links)

    data_e_hora_atual = data_e_hora()

    try:
        links = encontra_links(g1())

        titulos = listagem_de_titulos(links)

        data_e_hora_atual = data_e_hora()

        titulo = ", ".join(titulos)

        # banco
        conexao = sqlite3.connect(banco)
        connection = conexao.cursor()
        connection = (sqlite3.connect(banco)).cursor()
        connection.execute(f'insert into noticias values("{titulo}","{data_e_hora_atual[0]}","{data_e_hora_atual[1]}")')
        sqlite3.connect(banco).commit()
        connection.execute("select * from noticias")
        print(connection.fetchall())
        conexao.close()
        
    except sqlite3.Error as error:
        print(error)


    
    sleep(3)
