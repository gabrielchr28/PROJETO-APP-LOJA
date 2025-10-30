import requests
from token_key.token_api import TOKEN
URL = "https://api.tiny.com.br/api2/contatos.pesquisa.php"
FORMATO = "JSON"

def listar_clientes():
    pagina = 1
    todos_clientes = []

    while True:
        payload = {
            "token": TOKEN,
            "formato": FORMATO,
            "pagina": pagina
        }

        response = requests.post(URL, data=payload)
        data = response.json()

        if data.get('retorno', {}).get('status') == "Erro":
            break

        clientes = data.get('retorno', {}).get('contatos', [])
        if not clientes:
            print("erro")
            break

        for i in clientes:
            cliente = i.get('contato', {})
            todos_clientes.append(cliente)

        pagina += 1

    return todos_clientes
    
if __name__ == "__main__":
    clientes = listar_clientes()
    for n, i in enumerate(clientes):
        print(f"{n}: ", i['nome'], " - ", i['cidade'])