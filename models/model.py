from .core import db
from sqlalchemy import func


class IdqUser(db.Model):


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime(), default=func.now())
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=False)

    def self_serialize(self):
        user_serializer = {}
        user_serializer['id'] = self.id
        user_serializer['name'] = self.name
        user_serializer['phone'] = self.phone
        user_serializer['active'] = self.active
        user_serializer['created_on'] = self.created_on.strftime("%m-%d-%YT%H:%M:%S")
        return user_serializer


class IdqRole(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime(), default=func.now())
    role_name = db.Column(db.String(40), unique=True)
    description = db.Column(db.String(40))

    def self_serialize(self):
        role_serializer = {}
        role_serializer['id'] = self.id
        role_serializer['role_name'] = self.role_name
        role_serializer['description'] = self.description
        role_serializer['created_on'] = self.created_on.strftime("%m-%d-%YT%H:%M:%S")
        return role_serializer



class IdqUserRole(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime(), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('idq_user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('idq_role.id'))
    roles = db.relationship("IdqRole", backref="idquserrole")
    users = db.relationship("IdqUser", backref="idquserrole")

    def self_serialize(self):
        user_role_serializer = {}
        user_role_serializer['id'] = self.id
        user_role_serializer['role_id'] = self.role_id
        user_role_serializer['user_id'] = self.user_id
        user_role_serializer['roles'] = self.roles.self_serialize()
        user_role_serializer['users'] = self.users.self_serialize()
        user_role_serializer['created_on'] = self.created_on.strftime("%m-%d-%YT%H:%M:%S")
        return user_role_serializer
