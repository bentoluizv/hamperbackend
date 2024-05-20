import factory
from factory.alchemy import SQLAlchemyModelFactory
from datetime import datetime

from project.models.client_model import Client
from project.ext.database import db
from project.models.order_model import Order
from project.models.product_model import Product
from project.models.restaurant_model import Restaurant
from project.models.user_model import User


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    firstname = factory.Sequence(lambda n: f'Firstname{n}')
    lastname = factory.Sequence(lambda n: f'Lastname{n}')
    email = factory.Sequence(lambda n: f'email{n}@test.com')

class ClientFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Client
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    client_name = factory.Sequence(lambda n: f'Client{n}')
    client_cellphone = factory.Sequence(lambda n: f'123456789{n}')
    client_address = factory.Sequence(lambda n: f'Street{n}')
    client_address_number = factory.Sequence(lambda n: n)
    client_address_complement = factory.Sequence(lambda n: f'Complement{n}')
    client_address_neighborhood = factory.Sequence(lambda n: f'Neighborhood{n}')
    client_zip_code = factory.Sequence(lambda n: f'Zip{n}')

class RestaurantFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Restaurant
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f'Restaurant{n}')
    classification = factory.Sequence(lambda n: n)
    location = factory.Sequence(lambda n: f'Location{n}')
    url_image_logo = factory.Sequence(lambda n: f'Url{n}')
    url_image_banner = factory.Sequence(lambda n: f'Url{n}')
    # tem que ver como fazer as relações entre os factors restaurante tem um relacionamento com produtos
    products = factory.RelatedFactory('project.factories.ProductFactory', 'restaurant')

class ProductFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f'Product{n}')
    description = factory.Sequence(lambda n: f'Description{n}')
    price = factory.Sequence(lambda n: n)
    url_image = factory.Sequence(lambda n: f'Url{n}')
    # TODO: o relacionamento com o restaurante 
    restaurant = factory.SubFactory(RestaurantFactory)
    restaurant_id = factory.LazyAttribute(lambda obj: obj.restaurant.id)

class OrderFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Order
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    created_at = factory.LazyFunction(datetime.now)
    client_id = factory.SubFactory(ClientFactory)
    # TODO: o relacionamento com o restaurante 
    restaurant = factory.SubFactory(RestaurantFactory)
    restaurant_id = factory.LazyAttribute(lambda obj: obj.restaurant.id)
    total_value = factory.Sequence(lambda n: n * 10.0)
    # TODO: uma lista de produtos
    products = factory.List([factory.SubFactory(ProductFactory) for _ in range(5)])







