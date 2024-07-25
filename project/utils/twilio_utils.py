from flask_whatsapp import Whatsapp
from project.models.client_model import Client
from project.models.restaurant_model import Restaurant
import datetime

whatsapp = Whatsapp(
    phone_number_id="YOUR_WHATSAPP_PHONE_NUMBER",
    access_token="YOUR_ACCESS_TOKEN",
    bearer_token="YOUR_BEARER_TOKEN",
)

def send_whatsapp_message(new_order):
    restaurant = Restaurant.query.get(new_order.restaurant_id)
    client = Client.query.get(new_order.client_id)

    products_info = "\n".join([f"- {product.name} - R${product.value}" for product in new_order.products])
    for product in new_order.products:
        products_info += f"\n- {product.name} - R${product.value}"
    formatted_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = (
        f"📝 Pedido Recebido! \n"
        f"\n👤 Cliente: {client.client_name} \n"
        f"🍽️  Restaurante: {restaurant.name} \n"
        f"🛒 Produtos:\n{products_info} \n"
        f"\n💸 Valor Total: R${new_order.total_value} \n"
        f"📅 Data do Pedido: {formatted_time}"
    )

    recipient = "RECIPIENT_PHONE_NUMBER"
    try:
        response = whatsapp.send_message(recipient, body)
        print(response)
    except Exception as e:
        print(str(e))
