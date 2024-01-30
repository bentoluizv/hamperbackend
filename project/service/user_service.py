# from ..models.user_model import User
# from ..models.mock_data import mock_users
from ..ext.database import db
from ..models.user_model import User


def get_all_users():
    users = User.query.all()
    return [user.to_dict() for user in users]


def post_user(user_data):
    new_user = User(
        firstname=user_data.get("firstname"),
        lastname=user_data.get("lastname"),
        email=user_data.get("email"),
    )
    db.session.add(new_user)
    db.session.commit()
    return {"message": "Usuário cadastrado com sucesso!"}, 201


def update_user(user_id, updated_data):
    user = get_one_user(user_id)
    if user is None:
        return {"error": f"Usuário com ID {user_id} não encontrado"}

    try:
        for key, value in updated_data.items():
            setattr(user, key, value)

        db.session.commit()
        return {"message": f"Usuário com ID {user_id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def delete_user(id):
    user = get_one_user(id)
    if user is None:
        return {"error": f"Usuário com ID {id} não encontrado"}

    try:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"Usuário com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def get_one_user(user_id):
    return user if (user := User.query.get(user_id)) else None
