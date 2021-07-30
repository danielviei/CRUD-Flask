from marshmallow import fields

from app.ext import ma

class UserSchema(ma.Schema):
    id = fields.Integer()
    username = fields.String()
    mail = fields.String()

class PostSchema(ma.Schema):
    id = fields.Integer()
    user = fields.Integer()
    date = fields.DateTime()
    content = fields.String()

