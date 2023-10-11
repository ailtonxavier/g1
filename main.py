import requests
from bs4 import BeautifulSoup
from time import sleep

while 1 != 2:
    request = requests.get("https://g1.globo.com").content
    soup = BeautifulSoup(request, 'html.parser')
    links = []
    titulos = []

    for link in soup.find_all('a', attrs={'class':'feed-post-link'}):
        # adicionando o link das paginas na lista de links
        links.append(link.get('href'))

    aux = 0
    for link in links:
        request2 = requests.get(links[aux]).content
        soup2 = BeautifulSoup(request2, 'html.parser')
        titulo = soup2.find('h1', attrs={'class':'content-head__title'})
        if titulo != None: print(titulo.text)
        aux += 1
    print()
    sleep(3)
