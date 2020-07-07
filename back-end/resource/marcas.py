from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from banco import db
from models.modelMarca import Marca

marcas = Blueprint('marcas', __name__)

@marcas.route('/marcas')
def listagem_marcas():
    marcas = Marca.query.order_by(Marca.id).all()
    return jsonify([marca.to_json() for marca in marcas])

@marcas.route('/marcas', methods=['POST'])
@jwt_required
def inclusao_marcas():
    marca = Marca.from_json(request.json)
    db.session.add(marca)
    db.session.commit()
    return jsonify(marca.to_json()), 201

@marcas.route('/marcas/<int:id>', methods=['PUT'])
@jwt_required
def alterar_marcas(id):
    marcas = Marca.query.get_or_404(id)
    marcas.nome = request.json['nome']
    db.session.add(marcas)
    db.session.commit()
    return jsonify(marcas.to_json()), 204

@marcas.route('/marcas/<int:id>', methods=['DELETE'])
def excluir_marca():
    Marca.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id': id, 'message': 'Marca excluida.'}), 200