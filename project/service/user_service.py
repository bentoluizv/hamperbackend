from ..models.user_model import User


def get_all_users():
    return User.query.all()