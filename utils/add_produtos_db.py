from core.olist_api.listar_produtos_olist import listar_produtos
import requests

url = "http://127.0.0.1:5000/produtos"

produtos = listar_produtos()

for i in produtos:

    json = {
        "preco": i['preco'],
        "nome": i['nome']
    }

    requests.post(url, json=json)