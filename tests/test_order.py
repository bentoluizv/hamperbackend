def test_list_order_return_200(app_testing):
    order = app_testing.test_client()
    response = order.get('http://127.0.0.1:5000/api/v1/orders/')
    assert response.status_code == 200

def test_post_order_return_200(app_testing):
    client = app_testing.test_client()

    order_data = {
        "client_id": 4,
        "restaurant_id": 5,
        "products": [5],
        "created_at": "2024-03-11 10:00:00"
    }

    response = client.post('/api/v1/orders/', json=order_data)
   
    assert response.status_code == 201