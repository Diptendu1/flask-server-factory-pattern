import requests
import logging
import json
from sqlalchemy.orm import sessionmaker
from flask import jsonify, request
from app import db
from models.model import IdqUser
from models.model import IdqUserRole
from models.model import IdqRole

logger = logging.getLogger("app.access")


class ControllerObject:

    def first(self):
        logger.info("HERE")
        return "first API"

    async def get_json(self, url):
        async with requests.get(url) as response:
            assert response.status == 200
            return await response.json()

    def insert_data_ex(self):
        role = IdqRole(name="role2", description="Role description")
        db.session.add(role)
        db.session.commit()
        return_map = {"message": "added data to roles"}
        return return_map

    def add_role(self):
        role1 = IdqRole(name="role1", description="Role description")
        role2 = IdqRole(name="role2", description="Role description")
        role3 = IdqRole(name="role3", description="Role description")
        role4 = IdqRole(name="role4", description="Role description")
        db.session.add(role1)
        db.session.add(role2)
        db.session.add(role3)
        db.session.add(role4)
        db.session.commit()
        return_map = {"message": "added data to roles"}
        return return_map

    def add_user(self):
        user = IdqUser(name="name1", email="dip@dip.com", phone="4561", password="dfdfd", active=True)
        user1 = IdqUser(name="name2", email="dip2@dip.com", phone="4562", password="dfdfd", active=True)
        user2 = IdqUser(name="name3", email="dip3@dip.com", phone="4563", password="dfdfd", active=True)
        user3 = IdqUser(name="name4", email="dip4@dip.com", phone="4564", password="dfdfd", active=True)
        db.session.add(user)
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.commit()
        return_map = {"message": "added data to roles"}
        return return_map

    def get_all_users(self):
        user_roles = IdqUserRole.query.all()
        return_map = {}
        return_list = []
        for user_role in user_roles:
            # print(user_role.to_dict(show=['id','users', 'roles']))
            return_list.append(user_role.self_serialize())

        return_map['result'] = return_list
        return return_map

    def add_user_role(self):
        request_data = request.get_json()
        user_id = request_data['user_id']
        role_id = request_data['role_id']
        user = IdqUser.query.get(user_id)
        role = IdqRole.query.get(role_id)
        user_role_obj = IdqUserRole(roles=role, users=user)
        db.session.add(user_role_obj)
        db.session.commit()
        return "true"

    def get_user_details_by_id(self):
        user_id = request.args.get('user_id')
        user_details = IdqUser.query.get(int(user_id))
        return_map = {}
        return_map["user_details"] = user_details.self_serialize()
        return return_map

    @classmethod
    def change_username(cls):
        request_data = request.get_json()
        user_id = request_data['user_id']
        username = request_data['username']
        user = IdqUser.query.get(user_id)
        user_obj = user.self_serialize()
        old_name = user_obj['name']
        user.name = username
        db.session.add(user)
        db.session.commit()
        return_map = {}
        return_map['output'] = 'Successful'
        return return_map
