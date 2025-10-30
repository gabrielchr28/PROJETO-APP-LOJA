class Cliente:
    def __init__(self, nome="SEM NOME", id=0, cpf_cnpj="", tipo_pessoa="F", endereco="", numero_casa=0, bairro="", cidade="", uf="", cep="", email="", fone="", situacao="A"):
        self.__id = id
        self.__nome = nome
        self.__cpf_cnpj = cpf_cnpj
        self.__tipo = tipo_pessoa
        self.__endereco = endereco
        self.__numero = numero_casa
        self.__bairro = bairro
        self.__cidade = cidade
        self.__uf = uf
        self.__cep = cep
        self.__email = email
        self.__fone = fone
        self.__situacao = situacao

    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def cpf_cnpj(self):
        return self.__cpf_cnpj
    @cpf_cnpj.setter
    def cpf_cnpj(self, novo_cpf_cnpj):
        self.__cpf_cnpj = novo_cpf_cnpj

    @property
    def tipo_pessoa(self):
        return self.__tipo
    @tipo_pessoa.setter 
    def tipo_pessoa(self, novo_tipo):
        self.__tipo = novo_tipo

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @property
    def numero_casa(self):
        return self.__numero
    @numero_casa.setter
    def numero_casa(self, novo_numero):
        self.__numero = novo_numero

    @property
    def bairro(self):
        return self.__bairro
    @bairro.setter
    def bairro(self, novo_bairro):
        self.__bairro = novo_bairro

    @property
    def cidade(self):
        return self.__cidade
    @cidade.setter
    def cidade(self, nova_cidade):
        self.__cidade = nova_cidade

    @property
    def uf(self):
        return self.__uf
    @uf.setter
    def uf(self, nova_uf):
        self.__uf = nova_uf

    @property
    def cep(self):
        return self.__cep
    @cep.setter
    def cep(self, novo_cep):
        self.__cep = novo_cep

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, novo_email):
        self.__email = novo_email

    @property
    def fone(self):
        return self.__fone
    @fone.setter
    def fone(self, novo_fone):
        self.__fone = novo_fone

    @property
    def situacao(self):
        return self.__situacao
    @situacao.setter
    def situacao(self, nova_situacao):
        self.__situacao = nova_situacao
