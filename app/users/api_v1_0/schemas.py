from marshmallow import fields

from app.ext import marsh

class UserSchema(marsh.Schema):
    id = fields.Integer()
    username = fields.String()
    mail = fields.String()

class PostSchema(marsh.Schema):
    id = fields.Integer()
    user = fields.Integer()
    date = fields.DateTime()
    content: fields.String()

