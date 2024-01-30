from ..ext.database import db


class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(20), nullable=False)
    lastname: str = db.Column(db.String(20), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }
