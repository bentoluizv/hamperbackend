def test_list_client_return_200(app_testing):
    client = app_testing.test_client()
    response = client.get('http://127.0.0.1:5000/api/v1/clients/')
    assert response.status_code == 200

def test_post_client_return_200(app_testing):
    client = app_testing.test_client()

    client_data = {
        "client_name": "Maria Oliveira",
        "client_cellphone": "69996666666",
        "client_address": "Rua do Teste, 123",
        "client_address_number": 123,
        "client_address_complement": "Apto 101",
        "client_address_neighborhood": "Bairro do Teste",
        "client_zip_code": "12345-678"
    }

    response = client.post('/api/v1/clients/', json=client_data)
   
    assert response.status_code == 201


