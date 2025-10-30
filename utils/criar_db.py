import sqlite3

db = sqlite3.connect("loja.db")

cur = db.cursor()
cur.execute("CREATE TABLE produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, preco REAL NOT NULL)")
cur.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, cpf_cnpj TEXT NOT NULL, tipo_pessoa TEXT NOT NULL, endereco TEXT NOT NULL, numero_casa INTEGER NOT NULL, bairro TEXT NOT NULL, cidade TEXT NOT NULL, uf TEXT NOT NULL, cep TEXT NOT NULL, email TEXT NOT NULL, fone TEXT NOT NULL, situacao TEXT NOT NULL)")

db.close()