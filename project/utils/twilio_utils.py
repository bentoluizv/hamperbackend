from twilio.rest import Client

def send_whatsapp_message(new_order):
  account_sid = 'AC07bda34115f9e874de261be356af10d4'
  auth_token = '874db9a2531b4bc72c0f4a867aab3fb8'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Pedido confirmado',
    to='whatsapp:+554799080127'
  )

  print(message.sid)