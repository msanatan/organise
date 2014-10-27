class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///organise.db'
    SECRET_KEY = 'something secret'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'

class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'super secret?'

class TestConfig(Config):
    TESTING = True
