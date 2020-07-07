from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from banco import db
from models.modelProposta import Proposta
import smtplib

propostas = Blueprint('propostas', __name__)

@propostas.route('/propostas', methods=['POST'])
def incluir_proposta():
    proposta = Proposta.from_json(request.json)
    db.session.add(proposta)
    db.session.commit()
    return jsonify(proposta.to_json()), 201

@propostas.route('/propostas')
@jwt_required
def listar_propostas():
    propostas = Proposta.query.order_by(Proposta.id).all()
    return jsonify([Proposta.to_json() for Proposta in propostas])

@propostas.route('/propostas/<int:id>')
@jwt_required
def consultar_proposta(id):
    proposta = Proposta.query.get_or_404(id)
    return jsonify(proposta.to_json()), 200

@propostas.route('/propostas/<int:id>', methods=['DELETE'])
@jwt_required
def excluir_propostas(id):
    Proposta.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id': id, 'message': 'Proposta excluída.'}), 200

@propostas.route('/propostas/envia_email/<int:id>')
def envia_email(id):
    #proposta = Proposta.query.order_by(Proposta.id)
    proposta_email = Proposta.query.get_or_404(id)
    
    propostas.nome = request.json['nome']
    propostas.email = request.json['email']
    propostas.contato = request.json['contato']
    propostas.valor_proposta = request.json['valor_proposta']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('conta.teste.laravel@gmail.com', 'conta#teste#laravel')
    server.set_debuglevel(1)
    msg = 'Subject: Proposta Herbie Veículos\
        \nRecebemos sua proposta para o veiculo.\
        \nSua proposta será analisada por um de nossos \
        colaboradores'.encode('utf-8')
    server.sendmail('conta.teste.laravel@gmail.com', propostas.email, msg)
    server.quit()
    return "E-mail enviado."