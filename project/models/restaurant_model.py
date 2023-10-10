from ..ext.database import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    classification = db.Column(db.Float(precision=3), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    url_image_logo = db.Column(db.String(), nullable=True)
    url_image_banner = db.Column(db.String(), nullable=True)
    products = db.relationship(
        "Product", backref="restaurant", lazy=True, cascade="do nothing"
    )

    def __init__(self, name):
        self.name = name
