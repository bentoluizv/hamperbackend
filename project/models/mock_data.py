"""Dados estáticos para uso em desenvolvimento"""

mock_restaurants = [
    {"id": 1, "name": "Bóde do Nô", "description": "Descrrição do restaurante",
     "classification": 4.9, "location": "Recife-PE",
     "url_image_logo": "url_logo", "url_image_banner": "url_banner"},
    {"id": 2, "name": "Imperador dos camarões",
     "description": "Descrrição do restaurante", "classification": 4.8,
     "location": "Maceió-AL", "url_image_logo": "url_logo",
     "url_image_banner": "url_banner"},
    {"id": 3, "name": "Bar da Sogra",
     "description": "Descrrição do restaurante",
     "classification": 4.1, "location": "Salvador-BA",
     "url_image_logo": "url_logo", "url_image_banner": "url_banner"},
    {"id": 4, "name": "Raspa Tácho",
     "description": "Descrrição do restaurante",
     "classification": 4.8, "location": "Fortaleza-CE",
     "url_image_logo": "url_logo", "url_image_banner": "url_banner"},
    {"id": 5, "name": "Boi na Brasa",
     "description": "Descrrição do restaurante",
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
    {
        "id": 1,
        "client_name": "John Doe",
        "client_cellphone": "69999999999",
        "client_address": "1600 Amphitheatre Parkway",
        "client_address_number": 1600,
        "client_address_complement": "",
        "client_address_neighborhood": "Mountain View",
        "client_zip_code": "94043"
    },
    {
        "id": 2,
        "client_name": "Jane Smith",
        "client_cellphone": "69998887777",
        "client_address": "One Microsoft Way",
        "client_address_number": 1,
        "client_address_complement": "",
        "client_address_neighborhood": "Redmond",
        "client_zip_code": "98052"
    },
    {
        "id": 3,
        "client_name": "Alice Johnson",
        "client_cellphone": "69995554444",
        "client_address": "1600 Pennsylvania Avenue NW",
        "client_address_number": 1600,
        "client_address_complement": "",
        "client_address_neighborhood": "Washington",
        "client_zip_code": "20500"
    },
    {
        "id": 4,
        "client_name": "Bob Brown",
        "client_cellphone": "69992221111",
        "client_address": "221B Baker Street",
        "client_address_number": 221,
        "client_address_complement": "",
        "client_address_neighborhood": "London",
        "client_zip_code": "NW1 6XE"
    },
    {
        "id": 5,
        "client_name": "Eva Green",
        "client_cellphone": "69991112222",
        "client_address": "1600 Pennsylvania Avenue NW",
        "client_address_number": 1600,
        "client_address_complement": "",
        "client_address_neighborhood": "Washington",
        "client_zip_code": "20500"
    }
]

mock_orders = [
    {
        "id": 1,
        "client_id": 1,
        "restaurant_id": 1,
        "products": [1]
    },
    {
        "id": 2,
        "client_id": 2,
        "restaurant_id": 2,
        "products": [2, 3]
    },
    {
        "id": 3,
        "client_id": 3,
        "restaurant_id": 1,
        "products": [4]
    },
    {
        "id": 4,
        "client_id": 4,
        "restaurant_id": 2,
        "products": [5]
    },
    {
        "id": 5,
        "client_id": 5,
        "restaurant_id": 4,
        "products": [1, 2, 5]
    }
]