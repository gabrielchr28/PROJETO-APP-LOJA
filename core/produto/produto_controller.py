from flask import Blueprint, request, jsonify
from core.produto.produto import Produto
from core.produto.produto_service import ProdutoService

service = ProdutoService()

controller = Blueprint('produto', __name__, url_prefix="/produtos")

@controller.route('/', methods=['GET'])
def listar():
    return service.listar()

@controller.route('/', methods=['POST'])
def adicionar():
    dados = request.get_json()
    obj = Produto(nome=dados['nome'], preco=dados['preco'], id=0)
    produto = service.adicionar(obj)
    return jsonify(produto)

@controller.route('/<int:id>', methods=['DELETE'])
def remover(id):
    sucesso = service.remover(id)
    return jsonify(sucesso)