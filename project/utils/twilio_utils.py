import requests
from project.models.client_model import Client
from project.models.restaurant_model import Restaurant
import datetime

# Defina suas credenciais e IDs
PHONE_NUMBER_ID = "371872426011780" 
# token will expire 23h
ACCESS_TOKEN = "EAAHZAr2QDoRwBO0TYK6KnwI8FGEYuTyxb5GoTvi9vHml9cppZCbu8a7uyhZBxNcVxbYwj6ti47MndRFJZB7X0ItANJGZAe2mQXhGtWP0W1ZBd5LqexVjpcZCgx9dfgFDfrInpN1KiyzOWncX5oosFmx10FJvXgrJzP3B37bBAEFRiAW6rhaC6PxNfEyc5EIUYxEi32OFD3IKVBthAGOREGJ"
# Testar para ver se ele consegue pegar o proprio numero do cliente e enviar...
RECIPIENT_PHONE_NUMBER = "5581983019618"

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