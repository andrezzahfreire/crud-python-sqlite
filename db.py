import sqlite3
import os

def create_sqlite_database(filename):
    if os.path.exists(filename):
        return 
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            
def criar_conexao(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("Conexão estabelecida com o banco de dados")
        return conn
    except sqlite3.Error as e:
        print(e)
        return None


def fechar_conexao(conn):
    if conn:
        conn.close()
        print("Conexão com o banco de dados fechada")
