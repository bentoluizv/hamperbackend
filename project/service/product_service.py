from flask import request
from ..ext.database import db
from typing import Dict, Optional
from ..models.product_model import Product

def get_all_products(has_gluten, has_lactose, is_vegan, is_vegetarian):
    query = Product.query
    if has_gluten:
        query = query.filter(Product.has_gluten == has_gluten)
    if has_lactose:
        query = query.filter(Product.has_lactose == has_lactose)
    if is_vegan:
        query = query.filter(Product.is_vegan == is_vegan)
    if is_vegetarian:
        query = query.filter(Product.is_vegetarian == is_vegetarian)

    products = query.all()
    return products

def post_product(product_data: dict):
    product_data = request.get_json()

    valid_food_types = ["Italiana", "Japonesa", "Árabe", "Chinesa", "Brasileira", "Mexicana", "Lanches", "Pizza", "Doces"]
    
    if product_data.get("food_type") not in valid_food_types:
        raise ValueError(f"Tipo de comida inválido. Permitidos: {', '.join(valid_food_types)}")
    
    product = Product(**product_data)
    db.session.add(product)
    db.session.commit()

def get_one_product(product_id: int):
    return product if (product := Product.query.get(product_id)) else None


def update_product(id: int, updated_data: dict):
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

def delete_product(id: int):
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
