from app.users.models import DBPost, DBUsers

class DB():
    dbUsers = DBUsers()
    dbPosts = DBPost()
    
db = DB()