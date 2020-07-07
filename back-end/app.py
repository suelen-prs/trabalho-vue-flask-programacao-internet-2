from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import config
from banco import db
from blacklist import blacklist
from resource.marcas import marcas
from resource.carros import carros
from resource.funcionarios import funcionarios
from resource.propostas import propostas

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(carros)
app.register_blueprint(marcas)
app.register_blueprint(propostas)
app.register_blueprint(funcionarios)

@app.route('/')
def raiz():
    return '<h2>Revenda Herbie</h2>'

@app.route('/criadb')
def criadb():
    db.create_all()
    return '<h2>Tabelas do Banco de Dados Criadas</h2>'

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypeted_token):
    jti = decrypeted_token['jti']
    return jti in blacklist

if __name__ == '__main__':
    app.run(debug=True)