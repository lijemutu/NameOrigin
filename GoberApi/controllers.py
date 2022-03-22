from flask import Blueprint
from typing import Dict
from NameApi.controllers import NameNationalityInternal
from .models import GobernadoresMexicoModel
from .models import EstadosMexicoModel
from .scraper import RequestGoberInfo
from .scraper import ParserGoberInfo
from .scraper import SaveGoberInfo


GoberApi_blueprint = Blueprint("GoberApi", __name__, url_prefix="/GoberApi")


@GoberApi_blueprint.route("/addgobernors", methods=["GET"])
def AddGobernors():
    goberScraped = RequestGoberInfo()
    goberParsed = ParserGoberInfo(goberScraped)
    SaveGoberInfo(goberParsed)
    return f"{len(goberParsed)} Gobernors and states updated", 200


@GoberApi_blueprint.route("/origins", methods=["GET"])
def GobernorOrigin():
    gobernors = GobernadoresMexicoModel.query.join(
        EstadosMexicoModel, GobernadoresMexicoModel.id == EstadosMexicoModel.gobernador
    ).all()
    if len(gobernors) != 32:
        return "Gobernors are not in db, update them first", 404
    gobernor: GobernadoresMexicoModel
    originGobernor = {}
    for gobernor in gobernors:
        origin_result = NameNationalityInternal(
            gobernor.nombres, gobernor.a_paterno, gobernor.a_materno
        )
        if origin_result is not Dict[str, int]:
            originGobernor[gobernor.estado[0].estado] = origin_result
        else:
            return "error", origin_result["error"]
    return originGobernor, 200


def GobernorOriginInternal():
    gobernors = GobernadoresMexicoModel.query.join(
        EstadosMexicoModel, GobernadoresMexicoModel.id == EstadosMexicoModel.gobernador
    ).all()
    if len(gobernors) != 32:
        return "Gobernors are not in db, update them first", 404
    gobernor: GobernadoresMexicoModel
    originGobernor = {}
    for gobernor in gobernors:
        origin_result = NameNationalityInternal(
            gobernor.nombres, gobernor.a_paterno, gobernor.a_materno
        )
        if origin_result is not Dict[str, int]:
            originGobernor[gobernor.estado[0].estado] = origin_result
        else:
            return "error", origin_result["error"]
    return originGobernor, 200
