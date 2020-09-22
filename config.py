import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wainainakasyoka:W41n41n4@localhost/pitchme'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

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