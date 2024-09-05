import requests
from project.models.client_model import Client
from project.models.restaurant_model import Restaurant
import datetime

# Defina suas credenciais e IDs
PHONE_NUMBER_ID = "xxxxxxxx" 
# token will expire 23h
ACCESS_TOKEN = "xxxxxxxxxxx"
# Numero que deve vir do pedido acredito que o order já tenha isso
RECIPIENT_PHONE_NUMBER = "xxxxxxxxxx"

def send_whatsapp_message(new_order):
    restaurant = Restaurant.query.get(new_order.restaurant_id)
    client = Client.query.get(new_order.client_id)

    products_info = "\n".join([f"- {product.name} - R${product.value}" for product in new_order.products])
    formatted_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = (
        f"📝 Pedido Recebido! \n"
        f"\n👤 Cliente: {client.client_name} \n"
        f"🍽️ Restaurante: {restaurant.name} \n"
        f"🛒 Produtos:\n{products_info} \n"
        f"\n💸 Valor Total: R${new_order.total_value} \n"
        f"📅 Data do Pedido: {formatted_time}"
    )

    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_PHONE_NUMBER,
        "type": "text",
        "text": {
            "body": body
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print("mensagem enviada com sucesso:", response.json())
    except requests.exceptions.RequestException as e:
        print("Erro ao enviar mensagem:", e)