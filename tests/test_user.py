def test_list_user_return_200(app_testing):
    user = app_testing.test_client()
    response = user.get('http://127.0.0.1:5000/api/v1/users/')
    assert response.status_code == 200

def test_post_user_return_200(app_testing):
    client = app_testing.test_client()

    user_data = {
        "firstname": "João",
        "lastname": "Silva",
        "email": "joao.silva@example.com"
    }

    response = client.post('/api/v1/users/', json=user_data)
   
    assert response.status_code == 201