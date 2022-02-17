class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://test:password@localhost:5432/mex_polit_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
