# from project.models.restaurant_model import Restaurant

from ..ext.database import db

products_restaurants = db.Table(
    "products_restaurants",
    db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
    db.Column("restaurant_id", db.Integer, db.ForeignKey("restaurant.id")),
)


class Product(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(40), nullable=False, unique=False)
    value: float = db.Column(db.Float(precision=6), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    url_image: str = db.Column(db.String(), nullable=True)
    restaurant_id: int = db.Column(
        db.Integer, db.ForeignKey("restaurant.id"), nullable=False
    )
    associated_restaurants = db.relationship(
        "Restaurant", secondary=products_restaurants, backref="associated_products"
    )

    def __init__(self, name, value, description, url_image, restaurant_id):
        self.name = name
        self.value = value
        self.description = description
        self.url_image = url_image
        self.restaurant_id = restaurant_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "description": self.description,
            "url_image": self.url_image,
            "restaurant_id": self.restaurant_id,
        }
