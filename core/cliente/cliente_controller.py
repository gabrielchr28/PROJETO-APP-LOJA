from flask import Blueprint, request, jsonify
from core.cliente.cliente import Cliente
from core.cliente.cliente_service import ClienteService

service = ClienteService()

controller_cliente = Blueprint('cliente', __name__, url_prefix="/clientes")

@controller_cliente.route('/', methods=['GET'])
def listar():
    return service.listar()

@controller_cliente.route('/', methods=['POST'])
def adicionar():
    dados = request.get_json()
    obj = Cliente(nome=dados['nome'], bairro=dados['bairro'], cep=dados['cep'], cidade=dados['cidade'], cpf_cnpj=dados['cpf_cnpj'], email=dados['email'], endereco=dados['endereco'], fone=dados['fone'], numero_casa=dados['numero_casa'], situacao=dados['situacao'], tipo_pessoa=dados['tipo_pessoa'], uf=dados['uf'], id=0)
    produto = service.adicionar(obj)
    return jsonify(produto)

@controller_cliente.route('/<int:id>', methods=['DELETE'])
def remover(id):
    sucesso = service.remover(id)
    return jsonify(sucesso)