from ..ext.database import db
from ..models.client_model import Client


def get_all_clients():
    clients = Client.query.all()
    return [client.to_dict() for client in clients]


def post_client(client_data):
    new_client = Client(
        client_name=client_data.get("client_name"),
        client_cellphone=client_data.get("client_cellphone"),
        client_address=client_data.get("client_address"),
        client_address_number=client_data.get("client_address_number"),
        client_address_complement=client_data.get("client_address_complement"),
        client_address_neighborhood=client_data.get(
            "client_address_neighborhood"),
        client_zip_code=client_data.get("client_zip_code")
    )
    db.session.add(new_client)
    db.session.commit()
    return {"message": "Cliente cadastrado com sucesso!"}


def update_client(id, updated_data):
    client = get_one_client(id)
    if client is None:
        return {"error": f"Cliente com ID {id} não encontrado"}

    try:
        for key, value in updated_data.items():
            setattr(client, key, value)

        db.session.commit()
        return {"message": f"Cliente com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def delete_client(id):
    client = get_one_client(id)
    if client is None:
        return {"error": f"Cliente com ID {id} não encontrado"}

    try:
        db.session.delete(client)
        db.session.commit()
        return {"message": f"CLiente com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def get_one_client(id):
    return client if (client := Client.query.get(id)) else None
