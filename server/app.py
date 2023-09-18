from flask import Flask
from controller.pessoa_controller import pessoa
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Registrando o Blueprint pessoa
app.register_blueprint(pessoa)


if __name__ == '__main__':
    app.run(debug=True)