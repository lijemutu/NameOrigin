from NameApi.models import FullNameModel, PartialNameModel
from GoberApi.models import EstadosMexicoModel, GobernadoresMexicoModel
import os
from main import db, migrate, create_app

env = os.environ.get("APIAPP_ENV", "dev")
app = create_app("config.%sConfig" % env.capitalize())


@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        FullNameModel=FullNameModel,
        PartialNameModel=PartialNameModel,
        EstadosMexicoModel=EstadosMexicoModel,
        GobernadoresMexicoModel=GobernadoresMexicoModel,
        migrate=migrate,
    )
