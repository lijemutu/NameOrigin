import unittest

from main import create_app
from NameApi.models import db


class TestURLs(unittest.TestCase):
    def setUp(self):
        app = create_app("config.TestConfig")
        self.client = app.test_client()
        db.app = app
        db.create_all()

    def tearDown(self):
        db.session.remove()

    def test_name_400_no_params(self):
        """Tests if the root URL gives a 400 when no parameters are send"""
        result = self.client.get("/NameApi/name")
        assert result.status_code == 400

    def test_partialname_400_no_params(self):
        """Tests if the root URL gives a 400 when no parameters are send"""
        result = self.client.get("/NameApi/partialname")
        assert result.status_code == 400


if __name__ == "__main__":
    unittest.main()
