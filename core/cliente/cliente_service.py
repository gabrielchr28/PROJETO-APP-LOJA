from core.cliente.cliente_repository import ClienteRepository
from core.cliente.cliente import Cliente

class ClienteService:
    def __init__(self):
        self.repository = ClienteRepository()

    def listar(self):
        return self.repository.listar()

    def adicionar(self, cliente: Cliente):
        return self.repository.adicionar(cliente)

    def remover(self, id):
        cliente = self.repository.remover(id)
        if cliente:
            return {
                "id": id,
                "removido": True
            }
        else:
            return {
                "id": id,
                "removido": False
            }