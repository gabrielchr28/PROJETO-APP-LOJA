import sqlite3
from core.produto.produto import Produto
class ProdutoRepository:
    def __init__(self):
        self.nome_db = "perfumatch.db"

    def conectar(self):
        return sqlite3.connect(self.nome_db)
    
    def listar(self):
        db = self.conectar()

        cur = db.cursor()
        cur.execute("SELECT * FROM produtos")
        linhas = cur.fetchall()
        db.close()
        return [
            {
                "id": l[0],
                "nome": l[1],
                "preco": l[2]
            } for l in linhas
        ]
    
    def adicionar(self, produto: Produto):
        db = self.conectar()

        cur = db.cursor()
        cur.execute("INSERT INTO produtos (nome, preco) VALUES(?, ?)", (produto.nome, produto.preco))
        db.commit()
        novo_id = cur.lastrowid
        db.close()

        return {"id": novo_id, "nome": produto.nome, "preco": produto.preco}

    def remover(self, id):
        db = self.conectar()

        cur = db.cursor()
        cur.execute("DELETE FROM produtos WHERE id = ?;", (id,))
        db.commit()
        linhas = cur.rowcount
        db.close()
        return linhas > 0

