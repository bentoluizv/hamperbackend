from ..ext.database import db


class Restaurant(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(20), unique=True, nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    classification: float = db.Column(db.Float(precision=3), nullable=False)
    location: str = db.Column(db.String(120), nullable=False)
    url_image_logo: str = db.Column(db.String(), nullable=True)
    url_image_banner: str = db.Column(db.String(), nullable=True)
    products = db.relationship(
        "Product", backref="restaurant", lazy=True
    )

    def __init__(
        self,
        name,
        description,
        classification,
        location,
        url_image_logo,
        url_image_banner,
    ):
        self.name = name
        self.description = description
        self.classification = classification
        self.location = location
        self.url_image_logo = url_image_logo
        self.url_image_banner = url_image_banner

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "classification": self.classification,
            "location": self.location,
            "url_image_logo": self.url_image_logo,
            "url_image_banner": self.url_image_banner,
        }
