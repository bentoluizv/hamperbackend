from flask import request
from flask_restx import Api, Resource

from project.service.user_service import (create_user, delete_one_user,
                                          get_all_users, get_one_user,
                                          put_one_user)

from ..models.user_model import User, db

api = Api()


class UserResource(Resource):

    def get(self):
        users = get_all_users()
        return users, 200

    def post(self):
        user, status = create_user()
        return user, status


class UserResourceId(Resource):

    def get(self, id):
        if user := get_one_user(id):
            return user, 200
        else:
            return {'message': 'User not found'}, 404

    @api.doc(params={'id': 'ID of the user',
                     'firstname': 'Firstname of the user',
                     'lastname': 'Lastname of the user',
                     'email': 'Email of the user'})
    def put(self, id):
        user = put_one_user(id)
        db.session.commit()
        return user, 200

    @api.doc(params={'id': 'ID of the user'})
    def delete(self, id):
        if user := delete_one_user(id):
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted'}
        else:
            return {'message': 'User not found'}, 404
