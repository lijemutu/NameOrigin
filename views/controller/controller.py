import os
from flask import Blueprint, render_template
from maps.map import mexMap

template_dir = os.path.abspath(os.path.join("views", "controller", "static"))

views_blueprint = Blueprint(
    "Views", __name__, url_prefix="/", template_folder=template_dir
)


@views_blueprint.route("/", methods=["GET"])
def index():
    mexicoMap = mexMap()
    return render_template("index.html", plot=mexicoMap)
