from banco import db

class Proposta(db.Model):
    __tablename__ = 'propostas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    contato = db.Column(db.String(11), nullable=False)
    valor_proposta = db.Column(db.Float(60), nullable=False)

    carro_id = db.Column(db.Integer, db.ForeignKey('carros.id'), nullable=False)
    carro = db.relationship('Carro')

    def to_json(self):
        json_propostas = {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'contato': self.contato,
            'carro_id': self.carro_id,
            'carro': self.carro.modelo,
            'valor_proposta': self.valor_proposta
        }
        return json_propostas
    
    @staticmethod
    def from_json(json_propostas):
        nome = json_propostas.get('nome')
        email = json_propostas.get('email')
        contato = json_propostas.get('contato')
        carro_id = json_propostas.get('carro_id')
        valor_proposta = json_propostas.get('valor_proposta')
        return Proposta(nome=nome, email=email, contato=contato, carro_id=carro_id, valor_proposta=valor_proposta)