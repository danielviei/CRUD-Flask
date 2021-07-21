from marshmallow.fields import DateTime
from app.common.error_handling import ObjectNotFound
from flask import request, Blueprint 
from flask_restful import Api, Resource

from ..models import DBPost, DBUsers, User, Post
from .schemas import UserSchema, PostSchema

userPostBP = Blueprint('userPostBP', __name__)

userSchema = UserSchema()
postSchema = PostSchema()

api = Api(userPostBP)

class UserResource(Resource):
    def get(self, userID: int):
        b, user = DBUsers.readByID(userID=userID)
        if b:
            return userSchema.dump(user), 200
        else:
            raise ObjectNotFound("Can't find user with id = " + userID)

    def post(self, userID: int, username: str, mail: str):
        user = User(userID, username, mail)
        b = DBUsers.create(user)
        if b:
            return {"msg": "User created"}, 200
        else:
            raise ObjectNotFound('User already exist')

    def update(self, userID: int, username: str, mail: str):
        user = User(userID, username, mail)
        b = DBUsers(user)
        if b:
            return {'msg': 'User ' + userID + ' updated'}, 200
        else:
            raise ObjectNotFound("Can't find user with id = " + userID)

    def delete(self, userID: int):
        b = DBUsers.deleteByID(userID)
        if b:
            return {'msg': 'User ' + userID + ' deleted'}, 200
        else:
            raise ObjectNotFound("Can't find user with id = " + userID)

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

api.add_resource(UserResource, '/api/v1.0/userID/<int:userID>', endpoint='user_resource')
#add resource PostResource