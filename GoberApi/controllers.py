from flask import Blueprint
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
