import requests
from sqlalchemy import null
from bs4 import BeautifulSoup
from main import db
from . import models

GOBER_URL = "https://www.conago.org.mx/gobernadores"
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "cache-control": "max-age=0",
    "referer": "https://www.google.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
}


def RequestGoberInfo() -> str:
    """Method to get public Governor info from conago.org using requests"""
    r = requests.get(GOBER_URL, headers=HEADERS)
    if r.status_code != 200:
        return null
    return r.text


def ParserGoberInfo(html_text: str):
    soup = BeautifulSoup(html_text, "lxml")
    listGober = []
    for gober in soup.find_all("div", {"class": "row mrqo"}):
        nombre = gober.find("h4").contents[1].contents[0].strip()
        estado = (
            gober.find("div", {"class": "media-body escudo"})
            .contents[1]
            .contents[0]
            .strip()
        )
        listGober.append({"estado": estado, "nombre": nombre})
    return listGober


def SaveGoberInfo(gober_list_dict: list):
    # TODO If exist the record do not add it to db
    for gober in gober_list_dict:
        goberModel = models.GobernadoresMexicoModel(gober["estado"],
                                                    gober["nombre"])
        estadoModel = models.EstadosMexicoModel(estado=gober["estado"])
        goberModel.estado.append(estadoModel)
        db.session.add(goberModel)
        db.session.add(estadoModel)
    db.session.commit()
