"""Arquivo para inicialização da aplicação e seus módulos"""
from dotenv import load_dotenv
from dynaconf import FlaskDynaconf
from flask import Flask

from . import views

load_dotenv()


def create_app():
    app = Flask(__name__)

    FlaskDynaconf(app)

    views.init_app(app)

    return app
