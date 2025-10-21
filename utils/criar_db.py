import sqlite3

db = sqlite3.connect("perfumatch.db")

cur = db.cursor()
cur.execute("CREATE TABLE produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, preco REAL NOT NULL)")

db.close()