def test_list_product_return_200(app_testing):
    product = app_testing.test_client()
    response = product.get('http://127.0.0.1:5000/api/v1/products/')
    assert response.status_code == 200