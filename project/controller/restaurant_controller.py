from flask_restx import Resource

from project.service.restaurant_service import get_all_restaurants, post_restaurant


class RestaurantResource(Resource):

    def get(self):
        restaurants = get_all_restaurants()
        return restaurants, 200

    def post(self):
        restaurant = post_restaurant()
        return restaurant, 200