import customtkinter as ctk
from core.produto.produto_service import ProdutoService
from core.produto.produto import Produto

produto_service = ProdutoService()

def adicionar():
    produto = nome.get()
    preco_p = preco.get()
    try:
        preco_p = float(preco_p)
    except:
        return
    else:
        produto_service.adicionar(Produto(produto, preco_p))

app = ctk.CTk()
app.title("Cadastrar Produto")
app.geometry("375x700")
app._set_appearance_mode("dark")

# ENTRY
txt_nome = ctk.CTkLabel(app, text="Nome")
txt_nome.grid(padx=10, pady=(10, 0), column=0, row=0, stick="w")

nome = ctk.CTkEntry(app, placeholder_text="Nome Produto", width=350, border_color="gray", border_width=1)
nome.grid(padx=10, pady=(1, 10), column=0, row=1, stick="w")

# TAREFA
txt_preco = ctk.CTkLabel(app, text="Preço")
txt_preco.grid(padx=10, pady=(10, 0), column=0, row=2, stick="w")

preco = ctk.CTkEntry(app, placeholder_text="Preço do Produto", width=350, border_color="gray", border_width=1)
preco.grid(padx=10, pady=(1, 10), column=0, row=3, stick="w")

# BOTÕES
btao_canc = ctk.CTkButton(app, text="Cancelar", width=350, border_color="black", border_width=1, fg_color="transparent")
btao_canc.grid(padx=10, pady=10, column=0, row=5, stick="w")

btao_add = ctk.CTkButton(app, text="Adicionar Produto", width=350, border_color="black", border_width=1, command=adicionar)
btao_add.grid(padx=10, pady=10, column=0, row=4, stick="w")

app.mainloop()