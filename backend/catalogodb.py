import sqlite3

conn = sqlite3.connect('repertorio.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR,
    status VARCHAR,
    streaming VARCHAR)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS series (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR,
    temp INTEGER,
    ep INTEGER,
    streaming VARCHAR)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS livros (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR,
    capitulo INTEGER)""")

conn.commit()