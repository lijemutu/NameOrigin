import unittest

from main import create_app
from NameApi.models import db
from GoberApi.scraper import RequestGoberInfo
from GoberApi.scraper import ParserGoberInfo


class TestURLs(unittest.TestCase):
    def setUp(self):
        app = create_app("config.TestConfig")
        self.client = app.test_client()
        db.app = app
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
