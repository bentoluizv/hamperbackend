from flask_restx import Resource

from project.models.pix_model import Pix


class TokenResource(Resource):

    def post(self):
        pix_model = Pix()
        response = pix_model.get_token()

        return response 