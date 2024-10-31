from dotenv import load_dotenv
import os


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'


class TestConfig(Config):
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestConfig,
    'default': DevelopmentConfig,
}

