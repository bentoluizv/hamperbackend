from flask import abort, request
from flask_restx import Resource

from project.service.client_service import (delete_client, get_all_clients,
                                            get_one_client, post_client,
                                            update_client)


class ClientResource(Resource):
    def get(self):
        clients = get_all_clients()
        return {"clients": clients}, 200

    def post(self):
        try:
            client_data = request.json
            post_client(client_data)
            return {"message": "Cliente cadastrado com sucesso!"}, 201
        except Exception as e:
            return {"error": str(e)}, 400


class ClientResourceID(Resource):
    def patch(self, id):
        try:
            client_data = request.json
            result = update_client(id, client_data)

            if "error" in result:
                abort(404, message=result["error"])

            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

    def get(self, id):
        if client := get_one_client(id):
            return {"client": client.to_dict()}, 200  # type: ignore
        else:
            return {"error": f"Cliente com ID {id} não encontrado."}, 404

    def delete(self, id):
        try:
            result = delete_client(id)

            if "error" in result:
                return {"error": result["error"]}, 404

            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500
