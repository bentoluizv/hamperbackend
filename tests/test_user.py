def test_list_user_return_200(app_testing):
    user = app_testing.test_client()
    response = user.get('http://127.0.0.1:5000/api/v1/users/')
    assert response.status_code == 200

def test_post_user(app_testing):
    user = app_testing.test_client()
    response = user.post('http://127.0.0.1:5000/api/v1/users/', json = {"firstname": "user",
    "lastname": "Stark",
    "email": "teste@teste.com"})
    assert response.status_code == 201