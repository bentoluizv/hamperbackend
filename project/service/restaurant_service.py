# from ..models.mock_data import mock_restaurants
from ..ext.database import db
from ..models.restaurant_model import Restaurant


def get_all_restaurants():
    restaurants = Restaurant.query.all()
    return [restaurant.to_dict() for restaurant in restaurants]


def post_restaurant(restaurant_data):
    new_restaurant = Restaurant(
        name=restaurant_data.get("name"),
        description=restaurant_data.get("description"),
        classification=restaurant_data.get("classification"),
        location=restaurant_data.get("location"),
        url_image_logo=restaurant_data.get("url_image_logo"),
        url_image_banner=restaurant_data.get("url_image_banner"),
    )
    db.session.add(new_restaurant)
    db.session.commit()
    return {"message": "Restaurante cadastrado com sucesso!"}


def update_restaurant(id, updated_data):
    restaurant = get_one_restaurant(id)
    if restaurant is None:
        return {"error": f"Restaurante com ID {id} não encontrado"}

    try:
        for key, value in updated_data.items():
            setattr(restaurant, key, value)

        db.session.commit()
        return {"message": f"Restaurante com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def delete_restaurant(restaurant_id):
    restaurant = get_one_restaurant(restaurant_id)
    if restaurant is None:
        return {"error": f"Restaurante com ID {id} não encontrado"}

    try:
        db.session.delete(restaurant)
        db.session.commit()
        return {"message": f"Restaurante com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def get_one_restaurant(restaurant_id):
    return restaurant if (restaurant := Restaurant.query.get(restaurant_id)) else None
