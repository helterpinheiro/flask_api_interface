from flask import Flask
from controller.pessoa_controller import pessoa

app = Flask(__name__)

# Registrando o Blueprint pessoa
app.register_blueprint(pessoa)

if __name__ == '__main__':
    app.run(debug=True)