from flask import Blueprint
from .models import GobernadoresMexicoModel
from .models import EstadosMexicoModel

GoberApi_blueprint = Blueprint("GoberApi", __name__, url_prefix="/GoberApi")
