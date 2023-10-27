from flask import request

from project.ext.database import db
from project.models.restaurant_model import Restaurant


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


def get_one_restaurant(id):
    if restaurant := Restaurant.query.get(id):
        return restaurant.to_dict()
    else:
        return {'message': 'Restaurante not found'}, 404


def put_one_restaurant(id):
    if restaurant := Restaurant.query.get(id):
        data = request.get_json()
        restaurant.name = data.get('name')
        restaurant.description = data.get('description')
        restaurant.classification = data.get('classification')
        restaurant.location = data.get('location')
        restaurant.url_image_logo = data.get('url_image_logo')
        restaurant.url_image_banner = data.get('url_image_banner')
        db.session.commit()
        return restaurant.to_dict()
    else:
        return {'message': 'Restaurante not found'}, 404


def delete_restaurant(id):
    if restaurant := Restaurant.query.get(id):
        db.session.delete(restaurant)
        db.session.commit()
        return {'message': 'Restaurante deletado'}
    else:
        return {'message': 'Restaurante not found'}, 404
