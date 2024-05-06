from flask import request
from ..ext.database import db
from ..models.product_model import Product


def get_all_products():
    return Product.query.all()

#TODO: SERVICE DE PRODUTOS POR RESTAURANTE
def get_products_by_restaurant_id(restaurant_id):

    products = Product.query.filter(
        Product.restaurant_id == restaurant_id
    ).all()

    if not products:
        return {"error": f"Nenhum produto encontrado para restaurante com ID {restaurant_id}"}

    product_list = []
    for product in products:
        product_list.append(product)

    return product_list

def post_product(product_data):
    product_data = request.get_json()
    product = Product(**product_data)
    db.session.add(product)
    db.session.commit()


def get_one_product(product_id):
    return product if (product := Product.query.get(product_id)) else None


def update_product(id, updated_data):
    product = get_one_product(id)
    if product is None:
        return {"error": f"Produto com ID {id} não encontrado"}

    try:
        for key, value in updated_data.items():
            setattr(product, key, value)

        db.session.commit()
        return {"message": f"Produto com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def delete_product(id):
    product = get_one_product(id)
    if product is None:
        return {"error": f"Produto com ID {id} não encontrado"}

    try:
        db.session.delete(product)
        db.session.commit()
        return {"message": f"Produto com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}