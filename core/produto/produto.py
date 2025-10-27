class Produto:
    def __init__(self, nome="SEM NOME", preco=0, id=0):
        self.__nome = nome
        self.__preco = preco
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco

    @property
    def id(self):
        return self.__id