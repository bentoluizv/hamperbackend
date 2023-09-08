from dynaconf import settings
from flask import Config


class DefaultConfigurations(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = settings.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = settings.get('SECRET_KEY')
