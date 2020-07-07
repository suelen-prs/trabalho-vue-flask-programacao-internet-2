from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from models.modelFuncionario import Funcionario
from banco import db
from config import config
from blacklist import blacklist
import hashlib

funcionarios = Blueprint('funcionarios', __name__)

@funcionarios.route('/login', methods=['POST'])
def login_funcionario():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    cpf = request.json.get('cpf', None)
    password = request.json.get('password', None)
    if not cpf:
        return jsonify({"msg": "Missing cpf parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    password += config.SALT
    password_md5 = hashlib.md5(password.encode()).hexdigest()

    funcionario = Funcionario.query \
        .filter(Funcionario.cpf == cpf) \
        .filter(Funcionario.password == password_md5) \
        .first()
    if funcionario:
        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=cpf)
        return jsonify({"user": funcionario.name, "access_token": access_token}), 200
    else:
        return jsonify({"user": None, "access_token": None}), 200

@funcionarios.route('/logout')
@jwt_required
def logout_funcionario():
    jti = get_raw_jwt()['jwi']
    blacklist.add(jti)
    return jsonify({'msg': 'Successfuly logged out'})

@funcionarios.route('/funcionarios')
@jwt_required
def listar_funcionario():
    funcionarios = Funcionario.query.order_by(Funcionario.name).all()
    return jsonify([funcionario.to_json() for funcionario in funcionarios])

@funcionarios.route('/funcionarios', methods=['POST'])
def incluir_funcionario():
    funcionario = Funcionario.from_json(request.json)
    db.session.add(funcionario)
    db.session.commit()
    return jsonify(funcionario.to_json()), 201