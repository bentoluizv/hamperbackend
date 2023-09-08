from dynaconf import settings
from flask import Config


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = settings.get('SECRET_KEY')
