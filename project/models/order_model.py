from datetime import datetime

from project.models.client_model import Client
from project.models.restaurant_model import Restaurant

from ..ext.database import db

order_product_association = db.Table(
    "order_product_association",
    db.Column("order_id", db.Integer, db.ForeignKey("order.id")),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
)


class Order(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    client_id: int = db.Column(db.Integer, db.ForeignKey(Client.id))
    restaurant_id: int = db.Column(db.Integer, db.ForeignKey(Restaurant.id))
    products = db.relationship(
        "Product",
        secondary=order_product_association,
        backref=db.backref("orders", lazy="dynamic"),
    )
    client = db.relationship("Client", lazy=True)
    restaurant = db.relationship("Restaurant", lazy=True)

    def __init__(self, client_id, restaurant_id, products=None):
        self.client_id = client_id
        self.restaurant_id = restaurant_id
        self.products = products or []

    def to_dict(self):
        return {
            "id": self.id,
            "client": {
                "id": self.client_id,
                "client_name": self.client.client_name,
                "client_cellphone": self.client.client_cellphone,
                "client_address": self.client.client_address,
                "client_address_number": self.client.client_address_number,
                "client_address_complement": self.client.client_address_complement,
                "client_address_neighborhood": self.client.client_address_neighborhood,
                "client_zip_code": self.client.client_zip_code,
            },
            "restaurant": {
                "id": self.restaurant_id,
                "restaurant_name": self.restaurant.name,
                # "restaurant_cellphone": self.restaurant.cellphone,
            },
            "products": [product.to_dict() for product in self.products],
        }
