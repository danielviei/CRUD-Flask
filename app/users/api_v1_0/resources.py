from datetime import datetime
from app.common.error_handling import ObjectNotFound
from flask import request, Blueprint 
from flask_restful import Api, Resource, reqparse
from app.db import db

from ..models import User, Post
from .schemas import *

userPostBP = Blueprint('userPostBP', __name__)

userSchema = UserSchema()
postSchema = PostSchema()

api = Api(userPostBP)

class UserResource(Resource):
    def get(self):
        return userSchema.dump(db.dbUsers.users, many=True)
    
    def post(self, userID: int = None):
        req = request.get_json(force=True, silent=True)
        user = User(req["id"], req["username"], req["mail"])
        b = db.dbUsers.create(user)
        if b:
            return {"msg": "User created"}, 200
        else:
            raise ObjectNotFound('User '+ str(req["id"]) + ' already exist')


class UserIDResource(Resource):
    def get(self, userID: int = None):
        b, user = db.dbUsers.readByID(userID)
        if b:
            return userSchema.dump(user), 200
        else:
            raise ObjectNotFound("Can't find user with id = " + str(userID))

    def put(self, userID: int = None):
        req = request.get_json(force=True, silent=True)
        user = User(userID, req["username"], req["mail"])
        b = db.dbUsers.update(user)
        if b:
            return {'msg': 'User ' + str(userID) + ' updated'}, 200
        else:
            raise ObjectNotFound("Can't find user with id = " + str(userID))

    def delete(self, userID: int = None):
        b = db.dbUsers.deleteByID(userID)
        if b:
            return {'msg': 'User ' + str(userID) + ' deleted'}, 200
        else:
            raise ObjectNotFound("Can't find user with id = " + str(userID))

class PostResource(Resource):
    def get(self):
        return postSchema.dump(db.dbPosts.posts, many = True)
    
    def post(self):
        req = request.get_json(force=True, silent=True)
        date = datetime.now()
        post = Post(req["id"], req["user"], date, req["content"])
        b = db.dbPosts.create(post)
        if b:
            return {"msg": "Post created"}, 200
        else:
            raise ObjectNotFound("Post " + str(req["id"]) + " already exist")


class PostIDResource(Resource):
    def get(self, postID: int):
        b, post = db.dbPosts.readByID(postID)
        if b:
            return postSchema.dump(post), 200
        else:
            raise ObjectNotFound("Can't found post with ID = " + str(postID))

    def put(self, postID: int):
        req = request.get_json(force=True, silent=True)
        date = datetime.now()
        post = Post(postID, req["user"], date, req["content"])
        b = db.dbPosts.update(post)
        if b:
            return {"msg": "Post " + str(postID) + " updated"}, 200
        else:
            raise ObjectNotFound("Can't found post with ID = " + str(postID))

    def delete(self, postID: int):
        b = db.dbPosts.deleteByID(postID)
        if b:
            return {"msg": "Post " + str(postID) + " deleted"}, 200
        else:
            raise ObjectNotFound("Can't found post with ID = " + str(postID))

api.add_resource(UserResource, '/api/v1.0/user', endpoint='user_id_resource')
api.add_resource(UserIDResource, '/api/v1.0/user/<int:userID>', endpoint='user_resource')
api.add_resource(PostResource, '/api/v1.0/post', endpoint='post_resource')
api.add_resource(PostIDResource, '/api/v1.0/post/<int:postID>/', endpoint='post_id_resource')