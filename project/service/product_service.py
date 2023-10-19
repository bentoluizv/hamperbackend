from flask import request
from project.models.product_model import Product
from project.ext.database import db


def get_all_products():
    products = Product.query.all()
    product_list = []
    for product in products:
            product_data = {
                'id': product.id,
                'name': product.name,
                'value': product.value,
                'description': product.description,
                'url_image': product.url_image,
                'restaurant_id': product.restaurant_id
            }
            product_list.append(product_data)
    return product_list
    
def post_product():
    dados = request.get_json()
    product = Product(**dados)
    db.session.add(product)
    db.session.commit()
    return {'message': 'Produto criado com sucesso'}, 201
