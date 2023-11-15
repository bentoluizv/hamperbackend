"""Dados estáticos para uso em desenvolvimento"""

mock_restaurants = [
    {"id": 1, "name": "Bóde do Nô",
     "description": "Descrição do restaurante",
     "classification": 4.9,
     "location": "Recife-PE",
     "url_image_logo": "url_logo",
     "url_image_banner": "url_banner"},
    {"id": 2, "name": "Imperador dos camarões",
     "description": "Descrição do restaurante", "classification": 4.8,
     "location": "Maceió-AL", "url_image_logo": "url_logo",
     "url_image_banner": "url_banner"},
    {"id": 3, "name": "Bar da Sogra",
     "description": "Descrição do restaurante",
     "classification": 4.1, "location": "Salvador-BA",
     "url_image_logo": "url_logo", "url_image_banner": "url_banner"},
    {"id": 4, "name": "Raspa Tácho",
     "description": "Descrição do restaurante",
     "classification": 4.8, "location": "Fortaleza-CE",
     "url_image_logo": "url_logo", "url_image_banner": "url_banner"},
    {"id": 5, "name": "Boi na Brasa",
     "description": "Descrição do restaurante",
     "classification": 4.9, "location": "Fortaleza-CE",
     "url_image_logo": "url_logo", "url_image_banner": "url_banner"}
]

mock_products = [
    {"id": 1, "name": "X-Bacon", "value": 20, "description": "Bacon",
     "url_image": "url_image", "restaurant_id": 1},
    {"id": 2, "name": "X-Picanha", "value": 20, "description": "Picanha",
     "url_image": "url_image", "restaurant_id": 2},
    {"id": 3, "name": "X-Salada", "value": 20, "description": "Salada",
     "url_image": "url_image", "restaurant_id": 3},
    {"id": 4, "name": "X-Frango", "value": 20, "description": "Frango",
     "url_image": "url_image", "restaurant_id": 4},
    {"id": 5, "name": "X-Batata", "value": 20, "description": "Batata",
     "url_image": "url_image", "restaurant_id": 5},
]

mock_users = [
    {"id": 1,
     "firstname": "Tony",
     "lastname": "Stark",
     "email": "ironman@icloud.com"},
    {"id": 2,
     "firstname": "Peter",
     "lastname": "Parker",
     "email": "spiderman@icloud.com"},
    {"id": 3,
     "firstname": "Bruce",
     "lastname": "Banner",
     "email": "hulk@icloud.com"},
    {"id": 4,
     "firstname": "Natasha",
     "lastname": "Romanoff",
     "email": "blackwidow@icloud.com"},
    {"id": 5,
     "firstname": "Steve",
     "lastname": "Rogers",
     "email": "captainamerica@icloud.com"}
]

mock_clients = [
    {"id": 1,
     "client_name": "Tony",
     "client_cellphone": "999999999",
     "client_address": "Avenida da Paz",
     "client_address_number": 123,
     "client_address_complement": "Casa A",
     "client_address_neighborhood": "Centro",
     "client_zip_code": "12345678"},
    {"id": 2,
     "client_name": "Peter",
     "client_cellphone": "3199999955",
     "client_address": "Avenida da Aricanduva",
     "client_address_number": 321,
     "client_address_complement": "Casa B",
     "client_address_neighborhood": "Centro",
     "client_zip_code": "87654321"},
     {"id": 3,
     "client_name": "Bruce",
     "client_cellphone": "3199999966",
     "client_address": "Avenida da Paulista",
     "client_address_number": 213,
     "client_address_complement": "Condomínio ABC",
     "client_address_neighborhood": "Centro",
     "client_zip_code": "12344321"}
]

mock_orders = [
    {
        "id": 1,
        "client_id": 1,
        "restaurant_id": 1,
        "products": [1,2]
    },
    {
        "id": 2,
        "client_id": 2,
        "restaurant_id": 2,
        "products": [3,4]
    },
    {
        "id": 3,
        "client_id": 3,
        "restaurant_id": 3,
        "products": [5]
    },
    {
        "id": 4,
        "client_id": 4,
        "restaurant_id": 2,
        "products": [1,2,3,4]
    }
]