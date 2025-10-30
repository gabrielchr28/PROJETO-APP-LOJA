from core.olist_api.listar_clientes_olist import listar_clientes
import requests

clientes = listar_clientes()

url = "http://127.0.0.1:5000/clientes"

for i in clientes:

    json = {
        "nome": i['nome'],
        "cpf_cnpj": i['cpf_cnpj'],
        "tipo_pessoa": i['tipo_pessoa'],
        "endereco": i['endereco'],
        "numero_casa": i['numero'],
        "bairro": i['bairro'],
        "cidade": i['cidade'],
        "uf": i['uf'],
        "cep": i['cep'],
        "email": i['email'],
        "fone": i['fone'],
        "situacao": i['situacao']    
    }

    requests.post(url, json=json)