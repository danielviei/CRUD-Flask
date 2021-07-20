from app.common.error_handling import ObjectNoFound
from flask import request, Blueprint 
from flask_restful import Api, Resource

from ..models import DBUsers, User, Post
from .schemas import UserSchema, PostSchema

userPostBP = Blueprint('userPostBP', __name__)

userSchema = UserSchema()
postSchema = PostSchema()

api = Api(userPostBP)

class UserResource(Resource):
    def get(self, user: User):
        b, use = DBUsers.read(user)
        if b:
            ret = userSchema.dump(use)
        else:
            raise ObjectNoFound('El usuario no existe')
        return ret

#make post, delete and update methods

#create class PostResource with CRUD methods

api.add_resource(UserResource, '/api/v1.0/user/', endpoint='userResource')
#add resource PostResource