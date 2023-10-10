from project.models.restaurant_model import Restaurant
from ..ext.database import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    value = db.Column(db.Float(precision=6), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    url_image = db.Column(db.String(), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(Restaurant.id))

    def __init__(self, name):
        self.name = name
