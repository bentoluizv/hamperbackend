"""Arquivo para inserção das funções e rotas"""


def init_app(app):
    @app.route("/")
    def hello_world():
        return "<p>Hello, World {name}!</p>".format(name=__name__)
