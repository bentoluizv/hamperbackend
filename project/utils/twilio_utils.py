from twilio.rest import Client as ClientTwilio
from project.models.client_model import Client
from project.models.restaurant_model import Restaurant


def send_whatsapp_message(new_order):
  restaurant_query = Restaurant.query.filter(Restaurant.id == new_order.restaurant_id)
  client_query = Client.query.filter(Client.id == new_order.client_id)

  restaurant = restaurant_query.first()
  client = client_query.first()

  products_info = ""
  for product in new_order.products:
      products_info += f"\n- {product.name} - R${product.value}"

  formatted_time = new_order.created_at.strftime("%d-%m-%Y - %H:%M:%S")
  
  body = (f"📝 Pedido Recebido! \n"
          f"\nNúmero do pedido: {new_order.id} \n"
          f"\n👤 Cliente: {client.client_name} \n"
          f"Telefone: {client.client_cellphone} \n"
          f"Endereço: {client.client_address} \n"
          f"Bairro: {client.client_address_neighborhood} \n"
          f"Número: {client.client_address_number} \n"
          f"Complemento: {client.client_address_complement} \n"
          f"CEP: {client.client_zip_code}\n "
          f"\n🍽️  Restaurante: {restaurant.name} \n"
          f"🛒 Produtos: {products_info} \n"
          f"\n💸 Valor Total: R${new_order.total_value} \n"
          f"📅 Data do Pedido: {formatted_time}")

  try:
    account_sid = 'AC07bda34115f9e874de261be356af10d4'
    auth_token = '051223feaed4bf531f4071e9cca86a2b'
    client = ClientTwilio(account_sid, auth_token)

    message = client.messages.create(
      from_='whatsapp:+14155238886',
      body=body,
      to='whatsapp:+554799366596'
    )
  
  except Exception as e:
    print(str(e))