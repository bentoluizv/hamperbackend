from flask_restx import Resource
from project.service.product_service import get_all_products


class ProductResource(Resource):

    def get(self):
        products = get_all_products()
        return products, 200
