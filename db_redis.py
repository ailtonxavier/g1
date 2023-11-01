import redis
import datahora


def read():
    with redis.Redis(host='redis',port=6379,decode_responses=True) as connection:
        return connection.hgetall('g1:session')


def update(titulos):
    hora = datahora.hora()
    data = datahora.data()
    with redis.Redis(host='redis',port=6379,decode_responses=True) as connection:
        connection.hset('g1:session', mapping={
            "titulos": (f"{titulos}"),
            "data": (f"{data}"),
            "hora": (f"{hora}"),
        })