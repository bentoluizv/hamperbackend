from flask import Blueprint
from flask_restx import Api

from project.utils.namespace import restaurant_ns, user_ns
from project.controller.user_controller import UserResource
from ...controller.restaurant_controller import RestaurantResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    app.register_blueprint(bp)
    api.add_resource(RestaurantResource, "/restaurants/")
    api.add_namespace(restaurant_ns)
    api.add_resource(UserResource, "/users/")
    api.add_namespace(user_ns)