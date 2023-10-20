import sqlite3

def local_banco():
    return 'database.db'

def criar_sqlite3():
    try:
        banco = sqlite3.connect(local_banco())
        cursor = banco.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS NOTICIAS(noticia text, hora text, data text);')
        banco.close()
    except sqlite3.Error as error:
        print(error)

def inserir_sqlite3(noticia, hora, data):
    try:
        banco = sqlite3.connect(local_banco())
        cursor = banco.cursor()
        cursor.execute(f'INSERT INTO NOTICIAS VALUES("ailton","{hora}","{data}");')
        banco.commit()
        banco.close()
    except sqlite3.Error as error:
        print(error)
    

def listar_sqlite3():
    try:
        banco = sqlite3.connect(local_banco())
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM NOTICIAS")
        print(cursor.fetchall())
        banco.commit()
        banco.close()
    except sqlite3.Error as error:
        print(error)