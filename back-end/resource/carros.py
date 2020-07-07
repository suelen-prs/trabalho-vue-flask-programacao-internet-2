from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.modelCarro import Carro
from banco import db

carros = Blueprint('carros', __name__)

@carros.route('/carros', methods=['POST'])
@jwt_required
def incluir_carro():
    carro = Carro.from_json(request.json)
    db.session.add(carro)
    db.session.commit()
    return jsonify(carro.to_json()), 201

@carros.route('/carros')
def listar_carros():
    carros = Carro.query.order_by(Carro.modelo).all()
    return jsonify([carro.to_json() for carro in carros])

@carros.route('/carros/<int:id>')
def consultar_carro(id):
    carro = Carro.query.get_or_404(id)
    return jsonify(carro.to_json()), 200

@carros.route('/carros/filtro/<modelo>')
def filtrar_modelo(modelo):
    carros = Carro.query.order_by(Carro.modelo).filter(Carro.modelo.like(f'%{modelo}%')).all()
    return jsonify([carro.to_json() for carro in carros])

@carros.errorhandler(404)
def id_invalido(error):
    return jsonify({'id': 0, 'message': 'not found'}), 404


@carros.route('/carros/destaque')
def listar_destaque():
    carros = Carro.query.filter_by(destaque='x').all()
    return jsonify([carro.to_json() for carro in carros])

@carros.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    Carro.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id': id, 'message': 'Carros excluido!'}), 200

@carros.route('/carros/estatistica/total')
def total_carros():
    carros = Carro.query.count()
    return jsonify({'Total': carros})


