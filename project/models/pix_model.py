import base64
import json
import requests

from ..utils.constants_pix import CLIENT_ID, CLIENT_SECRET, CERTIFICATE, URL_PROD
from ..utils.generate_unique_txid import generate_unique_txid


class Pix:
    
    def __init__(self):
        self.access_token = self.get_token()
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }


    def get_token(self):
        auth = f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()
        
        headers = {
            'Authorization': f'Basic {base64.b64encode(auth).decode()}',
            'Content-Type': 'application/json'
        }

        payload = {"grant_type": "client_credentials"}

        response = requests.post(f'{URL_PROD}/oauth/token', headers=headers, data=json.dumps(payload), cert=CERTIFICATE)

        return response.json().get('access_token')


    def create_order(self, txid, payload):
        try:
            response = requests.put(f'{URL_PROD}/v2/cob/{txid}', data=json.dumps(payload), headers=self.headers, cert=CERTIFICATE)

            if response.status_code == 201:
                return response.json()

            return {
                "error": "Erro ao criar o pedido",
                "status_code": response.status_code,
                "response": response.text
            }

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return {"error": "Erro ao conectar com a API", "exception": str(e)}


    def create_charge(self, txid, payload):
        order_response = self.create_order(txid, payload)

        if "error" in order_response:
            if "txid_duplicado" in order_response["response"]:
                new_txid = generate_unique_txid()
                return self.create_charge(new_txid, payload)
            return order_response

        pix_copia_e_cola = order_response.get('pixCopiaECola')

        if not pix_copia_e_cola:
            print("Pix Copia e Cola não foi encontrado.")
            return {"error": "Pix Copia e Cola não foi retornado"}

        pix_base64 = base64.b64encode(pix_copia_e_cola.encode()).decode()
        return {
            "pixCopiaECola": pix_copia_e_cola,
            "pixBase64": pix_base64
        }
    