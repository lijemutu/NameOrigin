import unittest

from main import create_app
from NameApi.models import db
from GoberApi.scraper import RequestGoberInfo
from GoberApi.scraper import ParserGoberInfo
from GoberApi.models import GobernadoresMexicoModel
from GoberApi.models import EstadosMexicoModel


class TestURLs(unittest.TestCase):
    def setUp(self):
        app = create_app("config.TestConfig")
        self.client = app.test_client()
        db.app = app
        with app.app_context():
            db.create_all()

    def tearDown(self):
        db.session.remove()

    def test_requestgoberinfo(self):
        html_text = RequestGoberInfo()
        assert html_text is not None

    def test_parsergober(self):
        with open("tests/test_request.html.txt", "r") as testData:
            assert ParserGoberInfo(testData.read()) is not None

    def test_request_n_parse(self):
        html_text = RequestGoberInfo()
        parsed_text = ParserGoberInfo(html_text)
        assert parsed_text is not None

    def test_load_names(self):
        gobernador = GobernadoresMexicoModel(
            "coahuila", "Dr. Ricardo Alfonso Suarez Solis"
        )
        assert gobernador.titulo == "Dr."
        assert gobernador.a_paterno == "Suarez"
        assert gobernador.a_materno == "Solis"
        assert gobernador.nombres == "Ricardo Alfonso"

    def test_load_state(self):
        estadoCoahuila = EstadosMexicoModel("Coahuila")

        assert estadoCoahuila.estado == "Coahuila"

    def test_endpoint_200(self):
        """Tests if the root URL gives a 200"""
        result = self.client.get("/GoberApi/addgobernors")
        assert result.status_code == 200

    def test_origins(self):
        result = self.client.get("/GoberApi/addgobernors")
        result = self.client.get("GoberApi/origins")
        assert result.status_code == 200
