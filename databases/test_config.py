from dynaconf import settings
from flask import Config


class TestConfigurations(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = settings.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = settings.get('SECRET_KEY')
