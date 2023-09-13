from ..models.restaurant_model import Restaurant


def get_all_restaurants():
    return Restaurant.query.all()
