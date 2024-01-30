# from project.models.mock_data import mock_products
from flask import abort, request
from flask_restx import Resource

from project.service.product_service import (delete_product, get_all_products,
                                             get_one_product, post_product,
                                             update_product)


class ProductResource(Resource):
    def get(self):
        products = get_all_products()
        return {"products": products}, 200

    def post(self):
        try:
            product_data = request.json
            post_product(product_data)
            return {"message": "Produto cadastrado com sucesso!"}, 201
        except Exception as e:
            return {"error": str(e)}, 400


class ProductResourceID(Resource):
    def patch(self, id):
        try:
            product_data = request.json
            result = update_product(id, product_data)

            if "error" in result:
                abort(404, message=result["error"])

            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

    def get(self, id):
        if product := get_one_product(id):
            return {"restaurant": product.to_dict()}, 200  # type: ignore
        else:
            return {"error": f"Produto com ID {id} não encontrado."}, 404

    def delete(self, id):
        try:
            result = delete_product(id)

            if "error" in result:
                return {"error": result["error"]}, 404

            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500
