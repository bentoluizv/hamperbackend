def test_list_order_return_200(app_testing):
    order = app_testing.test_client()
    response = order.get('http://127.0.0.1:5000/api/v1/orders/')
    assert response.status_code == 200