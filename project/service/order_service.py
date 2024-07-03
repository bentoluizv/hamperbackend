from flask import abort

from project.ext.database import db
from project.models.client_model import Client
from project.models.order_model import Order
from project.models.product_model import Product
from project.models.restaurant_model import Restaurant

from ..utils.twilio_utils import send_whatsapp_message


def get_all_orders():
    return Order.query.all()


def save_client(order_data: dict):
    new_client = Client(
        client_name=order_data['client_name'], client_cellphone=order_data['client_cellphone'],
        client_address=order_data['client_address'], client_address_number=order_data['client_address_number'],
        client_address_complement=order_data['client_address_complement'], client_address_neighborhood=order_data['client_address_neighborhood'],
        client_zip_code=order_data['client_zip_code']
    )
    db.session.add(new_client)
    db.session.commit()


def post_order(order_data: dict):
    if not Restaurant.query.get(order_data['restaurant_id']):
        abort(404, f"Restaurante com ID {order_data['restaurant_id']} não encontrado.")

    if not all(Product.query.get(product_id) for product_id in order_data['products']):
        abort(404, "Um ou mais produtos não foram encontrados.")

    products = [Product.query.get(product_id) for product_id in order_data['products']]

    products_value = [product.value for product in products]

    save_client(order_data)

    client = Client.query.filter(Client.client_cellphone == order_data['client_cellphone']).first()
    if not client:
        abort(404, f"Cliente com telefone {order_data['client_cellphone']} não encontrado.")

    new_order = Order(
        client_id=client.id, restaurant_id=order_data['restaurant_id'], products=products, total_value=sum(products_value)
    )
    db.session.add(new_order)
    db.session.commit()

    send_whatsapp_message(new_order)

    return {"message": "Pedido cadastrado com sucesso!"}, 201


def get_one_order(order_id: int):
    return order if (order := Order.query.get(order_id)) else None


def update_order(id: int, updated_data: dict):
    order = get_one_order(id)

    if order is None:
        abort(404, error=f"Ordem com ID {id} não encontrado")

    try:
        for key, value in updated_data.items():
            if key == "products":
                value = [Product.query.get(product_id) for product_id in value]
            setattr(order, key, value)

        db.session.commit()
        return {"message": f"Ordem com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        abort(500, error=str(e))


def delete_one_order(id: int):
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
    
def total_order_value(order_data: dict):
    order_data