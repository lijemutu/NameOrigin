import datetime
import os

import requests
from main import db


class FullNameModel(db.Model):
    __tablename__ = "fullnamestb"

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(128), nullable=False)
    lastName = db.Column(db.String(128), nullable=False)
    secondLastName = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime)
    foundCountry1 = db.Column(db.String(128), nullable=False)
    foundCountry1percent = db.Column(db.Float, nullable=False)
    foundCountry2 = db.Column(db.String(128), nullable=True)
    foundCountry2percent = db.Column(db.Float, nullable=True)
    foundCountry3 = db.Column(db.String(128), nullable=True)
    foundCountry3percent = db.Column(db.Float, nullable=True)
    foundCountry4 = db.Column(db.String(128), nullable=True)
    foundCountry4percent = db.Column(db.Float, nullable=True)
    foundCountry5 = db.Column(db.String(128), nullable=True)
    foundCountry5percent = db.Column(db.Float, nullable=True)

    def __init__(self, firstName, lastName, secondLastName, countries: list):
        self.firstName = firstName
        self.lastName = lastName
        self.secondLastName = secondLastName
        self.created_at = datetime.datetime.utcnow()

        try:
            self.foundCountry1 = countries[0]["jurisdiction"]
        except IndexError:
            self.foundCountry1 = ""
        try:
            self.foundCountry1percent = float(countries[0]["percent"])
        except IndexError:
            self.foundCountry1percent = 0

        try:
            self.foundCountry2 = countries[1]["jurisdiction"]
        except IndexError:
            self.foundCountry2 = ""
        try:
            self.foundCountry2percent = float(countries[1]["percent"])
        except IndexError:
            self.foundCountry2percent = 0

        try:
            self.foundCountry3 = countries[2]["jurisdiction"]
        except IndexError:
            self.foundCountry3 = ""
        try:
            self.foundCountry3percent = float(countries[2]["percent"])
        except IndexError:
            self.foundCountry3percent = 0

        try:
            self.foundCountry4 = countries[3]["jurisdiction"]
        except IndexError:
            self.foundCountry4 = ""
        try:
            self.foundCountry4percent = float(countries[3]["percent"])
        except IndexError:
            self.foundCountry4percent = 0

        try:
            self.foundCountry5 = countries[4]["jurisdiction"]
        except IndexError:
            self.foundCountry5 = ""
        try:
            self.foundCountry5percent = float(countries[4]["percent"])
        except IndexError:
            self.foundCountry5percent = 0


class PartialNameModel(db.Model):
    __tablename__ = "partialnamestb"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    typeName = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    foundCountry1 = db.Column(db.String(128), nullable=False)
    foundCountry1percent = db.Column(db.Float, nullable=False)
    foundCountry2 = db.Column(db.String(128), nullable=True)
    foundCountry2percent = db.Column(db.Float, nullable=True)
    foundCountry3 = db.Column(db.String(128), nullable=True)
    foundCountry3percent = db.Column(db.Float, nullable=True)
    foundCountry4 = db.Column(db.String(128), nullable=True)
    foundCountry4percent = db.Column(db.Float, nullable=True)
    foundCountry5 = db.Column(db.String(128), nullable=True)
    foundCountry5percent = db.Column(db.Float, nullable=True)

    def __init__(self, name, typeName, countries: list):
        self.name = name
        self.typeName = typeName
        self.created_at = datetime.datetime.utcnow()

        try:
            self.foundCountry1 = countries[0]["jurisdiction"]
        except IndexError:
            self.foundCountry1 = ""
        try:
            self.foundCountry1percent = float(countries[0]["incidence"])
        except IndexError:
            self.foundCountry1percent = 0

        try:
            self.foundCountry2 = countries[1]["jurisdiction"]
        except IndexError:
            self.foundCountry2 = ""
        try:
            self.foundCountry2percent = float(countries[1]["incidence"])
        except IndexError:
            self.foundCountry2percent = 0

        try:
            self.foundCountry3 = countries[2]["jurisdiction"]
        except IndexError:
            self.foundCountry3 = ""
        try:
            self.foundCountry3percent = float(countries[2]["incidence"])
        except IndexError:
            self.foundCountry3percent = 0

        try:
            self.foundCountry4 = countries[3]["jurisdiction"]
        except IndexError:
            self.foundCountry4 = ""
        try:
            self.foundCountry4percent = float(countries[3]["incidence"])
        except IndexError:
            self.foundCountry4percent = 0

        try:
            self.foundCountry5 = countries[4]["jurisdiction"]
        except IndexError:
            self.foundCountry5 = ""
        try:
            self.foundCountry5percent = float(countries[4]["incidence"])
        except IndexError:
            self.foundCountry5percent = 0


class NamesApi:
    def __init__(self, firstName="", lastName="", secondLastName="") -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.secondLastName = secondLastName

    # TODO Refactor to another class
    def requestApiServer(self, url, type):
        try:
            r = requests.get(url)
        except requests.exceptions.Timeout:
            return {"error": 500}
        # Maybe set up for a retry, or continue in a retry loop
        except requests.exceptions.TooManyRedirects:
            return {"error": 500}
        # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException:
            return {"error": 500}

        if r.status_code != 200:
            raise Exception(f"Request for {type} ... not valid")
        data = r.json()

        apiErrors = ["0018", "0007"]
        if "status" in data and data["status"][0]["code"] in apiErrors:
            return {"error": 400}

        if type == "fullName":
            if "secondSurname" in data:
                parsedData = {
                    "forename": data["forename"],
                    "surname": data["surname"],
                    "secondSurname": data["secondSurname"],
                    "countries": data["countries"][0:5],
                }
            else:
                parsedData = {
                    "forename": data["forename"],
                    "surname": data["surname"],
                    "countries": data["countries"][0:5],
                }
            self.saveResponseFullNameToDatabase(parsedData)

        else:
            parsedData = {
                "name": data["name"],
                "type": data["type"],
                "countries": data["jurisdictions"][0:5],
            }
            self.saveResponsePartialNameToDatabase(parsedData)

        return parsedData

    def requestFullName(self):

        foundUser: FullNameModel = FullNameModel.query.filter_by(
            firstName=self.firstName,
            lastName=self.lastName,
            secondLastName=self.secondLastName,
        ).first()
        if foundUser is not None:
            return {
                "forename": foundUser.firstName,
                "surname": foundUser.lastName,
                "countries": [
                    {
                        "jurisdiction": foundUser.foundCountry1,
                        "percent": str(foundUser.foundCountry1percent),
                    },
                    {
                        "jurisdiction": foundUser.foundCountry2,
                        "percent": str(foundUser.foundCountry2percent),
                    },
                    {
                        "jurisdiction": foundUser.foundCountry3,
                        "percent": str(foundUser.foundCountry3percent),
                    },
                    {
                        "jurisdiction": foundUser.foundCountry4,
                        "percent": str(foundUser.foundCountry4percent),
                    },
                    {
                        "jurisdiction": foundUser.foundCountry5,
                        "percent": str(foundUser.foundCountry5percent),
                    },
                ],
            }
        API_KEY_NAMES = os.environ.get("API_KEY_NAMES")
        ONO_API_FULL_NAME = f"https://ono.4b.rs/v1/nat?key={API_KEY_NAMES}\
            &fn={self.firstName}&sn={self.lastName}&ssn={self.secondLastName}"
        return self.requestApiServer(ONO_API_FULL_NAME, "fullName")

    def requestPartialName(self, typeName):
        if typeName == "forename":
            name = self.firstName
        if typeName == "surname":
            name = self.lastName

        foundUser: FullNameModel.PartialNameModel = (
            FullNameModel.PartialNameModel.query.filter_by(
                name=name, typeName=typeName
            ).first()
        )
        if foundUser is not None:
            return {
                "name": foundUser.name,
                "type": foundUser.typeName,
                "countries": [
                    {
                        "jurisdiction": foundUser.foundCountry1,
                        "percent": str(foundUser.foundCountry1percent),
                    },
                    {
                        "jurisdiction": foundUser.foundCountry2,
                        "percent": str(foundUser.foundCountry2percent),
                    },
                    {
                        "jurisdiction": foundUser.foundCountry3,
                        "percent": str(foundUser.foundCountry3percent),
                    },
                    {
                        "jurisdiction": foundUser.foundCountry4,
                        "percent": str(foundUser.foundCountry4percent),
                    },
                    {
                        "jurisdiction": foundUser.foundCountry5,
                        "percent": str(foundUser.foundCountry5percent),
                    },
                ],
            }
        API_KEY_NAMES = os.environ.get("API_KEY_NAMES")
        ONO_API_PARTIAL = f"https://ono.4b.rs/v1/jur?key={API_KEY_NAMES}&name={name}\
                &type={typeName}"
        return self.requestApiServer(ONO_API_PARTIAL, typeName)

    # TODO Refactor to another class
    def saveResponsePartialNameToDatabase(self, data):
        name = data["name"]
        type = data["type"]
        countries = data["countries"]
        partialNameModel = FullNameModel.PartialNameModel(
            name=name, typeName=type, countries=countries
        )
        db.session.add(partialNameModel)
        db.session.commit()

    # TODO Refactor to another class
    def saveResponseFullNameToDatabase(self, data):
        forename = data["forename"]
        surname = data["surname"]
        if "secondSurname" in data:
            secondSurname = data["secondSurname"]
        else:
            secondSurname = ""
        countries = data["countries"]
        fullNameModel = FullNameModel(
            firstName=forename,
            lastName=surname,
            secondLastName=secondSurname,
            countries=countries,
        )
        db.session.add(fullNameModel)
        db.session.commit()
