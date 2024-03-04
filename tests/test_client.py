def test_list_restaurant_return_200(app_testing):
    client = app_testing.test_client()
    response = client.get('http://127.0.0.1:5000/api/v1/clients/')
    assert response.status_code == 200