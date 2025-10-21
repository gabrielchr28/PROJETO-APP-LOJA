import sqlite3
from core.produto.produto import Produto
class ProdutoRepository:
    def __init__(self):
        self.nome_db = "perfumatch.db"

    def conectar(self):
        return sqlite3.connect(self.nome_db)
    
    def adicionar(self, produto: Produto):
        db = self.conectar()

        cur = db.cursor()
        cur.execute("INSERT INTO produtos (nome, preco) VALUES(?, ?)", (produto.nome, produto.preco))
        db.commit()
        db.close()