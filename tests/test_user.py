import datetime
from unittest.mock import Mock, patch


def test_list_user_return_200(app_testing, User_10):
    """
    Test if the '/api/v1/users/' route returns status code 200 and mock_users data.
    """
    user = app_testing.test_client()
    response = user.get("http://127.0.0.1:5000/api/v1/users/")
    assert response.status_code == 200
    for user in response.json:
        assert "firstname" in user
        assert "Firstname" in user["firstname"]


def test_post_user_return_200(app_testing):
    """
    Test if the '/api/v1/clients/' route returns status code 201 (Created) when making a POST request with valid User data.
    """
    client = app_testing.test_client()

    user_data = {
        "firstname": "João",
        "lastname": "Silva",
        "email": "joao.silva@example.com",
    }

    response = client.post("/api/v1/users/", json=user_data)

    assert response.status_code == 201
    assert response.json["message"] == "Usuário cadastrado com sucesso!"


def test_post_user_return_400(app_testing):
    """
    Test if the '/api/v1/users/' route returns status code 400 (Bad Request) when making a POST request with invalid user data.
    """
    client = app_testing.test_client()

    response = client.post("/api/v1/users/", json={"invalid": "data"})

    assert response.status_code == 400
    assert response.json["error"] == "'invalid' is an invalid keyword argument for User"


def test_get_one_user_return_200(app_testing, user):
    """
    Test if the '/api/v1/users/<int:id>/' route returns status code 200 when making a GET request with a valid User ID.
    """
    client = app_testing.test_client()
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    assert response.json["firstname"] == "Tony"


def test_get_one_user_return_404(app_testing):
    """
    Test if the '/api/v1/users/<int:id>/' route returns status code 404 when making a GET request with an invalid User ID.
    """
    client = app_testing.test_client()
    response = client.get("/api/v1/users/1")
    assert response.status_code == 404
    assert response.json["error"] == "Usuário com ID 1 não encontrado."


def test_patch_users_return_200(app_testing, user):
    """
    Test if the '/api/v1/clients/<int:id>/' route returns status code 200 when making a PATCH request with a valid User ID.
    """
    client = app_testing.test_client()

    user_data = {
        "firstname": "João",
        "lastname": "Silva",
        "email": "joao.silva@example.com",
    }

    response = client.patch("/api/v1/users/1", json=user_data)

    assert response.status_code == 200
    assert response.json["message"] == "Usuário com ID 1 atualizado com sucesso!"


def test_patch_users_return_500(app_testing):
    """
    Test if the '/api/v1/users/<int:id>/' route returns status code 500 when making a PATCH request with an invalid User ID.
    """
    client = app_testing.test_client()
    response = client.patch("/api/v1/users/1", json={})
    assert response.status_code == 500


def test_delete_client_return_200(app_testing, user):
    """
    Test if the '/api/v1/users/<int:id>/' route returns status code 200 when making a DELETE request with a valid User ID.
    """
    client = app_testing.test_client()
    response = client.delete("/api/v1/users/1")
    assert response.status_code == 200
    assert response.json["message"] == "Usuário com ID 1 deletado com sucesso."


def test_delete_client_return_404(app_testing):
    """
    Test if the '/api/v1/users/<int:id>/' route returns status code 404 when making a DELETE request with an invalid User ID.
    """
    client = app_testing.test_client()
    response = client.delete("/api/v1/users/1")
    assert response.status_code == 404
    assert response.json["error"] == "Usuário com ID 1 não encontrado"


@patch('project.utils.twilio_utils.whatsapp')
def test_send_whatsapp_message(mock_whatsapp, app_testing):
    """
    Test if the send_whatsapp_message function sends a message using the WhatsApp API correctly.
    """
    from project.utils.message_utils import send_whatsapp_message
    from project.models.order_model import Order

    # Arrange
    mock_order = Mock(spec=Order)
    mock_order.configure_mock(
        restaurant_id=1,
        client_id=1,
        products=[Mock(name='Product 1', value=10.0)],
        total_value=10.0,
        created_at=datetime.now()
    )
    mock_whatsapp.send_message.return_value = {'success': True}

    # Act
    send_whatsapp_message(mock_order)

    # Assert
    mock_whatsapp.send_message.assert_called_once()
    assert mock_whatsapp.send_message.call_args[0][0] == 'RECIPIENT_PHONE_NUMBER'
    assert 'Pedido Recebido!' in mock_whatsapp.send_message.call_args[0][1]
