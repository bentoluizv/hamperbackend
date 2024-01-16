from flask import abort

from project.ext.database import db
from project.models.client_model import Client
from project.models.order_model import Order
from project.models.product_model import Product
from project.models.restaurant_model import Restaurant

# from .twilio_service import send_whatsapp_message


def get_all_orders():
    orders = Order.query.all()
    return [order.to_dict() for order in orders]


def post_order(client_id, restaurant_id, product_ids):
    if not Client.query.get(client_id):
        abort(404, f"Cliente com ID {client_id} não encontrado.")

    if not Restaurant.query.get(restaurant_id):
        abort(404, f"Restaurante com ID {restaurant_id} não encontrado.")

    if not all(Product.query.get(product_id) for product_id in product_ids):
        abort(404, "Um ou mais produtos  nao foram encontrados.")

    products = [Product.query.get(product_id) for product_id in product_ids]
    new_order = Order(
        client_id=client_id, restaurant_id=restaurant_id, products=products
    )
    db.session.add(new_order)
    db.session.commit()

    # send_whatsapp_message(new_order)

    return {"message": "Pedido cadastrado com sucesso!"}, 201


def get_one_order(order_id):
    return order if (order := Order.query.get(order_id)) else None


def update_order(id, updated_data):
    order = get_one_order(id)
    if order is None:
        abort(404, error=f"Ordem com ID {id} não encontrado")

    try:
        for key, value in updated_data.items():
            setattr(order, key, value)

        db.session.commit()
        return {"message": f"Ordem com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        abort(500, error=str(e))


def delete_one_order(id):
    order = get_one_order(id)
    if order is None:
        return {"error": f"Ordem com ID {id} não encontrado"}

    try:
        db.session.delete(order)
        db.session.commit()
        return {"message": f"Ordem com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
