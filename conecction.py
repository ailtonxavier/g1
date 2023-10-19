import sqlite3

def local_banco():
    return 'database.db'

def criar_sqlite3():
    conexao = sqlite3.connect(local_banco())
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS noticias (noticia TEXT, hora TEXT, data TEXT);')
    conexao.close()

def inserir_sqlite3(noticia, hora, data):
    conexao = sqlite3.connect(local_banco())
    cursor = conexao.cursor()
    cursor.execute(f'insert into noticias values("{noticia}","{hora}","{data}")')
    sqlite3.connect(local_banco()).commit()
    conexao.close()
    

def listar_sqlite3():
    conexao = sqlite3.connect(local_banco())
    cursor = conexao.cursor()
    cursor.execute("select * from noticias")
    print(cursor.fetchall())
    conexao.commit()
    conexao.close()
