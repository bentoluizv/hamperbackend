from flask_restx import Resource

from script_populate_db import populate_db_mock_restaurant


class UtilsResource(Resource):

    def get(self):
        restaurants = populate_db_mock_restaurant()
        return {"message": "Populate db executado com sucesso!"}, 200