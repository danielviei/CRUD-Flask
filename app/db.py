from app.users.models import *

class DB():
    dbUsers = DBUsers()
    dbPosts = DBPost()
    
db = DB()