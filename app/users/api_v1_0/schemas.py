from marshmallow import fields

from app.ext import marsh

class userSchema(marsh.Schema):
    id = fields.Integer()
    username = fields.String()
    mail = fields.String()

class postSchema(marsh.Schema):
    id = fields.Integer()
    user = fields.Integer()
    date = fields.DateTime
    content: fields.String()

