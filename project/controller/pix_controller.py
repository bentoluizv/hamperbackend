from flask import request
from flask_restx import Resource
from ..models.pix_model import Pix


class PixResource(Resource):
    
    def post(self):
        payload = request.json
        txid = payload.pop('txid')

        pix_model = Pix()
        response = pix_model.create_charge(txid, payload)

        return response