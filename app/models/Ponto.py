

from db import db
from datetime import datetime

class Ponto(db.Model):

    __tablename__ = "ponto"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 'in' ou 'out'
    tipo_de_ponto = db.Column(db.String(10), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    last_modified_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    colaborador_id = db.Column(db.Integer, db.ForeignKey("colaborador.id"))
    colaborador = db.relationship("Colaborador", back_populates="pontos")
