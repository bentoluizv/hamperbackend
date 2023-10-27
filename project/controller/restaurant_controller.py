from flask import request
from flask_restx import Api, Resource

from project.service.restaurant_service import (delete_restaurant,
                                                get_all_restaurants,
                                                get_one_restaurant,
                                                post_restaurant,
                                                put_one_restaurant)

from ..models.user_model import db

api = Api()


class RestaurantResource(Resource):

    def get(self):
        restaurants = get_all_restaurants()
        return restaurants, 200

    @api.doc(params={'name': 'Name of the restaurant',
                     'value': 'Value of the restaurant',
                     'description': 'Description of the restaurant',
                     'url_image': 'URL image of the restaurant',
                     'restaurant_id': 'ID of the restaurant'})
    def post(self):
        restaurant, status = post_restaurant()
        return restaurant, status


class RestaurantResourceId(Resource):

    @api.doc(params={'id': 'ID of the restaurant'})
    def get(self, id):
        if restaurant := get_one_restaurant(id):
            return restaurant, 200
        else:
            return {'message': 'Restaurant not found'}, 404

    @api.doc(params={'id': 'ID of the restaurant'})
    def put(self, id):
        if restaurant := put_one_restaurant(id):
            db.session.commit()
            return restaurant, 200

    @api.doc(params={'id': 'ID of the restaurant'})
    def delete(self, id):
        if restaurant := delete_restaurant(id):
            db.session.delete(restaurant)
            db.session.commit()
            return {'message': 'Restaurant deleted'}
        else:
            return {'message': 'Restaurant not found'}, 404
