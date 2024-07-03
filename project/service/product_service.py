from flask import request
from ..ext.database import db
from ..models.product_model import Product


def get_all_products():
    return Product.query.all()


def post_product(product_data: dict):
    product_data = request.get_json()
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