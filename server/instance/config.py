import os


class Config(object):
    """
    Base Config Class
    """
    DEBUG = True
    TESTING = True
    PRODUCTION = False
    CSRF_ENABLED = True
    SECRET_KEY = ''


class ProductionConfig(Config):
    """
    Production Config
    """
    DEBUG = False
    TESTING = False
    PRODUCTION = True


class DevelopmentConfig(Config):
    """
    Development Env Config
    """
    DEBUG = True
    TESTING = True
    PRODUCTION = False
