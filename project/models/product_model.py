from ..ext.database import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    value = db.Column(db.Float(precision=6), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    url_image = db.Column(db.String(), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False, unique=True)
    restaurant = db.relationship('Restaurant', backref=db.backref('Product', uselist=False))


    def __init__(self, name, value, description, url_image, restaurant_id):
        self.name = name
        self.value = value
        self.description = description
        self.url_image = url_image
        self.restaurant_id= restaurant_id
