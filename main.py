from time import sleep
import links
import db_redis

i = 0
while 1 != 2:

    lista_de_links = links.encontra_links(links.g1())

    titulos = links.listagem_de_titulos(lista_de_links)

    titulo = ",".join(titulos)

    db_redis.update(titulo)
    print(db_redis.read())
    sleep(5)