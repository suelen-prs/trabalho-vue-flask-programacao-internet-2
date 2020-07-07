from banco import db
import hashlib
from config import config

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def to_json(self):
        json_funcionarios = {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf
        }
        return json_funcionarios

    @staticmethod
    def from_json(json_funcionarios):
        name = json_funcionarios.get('name')
        cpf = json_funcionarios.get('cpf')
        password = json_funcionarios.get('password') + config.SALT
        password_md5 = hashlib.md5(password.encode()).hexdigest()
        return Funcionario(name=name, cpf=cpf, password=password_md5)