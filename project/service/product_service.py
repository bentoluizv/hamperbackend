# from ..models.mock_data import mock_products
from ..ext.database import db
from ..models.product_model import Product


def get_all_products():
    products = Product.query.all()
    return [product.to_dict() for product in products]


def post_product(product_data):
    new_product = Product(
        name=product_data.get("name"),
        value=product_data.get("value"),
        description=product_data.get("description"),
        url_image=product_data.get("url_image"),
        restaurant_id=product_data.get("restaurant_id")
    )
    db.session.add(new_product)
    db.session.commit()
    return {"message": "Product cadastrado com sucesso!"}, 201


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


def get_one_product(product_id):
    return product if (product := Product.query.get(product_id)) else None
