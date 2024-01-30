# from project.models.mock_data import mock_restaurants
from flask import abort, request
from flask_restx import Resource

from project.service.restaurant_service import (delete_restaurant,
                                                get_all_restaurants,
                                                get_one_restaurant,
                                                post_restaurant,
                                                update_restaurant)


class RestaurantResource(Resource):
    def get(self):
        restaurants = get_all_restaurants()
        return {"restaurants": restaurants}, 200

    def post(self):
        restaurant_data = request.json
        try:
            post_restaurant(restaurant_data)
            return {"message": "Restaurante cadastrado com sucesso!"}, 201
        except Exception as e:
            return {"error": str(e)}, 400


class RestaurantResourceID(Resource):
    def patch(self, id):
        try:
            restaurant_data = request.json
            result = update_restaurant(id, restaurant_data)

            if "error" in result:
                abort(404, message=result["error"])

            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

    def get(self, id):
        if restaurant := get_one_restaurant(id):
            return {"restaurant": restaurant.to_dict()}, 200  # type: ignore
        else:
            return {"error": f"Restaurante com ID {id} não encontrado."}, 404

    def delete(self, id):
        try:
            result = delete_restaurant(id)

            if "error" in result:
                return {"error": result["error"]}, 404

            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500
