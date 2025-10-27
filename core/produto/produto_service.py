from core.produto.produto_repository import ProdutoRepository
from core.produto.produto import Produto

class ProdutoService:
    def __init__(self):
        self.repository = ProdutoRepository()

    def listar(self):
        return self.repository.listar()

    def adicionar(self, produto: Produto):
        return self.repository.adicionar(produto)

    def remover(self, id):
        produto = self.repository.remover(id)
        if produto:
            return {
                "id": id,
                "removido": True
            }
        else:
            return {
                "id": id,
                "removido": False
            }