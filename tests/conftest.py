import os

import pytest

from project import create_app_wsgi
from project.ext.database import db
from sqlalchemy import Engine,event
from project.models.user_model import User
from project.models.restaurant_model import Restaurant
from project.models.product_model import Product
from project.models.client_model import Client
from project.models.order_model import Order
from project.models.mock_data import mock_users, mock_restaurants, mock_products , mock_clients, mock_orders


@pytest.fixture
def app_testing():
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app_wsgi()
    with app.app_context():
        db.create_all()
        seeding_database()

    yield app

    with app.app_context():
        db.drop_all()

# Define o pragma de chaves estrangeiras para conexões de banco de dados SQLite. (no momento deixarei desativado)
# @event.listens_for(Engine, 'connect')
# def set_sqlite_pragma(dbapi_connection, connection_record):
#     """
#     Define o pragma de chaves estrangeiras para conexões de banco de dados SQLite.

#     Args:
#         dbapi_connection: O objeto de conexão com o banco de dados.
#         connection_record: O objeto de registro de conexão.
#     """
#     cursor = dbapi_connection.cursor()
#     cursor.execute('PRAGMA foreign_keys=ON')
#     cursor.close()


def seeding_database():
    for user_data in mock_users:
        user = User(**user_data)
        db.session.add(user)
    
    for restaurant_data in mock_restaurants:
        restaurant = Restaurant(**restaurant_data)
        db.session.add(restaurant)
    
    for product_data in mock_products:
        product = Product(**product_data)
        db.session.add(product)
    
    for client_data in mock_clients:
        client = Client(**client_data)
        db.session.add(client)

    for order_data in mock_orders:       

        # Adicionar produtos ao pedido
        products = [Product.query.get(id) for id in order_data['products']]
        
        order = Order(
                id=order_data["id"],
                client_id=order_data["client_id"],
                restaurant_id=order_data["restaurant_id"],
                products=products
        )

        db.session.add(order)

    db.session.commit()

