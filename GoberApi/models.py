from sqlalchemy import true
from main import db


class EstadosMexicoModel(db.Model):
    __tablename__ = "estadosmextb"

    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(128), nullable=False)
    gobernador = db.relationship(
        "gobernadoresmextb", backref="estadosmextb", lazy=true
    )

    def __init__(self, estado) -> None:
        self.estado = estado


class GobernadoresMexicoModel(db.Model):
    __tablename__ = "gobernadoresmextb"

    id = db.Column(db.Integer, primary_key=True)
    estado_id = db.Column(db.Integer, db.ForeignKey("estadosmextb.id"))
    titulo = db.Column(db.String(128))
    nombres = db.Column(db.String(128), nullable=False)
    a_paterno = db.Column(db.String(128), nullable=False)
    a_materno = db.Column(db.String(128), nullable=False)
