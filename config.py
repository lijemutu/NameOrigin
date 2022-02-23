class Config(object):
    pass


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://test:password@postgres:5432/mex_polit_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://test:password@localhost:5432/mex_polit_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    DEBUG = True
    DEBUG_TB_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "null"
    WTF_CSRF_ENABLED = False
