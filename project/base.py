from dynaconf import FlaskDynaconf
from flask import Flask
from flask_cors import CORS


def create_app(**config):
    app = Flask(__name__)
    FlaskDynaconf(app, envvar_prefix="FLASK", settings_files=[
                  "settings.toml"])
    app.config.load_extensions(
        "EXTENSIONS"
    )
    app.config.update(config)
    CORS(app)

    print(f"Ambiente atual: {app.config.env}")
    print(f"Banco de dados atual: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    print("Aplicação inicializada com sucesso!")

    return app


def create_app_wsgi():
    return create_app()
