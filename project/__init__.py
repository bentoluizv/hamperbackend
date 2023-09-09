"""Arquivo para inicialização da aplicação e seus módulos"""
import os

from dotenv import load_dotenv
from dynaconf import FlaskDynaconf
from flask import Flask
from flask_migrate import Migrate

from . import views
from .models import db

load_dotenv()
Migrate()


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app)

    if os.environ.get('FLASK_ENV') == 'testing':
        app.config.from_object('databases.test_config.TestConfigurations')
    elif os.environ.get('FLASK_ENV') == 'development':
        app.config.from_object('databases.development_config.DevelopmentConfig')
    elif os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object('databases.production_config.ProductionConfig')
    elif os.environ.get('FLASK_ENV') == 'default':
        app.config.from_object('databases.default_config.DefaultConfigurations')
    else:
        raise ValueError('FLASK_ENV inválido')

    views.init_app(app)
    db.init_app(app)
    Migrate(app, db)

    return app
