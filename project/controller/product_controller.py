from flask_restx import Api, Resource

from project.service.product_service import (delete_one_product,
                                             get_all_products, get_one_product,
                                             post_product, put_one_product)

api = Api()


class ProductResource(Resource):

    def get(self):
        products = get_all_products()
        return products, 200

    @api.doc(params={'name': 'Name of the product',
                     'value': 'Value of the product',
                     'description': 'Description of the product',
                     'url_image': 'URL image of the product',
                     'restaurant_id': 'ID of the restaurant'})
    def post(self):
        product = post_product()
        return product, 201


class ProductResourceId(Resource):
    def get(self, id):
        if product := get_one_product(id):
            return product, 200

    @api.doc(params={'id': 'ID of the product',
                     'name': 'Name of the product',
                     'value': 'Value of the product',
                     'description': 'Description of the product',
                     'url_image': 'URL image of the product',
                     'restaurant_id': 'ID of the restaurant'})
    def put(self, id):
        product = put_one_product(id)
        return product, 200

    @api.doc(params={'id': 'ID of the product'})
    def delete(self, id):
        product = delete_one_product(id)
        return product, 200
