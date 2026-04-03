import sqlite3

conn = sqlite3.connect('repertorio.db')
cursor = conn.cursor()
tabelas = ['filmes','series','livros']

for tabela in tabelas:
    cursor.execute(f"""
               CREATE TABLE IF NOT EXISTS {tabela} (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome VARCHAR
               )
               """)
    conn.commit()