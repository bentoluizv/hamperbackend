# delivery-app-backend

DeliveryAPP BackEnd

## Descrição do projeto
O DeliveryAPP é um aplicativo de delivery que oferece aos restaurantes a capacidade de disponibilizar suas informações e produtos diretamente aos usuários do aplicativo. Os restaurantes podem integrar suas operações com o DeliveryAPP, permitindo uma experiência de pedidos de delivery contínua e conveniente para seus clientes.

# Endpoints

## Restaurant

### GET - /api/v1/restaurants
#### Response:
```
{
    "id": 1,
    "name": "Imperador dos camarões",
    "description": "Descrição do restaurante",
    "classification": 4.8,
    "location": "Maceió-AL",
    "url_image_logo": "url_logo",
    "url_image_banner": "url_banner"
}
```
### POST
#### Request Body:
```
{
    "name": "Imperador dos camarões",
    "description": "Descrição do restaurante",
    "classification": 4.8,
    "location": "Maceió-AL",
    "url_image_logo": "url_logo",
    "url_image_banner": "url_banner"
}
```
#### Response:
```
[
    {
        "message": "Restaurante criado com sucesso"
    },
    201
]
```

## Product

### GET - /api/v1/products
#### Response:
```
{
    "id": 1,
    "name": "X-Bacon",
    "value": 20.0,
    "description": "Bacon",
    "url_image": "url_image",
    "restaurant_id": 1
}
```
### POST
#### Request Body:
```
{
    "name": "X-Bacon",
    "value": 20,
    "description": "Bacon",
    "url_image": "url_image",
    "restaurant_id": 2
}
```
#### Response:
```
[
    {
        "message": "Produto criado com sucesso"
    },
    201
]
```


## Dynaconf
### Ambiente default
```
export FLASK_ENV=default
```
### Ambiente desenvolvimento
```
export FLASK_ENV=development
```
### Ambiente teste
```
export FLASK_ENV=testing
```
### Ambiente produção
```
export FLASK_ENV=production
```
## Makefile
### Rodar aplicação local
```
make up
```
