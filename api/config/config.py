import os
from decouple import config
from datetime import timedelta



BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Baseconfig:
    SECRET_KEY = config('SECRET_KEY', 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRE = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRE = timedelta(minutes=30)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')


class DevConfig(Baseconfig):
    DEBUG = config('DEBUG',cast=bool)
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:1212@localhost/QuizApi'
    DEBUG = True
    

class TestConfig(Baseconfig):
    pass


class ProdConfig(Baseconfig):
    pass


config_dict = {
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig,
}
