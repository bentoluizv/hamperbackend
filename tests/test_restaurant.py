def test_list_restaurant_return_200(app_testing):
    restaurant = app_testing.test_client()
    response = restaurant.get('http://127.0.0.1:5000/api/v1/restaurants/')
    assert response.status_code == 200