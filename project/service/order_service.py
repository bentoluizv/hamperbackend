from decimal import Decimal
from flask import abort
from efipay import EfiPay
from project.ext.database import db
from project.models.client_model import Client
from project.models.order_model import Order
from project.models.pix_model import Pix
from project.models.product_model import Product
from project.models.restaurant_model import Restaurant
from project.utils.generate_unique_txid import generate_unique_txid
from ..utils.constants_pix import CLIENT_ID, CLIENT_SECRET, CERTIFICATE, URL_PROD
from ..utils.twilio_utils import send_whatsapp_message


options = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'certificate': CERTIFICATE,
    'url': URL_PROD
}

efi = EfiPay(options)

def get_all_orders():
    return Order.query.all()


def save_client(order_data: dict):
    required_fields = ['client_name', 'client_cellphone', 'client_cpf', 'client_address', 
                       'client_address_number', 'client_address_complement', 
                       'client_address_neighborhood', 'client_zip_code']
    
    for field in required_fields:
        if field not in order_data:
            abort(400, f"Campo '{field}' é obrigatório.")


    new_client = Client(
        client_name=order_data['client_name'], 
        client_cellphone=order_data['client_cellphone'],
        client_cpf=order_data['client_cpf'],
        client_address=order_data['client_address'], 
        client_address_number=order_data['client_address_number'],
        client_address_complement=order_data['client_address_complement'], 
        client_address_neighborhood=order_data['client_address_neighborhood'],
        client_zip_code=order_data['client_zip_code']
    )
    db.session.add(new_client)
    db.session.commit()


def post_order(order_data: dict):
    if not Restaurant.query.get(order_data['restaurant_id']):
        abort(404, f"Restaurante com ID {order_data['restaurant_id']} não encontrado.")
    
    if "current_time" in order_data:
        current_time = datetime.strptime(order_data["current_time"], "%H:%M:%S").time()
    elif current_time is None:
        current_time = datetime.now().time()
    
    if restaurant.horario_funcionamento and restaurant.horario_fechamento:
        if not (restaurant.horario_funcionamento <= current_time <= restaurant.horario_fechamento):
            abort(403, "O restaurante está fora do horário de funcionamento.")
        
    if not all(Product.query.get(product["product_id"]) for product in order_data["products"]):
        abort(404, "Um ou mais produtos não foram encontrados.")

    products = [Product.query.get(product_id) for product_id in order_data['products']]
    products_value = [product.value for product in products]

    client = Client.query.filter(Client.id == order_data.get('client_id')).first()

    if not client:
        save_client(order_data)
        
        client = Client.query.filter(Client.client_cellphone == order_data['client_cellphone']).first()
        if not client:
            abort(404, f"Cliente com telefone {order_data['client_cellphone']} não encontrado.")
    else:
        client.client_name = order_data.get('client_name', client.client_name)
        client.client_cellphone = order_data.get('client_cellphone', client.client_cellphone)
        client.client_cpf = order_data.get('client_cpf', client.client_cpf)
        client.client_address = order_data.get('client_address', client.client_address)
        client.client_address_number = order_data.get('client_address_number', client.client_address_number)
        client.client_address_complement = order_data.get('client_address_complement', client.client_address_complement)
        client.client_address_neighborhood = order_data.get('client_address_neighborhood', client.client_address_neighborhood)
        client.client_zip_code = order_data.get('client_zip_code', client.client_zip_code)

        db.session.commit()

    new_order = Order(
        client_id=client.id,
        restaurant_id=order_data['restaurant_id'],
        total_value=sum(products_value),
        products=products,
        payment=order_data['payment']
    )

    db.session.add(new_order)
    db.session.commit()

    send_whatsapp_message(new_order)

    if order_data['payment'] == 'Pix':
        pix_model = Pix()
        
        body = {
        "calendario": {
            "expiracao": 3600
        },
        "devedor": {
            "cpf": f"{client.client_cpf}",
            "nome": f"{client.client_name}"
        },
        "valor": {
            "original": f"{Decimal(sum(products_value)).quantize(Decimal('0.00'))}"
        },
        "chave": "afe37274-6de9-4c91-8ffe-9830dbe8c1a6",
        "solicitacaoPagador": "Cobrança dos serviços prestados."
    }

        txid = generate_unique_txid()

        info_pix = pix_model.create_charge(txid, body)
        return info_pix
    
    return None

def get_one_order(order_id: int):
    return order if (order := Order.query.get(order_id)) else None


def update_order(id: int, updated_data: dict):
    order = get_one_order(id)

    if order is None:
        return {"error": f"Ordem com ID {id} não encontrado."}

    try:
        for key, value in updated_data.items():
            if key == "products":
                value = [Product.query.get(product_id) for product_id in value]
            setattr(order, key, value)

        db.session.commit()
        return {"message": f"Ordem com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

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
    pass
