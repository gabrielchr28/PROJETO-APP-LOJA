from flask import Flask
from core.produto.produto_controller import controller
from core.cliente.cliente_controller import controller_cliente

app = Flask(__name__)

app.register_blueprint(controller)
app.register_blueprint(controller_cliente)

if __name__ == "__main__":
    app.run(debug=True)