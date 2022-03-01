from main import db


class EstadosMexicoModel(db.Model):
    __tablename__ = "estadosmextb"

    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(128), nullable=False)
    gobernador = db.relationship("GobernadoresMexicoModel",
                                 backref="estadosmextb")

    def __init__(self, estado: str) -> None:
        self.estado = estado


class GobernadoresMexicoModel(db.Model):
    __tablename__ = "gobernadoresmextb"

    id = db.Column(db.Integer, primary_key=True)
    estado_id = db.Column(db.Integer, db.ForeignKey("estadosmextb.id"))
    titulo = db.Column(db.String(128))
    nombres = db.Column(db.String(128), nullable=False)
    a_paterno = db.Column(db.String(128), nullable=False)
    a_materno = db.Column(db.String(128), nullable=False)

    def __init__(self, estado: str, nombre: str) -> None:
        nombreSplit = nombre.split(sep=" ")
        self.titulo = nombreSplit[0]
        del nombreSplit[0]
        nombreSplit.reverse()
        self.a_materno = nombreSplit[0]
        self.a_paterno = nombreSplit[1]
        nombreSplit[2:] = nombreSplit[2:][::-1]
        self.nombres = " ".join(nombreSplit[2:])
