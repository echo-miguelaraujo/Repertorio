import sqlite3

conn = sqlite3.connect('repertorio.db')
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS series (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
               )
               """)
conn.commit()