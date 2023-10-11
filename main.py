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

    for link in links:
        request2 = requests.get(links[links.index(link)]).content
        soup2 = BeautifulSoup(request2, 'html.parser')
        titulo = soup2.find('h1', attrs={'class':'content-head__title'})
        if titulo != None: 
            print(titulo.text)
            titulos.append(titulo.text)
    
    print(titulos)
    print()
    sleep(3)
