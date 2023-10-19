from flask_restx import Resource

from project.service.product_service import get_all_products, post_product


class ProductResource(Resource):

    def get(self):
        products = get_all_products()
        return products, 200
    
    def post(self):
        product = post_product()
        return product, 200
