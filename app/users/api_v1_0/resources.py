from marshmallow.fields import DateTime
from app.common.error_handling import ObjectNotFound
from flask import request, Blueprint 
from flask_restful import Api, Resource
from app.db import db

from ..models import DBPost, DBUsers, User, Post
from .schemas import UserSchema, PostSchema

userPostBP = Blueprint('userPostBP', __name__)

userSchema = UserSchema()
postSchema = PostSchema()

api = Api(userPostBP)

class UserResource(Resource):
    def get(self, userID: int, username: str, mail: str):
        u = User(userID, username, mail)
        b, user = db.dbUsers.read(u)
        if b:
            return userSchema.dump(user), 200
        else:
            raise ObjectNotFound("Can't find user with id = " + str(userID))

    def post(self, userID: int, username: str, mail: str):
        user = User(userID, username, mail)
        b = db.dbUsers.create(user)
        if b:
            return {"msg": "User created"}, 200
        else:
            raise ObjectNotFound('User already exist')

    def put(self, userID: int, username: str, mail: str):
        user = User(userID, username, mail)
        b = db.dbUsers.update(user)
        if b:
            return {'msg': 'User ' + str(userID) + ' updated'}, 200
        else:
            raise ObjectNotFound("Can't find user with id = " + str(userID))

    def delete(self, userID: int, username: str, mail: str):
        user = User(userID, username, mail)
        b = db.dbUsers.delete(user)
        if b:
            return {'msg': 'User ' + str(userID) + ' deleted'}, 200
        else:
            raise ObjectNotFound("Can't find user with id = " + str(userID))

class PostResource(Resource):
    def get(self, postID: int):
        b, post = DBPost.readByID(postID)
        if b:
            return postSchema.dump(post), 200
        else:
            raise ObjectNotFound("Can't found post with ID = " + postID)

    def post(self, postID: int, user: int, date_str: str, content: str):
        date = DateTime(date_str)
        post = Post(postID, user, date, content)
        b = DBPost.create(post)
        if b:
            return {"msg": "Post created"}, 200
        else:
            raise ObjectNotFound("Post " + postID + "already exist")

    def update(self, postID: int, user: int, date_str: str, content: str):
        date = DateTime(date_str)
        post = Post(postID, user, date, content)
        b = DBPost.create(post)
        if b:
            return {"msg": "Post" + postID + "updated"}, 200
        else:
            raise ObjectNotFound("Can't found post with ID = " + postID)

    def delete(self, postID: int):
        b = DBPost.deleteByID(postID)
        if b:
            return {"msg": "Post " + postID + "deleted"}, 200
        else:
            raise ObjectNotFound("Can't found post with ID = " + postID)

# api.add_resource(UserResource, '/api/v1.0/get_user/<int:userID>', endpoint='user_resource')
api.add_resource(UserResource, '/api/v1.0/user/<int:userID>/<string:username>/<string:mail>', endpoint='user_resource')
api.add_resource(PostResource, '/api/v1.0/postID/<int:postID>', endpoint='post_resource')