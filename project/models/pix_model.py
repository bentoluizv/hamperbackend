import base64
import json
import pyqrcode
from io import BytesIO
from PIL import Image
from flask import send_file
import requests
from ..utils.constants_pix import CLIENT_ID, CLIENT_SECRET, CERTIFICADO, URL_PROD

class Pix:

    def __init__(self):
        self.access_token = self.get_token()
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

    def get_token(self):
        auth = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode()
        
        headers = {
            'Authorization': f'Basic {auth}',
            'Content-Type': 'application/json'
        }

        payload = {"grant_type": "client_credentials"}

        response = requests.post(f'{URL_PROD}/oauth/token', headers=headers, data=json.dumps(payload), cert=CERTIFICADO)

        return json.loads(response.content).get('access_token')

    def create_qrcode(self, location_id):
        response = requests.get(f'{URL_PROD}/v2/loc/{location_id}/qrcode', headers=self.headers, cert=CERTIFICADO)
        
        return json.loads(response.content)

    def create_order(self, txid, payload):
        response = requests.put(f'{URL_PROD}/v2/cob/{txid}', data=json.dumps(payload), headers=self.headers, cert=CERTIFICADO)

        if response.status_code == 201:
            return json.loads(response.content)
        
        return {}

    def qrcode_generator(self, location_id):
        qrcode = self.create_qrcode(location_id)

        if 'qrcode' in qrcode:
            data_qrcode = qrcode['qrcode']

            url = pyqrcode.create(data_qrcode, error='H')
            img_io = BytesIO()
            url.png(img_io, scale=10)
            img_io.seek(0)

            return send_file(img_io, mimetype='image/png', as_attachment=False)
        else:
            print("Erro ao gerar QR Code.")
            return None

    def create_charge(self, txid, payload):
        order_response = self.create_order(txid, payload)
        
        if 'loc' in order_response:
            loc_data = order_response['loc']
            if 'id' in loc_data:
                location_id = loc_data['id']
                return self.qrcode_generator(location_id)
            else:
                print("Erro: ID do local não encontrado na resposta da ordem.")
        else:
            print("Erro: Local não encontrado na resposta da ordem.")

        return None
