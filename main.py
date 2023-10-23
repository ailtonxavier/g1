import requests
from bs4 import BeautifulSoup
from datahora import data, hora
from time import sleep
from conecction import *
from auth import *
import links

criar_sqlite3() # se não existir criar, caso contrário 

while 1 != 2:

    lista_de_links = links.encontra_links(links.g1())

    titulos = links.listagem_de_titulos(lista_de_links)

    titulo = ", ".join(titulos)
    print(titulo)
    inserir_sqlite3(titulo, hora(), data())
    listar_sqlite3()
    sleep(5)