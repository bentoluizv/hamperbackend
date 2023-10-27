from flask import request

from ..models.user_model import User, db


def get_all_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'email': user.email
        }
        user_list.append(user_data)
    return user_list


def create_user():
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    user = User(firstname=firstname, lastname=lastname, email=email)
    db.session.add(user)
    db.session.commit()
    return {'message': 'User created'}, 201


def get_one_user(id):
    if user := User.query.get(id):
        return user.to_dict()
    else:
        return {'message': 'User not found'}, 404


def put_one_user(id):
    if user := User.query.get(id):
        data = request.get_json()
        user.firstname = data.get('firstname')
        user.lastname = data.get('lastname')
        user.email = data.get('email')
        return user.to_dict()
    else:
        return {'message': 'User not found'}, 404


def delete_one_user(id):
    if user := User.query.get(id):
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted'}
    else:
        return {'message': 'User not found'}, 404
