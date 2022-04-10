from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(object_name):
    from NameApi.controllers import NameApi_blueprint
    from GoberApi.controllers import GoberApi_blueprint
    from views.controller.controller import views_blueprint

    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    db.create_all()
    migrate.init_app(app, db)
    app.register_blueprint(NameApi_blueprint)
    app.register_blueprint(GoberApi_blueprint)
    app.register_blueprint(views_blueprint)
    return app
