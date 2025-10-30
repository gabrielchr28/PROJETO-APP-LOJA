import requests
from token_key.token_api import TOKEN

URL = "https://api.tiny.com.br/api2/produtos.pesquisa.php"
FORMATO = "JSON"


def listar_produtos():
    pagina = 1
    todos_produtos = []

    while True:
        payload = {
            "token": TOKEN,
            "formato": FORMATO,
            "pagina": pagina
        }

        response = requests.post(URL, data=payload)
        data = response.json()


        if data.get("retorno", {}).get("status_processamento") == "erro":
            print("Erro:", data["retorno"].get("erros"))
            break

        produtos = data.get("retorno", {}).get("produtos", [])
        if not produtos:
            break

        
        for p in produtos:
            produto = p.get("produto", {})
            todos_produtos.append(produto)


        pagina += 1

    return todos_produtos


if __name__ == "__main__":
    produtos = listar_produtos()

    for p in produtos:
       print(f" - Produto: {p['nome']} - Preço: {p['preco']}")
