from flask import Blueprint, request
from .models import NamesApi

NameApi_blueprint = Blueprint("NameApi", __name__, url_prefix="/NameApi")


@NameApi_blueprint.route("/name", methods=["GET"])
def NameNationality():
    args = request.args

    if "fn" in args and "sn" in args:
        firstName = args["fn"]
        lastName = args.get("sn")
    else:
        return "Parameters malformed", 400

    if "ssn" in args:
        secondLastName = args["ssn"]
    else:
        secondLastName = ""

    if firstName == "" or lastName == "":
        return "You miss firstName or lastName", 400

    nameObject = NamesApi(firstName, lastName, secondLastName=secondLastName)

    nationalities = nameObject.requestFullName()
    if "error" in nationalities:
        if nationalities["error"] == 404:
            return "Elements not found", 404
        if nationalities["error"] == 500:
            return "Internal Server error with request", 500
        if nationalities["error"] == 400:
            return "Bad request", 400
    return nationalities, 200


@NameApi_blueprint.route("/partialname", methods=["GET"])
def PartialNameLocation():
    args = request.args

    if "name" in args and "type" in args:
        name = args["name"]
        typeName = args.get("type")
    else:
        return "Parameters malformed", 400

    if name == "" or typeName == "":
        return "You miss name or type", 400

    if not (typeName == "forename" or typeName == "surname"):
        return f"typeName '{typeName}' not valid", 400

    if typeName == "forename":
        nameObject = NamesApi(firstName=name, lastName="")
    if typeName == "surname":
        nameObject = NamesApi(firstName="", lastName=name)

    locations = nameObject.requestPartialName(typeName)
    if "error" in locations:
        if locations["error"] == 404:
            return "Elements not found", 404
        if locations["error"] == 500:
            return "Internal Server error with request", 500
        if locations["error"] == 400:
            return "Bad request", 400

    return locations, 200
