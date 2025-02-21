from flask import request
from datetime import datetime
from ..ext.database import db
from ..models.restaurant_model import Restaurant
from typing import Dict, Optional


def get_all_restaurants() -> list[Restaurant]:
    return Restaurant.query.all()

def post_restaurant(data_restaurant: dict):
    data_restaurant = request.get_json()
    data_restaurant['horario_funcionamento'] = datetime.strptime(data_restaurant['horario_funcionamento'], '%H:%M:%S').time()
    data_restaurant['horario_fechamento'] = datetime.strptime(data_restaurant['horario_fechamento'], '%H:%M:%S').time()
    restaurant = Restaurant(**data_restaurant)
    db.session.add(restaurant)
    db.session.commit()

def get_one_restaurant_by_id(restaurant_id: int):
    return Restaurant.query.get(restaurant_id)


def get_one_restaurant_with_products(restaurant_id: int):
    restaurant = Restaurant.query.get(restaurant_id)

    if restaurant:
        restaurant_data = {
            "id": restaurant.id,
            "name": restaurant.name,
            "description": restaurant.description,
            "classification": restaurant.classification,
            "location": restaurant.location,
            "url_image_logo": restaurant.url_image_logo,
            "url_image_banner": restaurant.url_image_banner,
            "telephone": restaurant.telephone,
            "associated_products": []
        }

        for product in restaurant.products:
            product_data = {
                "id": product.id,
                "name": product.name,
                "value": product.value,
                "description": product.description,
                "url_image": product.url_image,
                "restaurant_id": product.restaurant_id,
            }
            restaurant_data["associated_products"].append(product_data)

        return restaurant_data
    else:
        return None

def update_restaurant(id: int, updated_data: dict):
    restaurant = get_one_restaurant_by_id(id)

    if restaurant is None:
        return {"error": f"Restaurante com ID {id} não encontrado"}

    try:
        for key, value in updated_data.items():
            restaurant[key] = value

        db.session.commit()
        return {"message": f"Restaurante com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def delete_restaurant(id: int):
    restaurant = get_one_restaurant_by_id(id)
    
    if restaurant is None:
        return {"error": f"Restaurante com ID {id} não encontrado"}

    try:
        db.session.delete(restaurant)
        db.session.commit()
        return {"message": f"Restaurante com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
