

from app import db
from datetime import datetime

class Colaborador(db.Model):

    __tablename__ = "colaborador"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    nome = db.Column(db.String(150), nullable=False)
    
    cpf = db.Column(db.String(30), nullable=False)
    
    email = db.Column(db.String(255), nullable=False)

    celular = db.Column(db.String(30), nullable=False)

    # em um ambiente real, seria uma chave estrangeira para a tabela empresa
    empresa = db.Column(db.String(255), nullable=False)

    cargo = db.Column(db.String(255), nullable=False)

    endereco = db.Column(db.String(150), nullable=False)

    cep = db.Column(db.String(20), nullable=False)

    ativo = db.Column(db.Boolean, default=False, nullable=False)

    ''' Em um ambiente real, seria uma chave estrangeira para a tabela regras, 
    onde seriam guardadas as regras de ponto do colaborador'''
    regras = db.Column(db.Integer, default=0, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    last_modified_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    pontos = db.relationship("Ponto")