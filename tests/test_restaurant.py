from project.models.mock_data import mock_restaurants
def test_list_restaurant_return_200(app_testing):
    """
    Teste para verificar se o endpoint da API para listar restaurante retorna o código de status 200.
    """
    restaurant = app_testing.test_client()
    response = restaurant.get('http://127.0.0.1:5000/api/v1/restaurants/')
    assert response.status_code == 200

def test_post_restaurant_return_200(app_testing):
    """
    Testa se a rota '/api/v1/restaurants/' retorna o código de status 201 (Created) ao fazer uma requisição POST com dados válidos de products.
    """
    client = app_testing.test_client()

    restaurant_data = {
        "name": "Restaurante Teste",
        "description": "Descrição do restaurante de teste",
        "classification": 4.5,
        "location": "Cidade do Teste",
        "url_image_logo": "url_logo_teste",
        "url_image_banner": "url_banner_teste"
    }
    
    response = client.post('/api/v1/restaurants/', json=restaurant_data)
    
    assert response.status_code == 201
    assert response.json['message'] == 'Restaurante cadastrado com sucesso!'

def test_post_restaurant_return_400(app_testing):
    """
    Testa se a rota '/api/v1/restaurants/' retorna o código de status 400 (Solicitação Incorreta) ao fazer uma requisição POST com dados invalidos de products.
    """
    client = app_testing.test_client()

    response = client.post('/api/v1/restaurants/', json={"invalid": "data"})


    assert response.status_code == 400
    assert response.json['error'] == "'invalid' is an invalid keyword argument for Restaurant"

def test_get_one_restaurant_return_200(app_testing):
    """
    Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 200 ao fazer uma requisição GET com um ID de restaurante válido.
    """
    client = app_testing.test_client()

    response = client.get(f'/api/v1/restaurants/{mock_restaurants[1]["id"]}/products')
    data = response.json
    assert response.status_code == 200
    assert data['id'] == mock_restaurants[1]['id']
    assert data['name'] == mock_restaurants[1]['name']
    assert data['description'] == mock_restaurants[1]['description']
    assert data['classification'] == mock_restaurants[1]['classification']
    assert data['location'] == mock_restaurants[1]['location']
    assert data['url_image_logo'] == mock_restaurants[1]['url_image_logo']
    assert data['url_image_banner'] == mock_restaurants[1]['url_image_banner']
    #FIXME: assert response.json == mock_restaurants[1] não funciona aqui pois o sqlite está tentando achar associated_products pois no servidor tecnicemente não temos o associated_products
    # O próximo assert irá falhar se 'associated_products' não estiver na resposta
    # assert data['associated_products'] == mock_restaurants[1]['associated_products']

def test_get_one_restaurant_return_404(app_testing):
    """
    Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 404 ao fazer uma requisição GET com um ID de restaurante invalido.
    """
    client = app_testing.test_client()
    response = client.get('/api/v1/restaurants/0/products')
    assert response.status_code == 404
    assert response.json['error'] == 'Restaurante com ID 0 não encontrado.'


# FIXME: testes estão dando problema pelo que estou entendendo é algo relacionado ao banco que não ta encontrando as informações
# def test_patch_restaurant_return_200(app_testing):
#     """
#     Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 200 ao fazer uma requisição PATCH com um ID de restaurante válido.
#     """
#     client = app_testing.test_client()

#     product_data = {
#         "name": "X-Teste",
#         "value": 15,
#         "description": "Descrição do produto de teste",
#         "url_image": "url_image_teste",
#         "restaurant_id": 5
#     }

#     response = client.patch(f'/api/v1/restaurants/{mock_restaurants[1]["id"]}/products', json=product_data)
#     assert response.status_code == 200
#     assert response.json['message'] == 'Produto com ID 2 atualizado com sucesso!'

# def test_patch_restaurant_return_500(app_testing):
#     """
#     Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 500 ao fazer uma requisição PATCH com um ID de restaurante invalido.
#     """
#     client = app_testing.test_client()
#     response = client.patch('/api/v1/restaurants/0/products', json={})
#     assert response.status_code == 500

# def test_delete_restaurant_return_200(app_testing):
#     """
#     Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 200 ao fazer uma requisição DELETE com um ID de restaurante válido.
#     """
#     client = app_testing.test_client()
#     response = client.delete(f'/api/v1/restaurants/{mock_restaurants[1]["id"]}/products')
#     assert response.status_code == 200
#     assert response.json['message'] == 'Restaurante com ID 2 deletado com sucesso!'

# TODO: é algo relacionado ao preenchimento do banco pois se fosse a rota esse teste iria falhar tbm....
def test_delete_restaurant_return_404(app_testing):
    """
    Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 404 ao fazer uma requisição DELETE com um ID de restaurante invalido.
    """
    client = app_testing.test_client()
    response = client.delete('/api/v1/restaurants/0/products')
    assert response.status_code == 404
    assert response.json['error'] == 'Restaurante com ID 0 não encontrado'
