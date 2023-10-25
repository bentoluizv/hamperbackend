from flask import request
from project.models.restaurant_model import Restaurant
from project.ext.database import db


def get_all_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = []
    for restaurant in restaurants:
            restaurant_data = {
                'id': restaurant.id,
                'name': restaurant.name,
                'description': restaurant.description,
                'classification': restaurant.classification,
                'location': restaurant.location,
                'url_image_logo': restaurant.url_image_logo,
                'url_image_banner': restaurant.url_image_banner,
            }
            restaurant_list.append(restaurant_data)
    return restaurant_list

def post_restaurant():
    dados = request.get_json()
    restaurant = Restaurant(**dados)
    db.session.add(restaurant)
    db.session.commit()
    return {'message': 'Restaurante criado com sucesso'}, 201