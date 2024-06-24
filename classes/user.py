#!/usr/bin/env python

# Import package
from flask_restful import Resource
from flask import request, current_app
from models import User
from schemas import user_schema, users_schema


# Api endpoint
class UserApi(Resource):

    # 1 - Function to get User
    def get(self, id=None):
        if not id:
            users = User.query.all()
            return users_schema.dump(users), 200
        else:
            user = User.query.get(id)
            if not user:
                return "User not in database", 404
            return user_schema.dump(user), 200

    # 2 - Function to create new plant
    def post(self):
            mail = request.json['mail']
            existing_user = User.query.filter(User.mail == mail).one_or_none()
            if existing_user is None:
                new_user = user_schema.load(request.json, session=current_app.config['db'].session)
                current_app.config['db'].session.add(new_user)
                current_app.config['db'].session.commit()
                return user_schema.dump(new_user), 201
            else:
                return "The user {} exist already in db with id {}".format(mail,existing_user.id), 400

    # 3 - Function to create or update plant
    def put(self, id):
        existing_user = User.query.get(id)
        if existing_user is None:
            return {"message": "User not found"}, 404
        updated_user = user_schema.load(request.json, instance=existing_user, session=current_app.config['db'].session) # to update the plant use instance=existing_plant, if not a new plant is created
        current_app.config['db'].session.add(updated_user)
        current_app.config['db'].session.commit()
        return user_schema.dump(updated_user), 201

    # 4 - Function to delete plant
    def delete(self, id):
        user_to_delete = User.query.get(id)
        if user_to_delete is None:
            return {"message": "User not found"}, 404
        current_app.config['db'].session.delete(user_to_delete)
        current_app.config['db'].session.commit()
        return {"message": "User has been deleted"}, 204