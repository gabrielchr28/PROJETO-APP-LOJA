from core.produto.produto_repository import ProdutoRepository
from core.produto.produto import Produto

class ProdutoService:
    def __init__(self):
        self.repository = ProdutoRepository()

    def adicionar(self, produto: Produto):
        self.repository.adicionar(produto)