import sqlite3
from core.cliente.cliente import Cliente
class ClienteRepository:
    def __init__(self):
        self.nome_db = "loja.db"

    def conectar(self):
        return sqlite3.connect(self.nome_db)
    
    def listar(self):
        db = self.conectar()

        cur = db.cursor()
        cur.execute("SELECT * FROM clientes")
        linhas = cur.fetchall()
        db.close()
        return [
            {
                "id": l[0],
                "nome": l[1],
                "preco": l[2]
            } for l in linhas
        ]
    
    def adicionar(self, cliente: Cliente):
        db = self.conectar()

        cur = db.cursor()
        cur.execute("INSERT INTO produtos (nome, cpf_cnpj, tipo_pessoa, endereco, numero_casa, bairro, cidade, uf, cep, email, fone, situacao) VALUES(?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (cliente.nome, cliente.cpf_cnpj, cliente.tipo_pessoa, cliente.endereco, cliente.numero_casa, cliente.bairro, cliente.cidade, cliente.uf, cliente.cep, cliente.email, cliente.fone, cliente.situacao))
        db.commit()
        novo_id = cur.lastrowid
        db.close()

        return {
                "id": novo_id,
                "nome": cliente.nome,
                "cpf_cnpj": cliente.cpf_cnpj,
                "tipo_pessoa": cliente.tipo_pessoa,
                "endereco": cliente.endereco,
                "numero_casa": cliente.numero_casa,
                "bairro": cliente.bairro,
                "cidade": cliente.cidade,
                "uf": cliente.uf,
                "cep": cliente.cep,
                "email": cliente.email,
                "fone": cliente.fone,
                "situacao": cliente.situacao
            }

    def remover(self, id):
        db = self.conectar()

        cur = db.cursor()
        cur.execute("DELETE FROM clientes WHERE id = ?;", (id,))
        db.commit()
        linhas = cur.rowcount
        db.close()
        return linhas > 0

