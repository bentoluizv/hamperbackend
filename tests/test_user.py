from project.models.mock_data import mock_users

def test_list_user_return_200(app_testing):
    """
    Testa se a rota '/api/v1/users/' retorna o código de status 200 e os dados contidos em mock_users.
    """
    user = app_testing.test_client()
    response = user.get('http://127.0.0.1:5000/api/v1/users/')
    assert response.status_code == 200
    assert response.json == mock_users

def test_post_user_return_200(app_testing):
    """
    Testa se a rota '/api/v1/clients/' retorna o código de status 201 (Created) ao fazer uma requisição POST com dados válidos de Usuário.
    """
    client = app_testing.test_client()
    
    user_data = {
        "firstname": "João",
        "lastname": "Silva",
        "email": "joao.silva@example.com"
    }
    
    response = client.post('/api/v1/users/', json=user_data)
    
    assert response.status_code == 201
    assert response.json['message'] == 'Usuário cadastrado com sucesso!'

def test_post_user_return_400(app_testing):
    """
    Testa se a rota '/api/v1/users/' retorna o código de status 400 (Solicitação Incorreta) ao fazer uma requisição POST com dados invalidos de usuario.
    """
    client = app_testing.test_client()
    
    response = client.post('/api/v1/users/', json={"invalid": "data"})
    
    assert response.status_code == 400
    assert response.json['error'] == "'invalid' is an invalid keyword argument for User"

def test_get_one_user_return_200(app_testing):
    """
    Testa se a rota '/api/v1/users/<int:id>/' retorna o código de status 200 ao fazer uma requisição GET com um ID de Usuário válido.
    """
    client = app_testing.test_client()
    response = client.get(f'/api/v1/users/{mock_users[1]["id"]}')
    assert response.status_code == 200
    assert response.json == mock_users[1]

def test_get_one_user_return_404(app_testing):
    """
    Testa se a rota '/api/v1/users/<int:id>/' retorna o código de status 404 ao fazer uma requisição GET com um ID de Usuário invalido.
    """
    client = app_testing.test_client()
    response = client.get('/api/v1/users/0')
    assert response.status_code == 404
    assert response.json['error'] == 'Usuário com ID 0 não encontrado.'

def test_patch_users_return_200(app_testing):
    """
    Testa se a rota '/api/v1/clients/<int:id>/' retorna o código de status 200 ao fazer uma requisição PATCH com um ID de Usuario válido.
    """
    client = app_testing.test_client()

    user_data = {
        "firstname": "João",
        "lastname": "Silva",
        "email": "joao.silva@example.com"
    }

    response = client.patch(f'/api/v1/users/{mock_users[1]["id"]}', json=user_data)

    assert response.status_code == 200
    assert response.json['message'] == 'Usuário com ID 2 atualizado com sucesso!'

def test_patch_users_return_500(app_testing):
    """
    Testa se a rota '/api/v1/users/<int:id>/' retorna o código de status 500 ao fazer uma requisição PATCH com um ID de Usuario invalido.
    """
    client = app_testing.test_client()
    response = client.patch('/api/v1/users/0', json={})
    assert response.status_code == 500

def test_delete_client_return_200(app_testing):
    """
    Testa se a rota '/api/v1/users/<int:id>/' retorna o código de status 200 ao fazer uma requisição DELETE com um ID de cliente válido.
    """
    client = app_testing.test_client()
    response = client.delete(f'/api/v1/users/{mock_users[1]["id"]}')
    assert response.status_code == 200
    assert response.json['message'] == 'Usuário com ID 2 deletado com sucesso.'

def test_delete_client_return_404(app_testing):
    """
    Testa se a rota '/api/v1/users/<int:id>/' retorna o código de status 404 ao fazer uma requisição DELETE com um ID de cliente invalido.
    """
    client = app_testing.test_client()
    response = client.delete('/api/v1/users/0')
    assert response.status_code == 404
    assert response.json['error'] == 'Usuário com ID 0 não encontrado'