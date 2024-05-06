from flask import request
from project.service.product_service import delete_product, get_products_by_restaurant_id
from ..ext.database import db
from ..models.restaurant_model import Restaurant


def get_all_restaurants():
    return Restaurant.query.all()


def post_restaurant(data_restaurant):
    data_restaurant = request.get_json()
    restaurant = Restaurant(**data_restaurant)
    db.session.add(restaurant)
    db.session.commit()

def get_one_restaurant_by_id(restaurante_id):
    return Restaurant.query.get(restaurante_id)


def get_one_restaurant(restaurant_id):
    return restaurant if (restaurant := Restaurant.query.get(restaurant_id)) else None


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



# def delete_restaurant(id):
#     restaurant = get_one_restaurant_by_id(id)
    
#     if restaurant is None:
#         return {"error": f"Restaurante com ID {id} não encontrado"}

#     try:
#         db.session.delete(restaurant)
#         db.session.commit()
#         return {"message": f"Restaurante com ID {id} deletado com sucesso."}

#     except Exception as e:
#         db.session.rollback()
#         return {"error": str(e)}


def delete_restaurant(id):
    restaurant = get_one_restaurant_by_id(id)

    if restaurant is None:
        return {"error": f"Restaurante com ID {id} não encontrado"}
    
    #TODO: VERIFICA SE TEM ALGUM PRODUTO VINCULADO AO RESTAURANTE
    products = get_products_by_restaurant_id(id)  
    
    # SE TIVER É APAGADO PRIMEIRO:
    for product in products:
        delete_product(product.id)

    try:
        db.session.delete(restaurant)  
        db.session.commit()

        return {"message": f"Restaurante com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
