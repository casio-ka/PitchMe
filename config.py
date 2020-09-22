import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wainainakasyoka:W41n41n4@localhost/pitchme'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}