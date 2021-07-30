from datetime import datetime

def toDate(dateString): 
    return datetime.datetime.strptime(dateString, "%Y-%m-%d").date()

class Post:
    id: int
    user: int
    date: datetime
    content: str

    def __init__(self, id: int, user: int, date: datetime, content:str):
        self.id = id
        self.user = user
        self.date = date
        self.content = content

class User:
    id: int
    username: str
    mail: str

    def __init__(self, id:int, username:str, mail: str):
        self.id = id
        self.username = username
        self.mail = mail

class DBUsers:
    def __init__(self):
        self.users = []

    def create(self, user: User):
        if self.users:
            for usr in self.users:
                if usr.id == user.id:
                    return False
        self.users.append(user)
        return True
    
    def deleteByID(self, userID: int, db = None):
        if self.users:
            for i, user in enumerate(self.users):
                if user.id == userID:
                    del self.users[i]
                    # uncommet if need remove users post when user is deleted
                    # db.dbPost.deleteUserPost(userID)
                    return True
        return False
    
    def delete(self, user: User):
        if self.users:
            for i, usr in enumerate(self.users):
                if usr.id == user:
                    del self.users[i]
                    return True
        return False

    def update(self, user: User):
        if self.users:
            for i, usr in enumerate(self.users):
                if usr.id == user.id:
                    self.users[i] = user
                    return True
        return False

    def readByID(self, userID: int):
        if self.users:
            for user in self.users:
                print(user.id)
                if user.id == userID:
                    return (True, user)
        return (False, None)

    def read(self, user: User):
        if self.users:
            for usr in self.users:
                print(usr.id)
                if usr.id == user.id:
                    return (True, usr)
        return (False, None)

class DBPost:
    def __init__(self):
        self.posts = []
    
    def create(self, post: Post):
        if self.posts:
            for pst in self.posts:
                if pst.id == post.id:
                    return False
        self.posts.append(post)
        return True
    
    def deleteByID(self, postID: int):
        if self.posts:
            for i, post in enumerate(self.posts):
                if post.id == postID:
                    del self.posts[i]
                    return True
        return False
    
    def delete(self, post: Post):
        if self.posts:
            for i, pst in self.posts:
                if pst.id == post.id:
                    del self.posts[i]
                    return True
        return False

    def update(self, post: Post):
        if self.posts:
            for i, pst in enumerate(self.posts):
                if pst.id == post.id:
                    self.posts[i] = post
                    return True
        return False

    def readByID(self, postID: int):
        if self.posts:
            for post in self.posts:
                if post.id == postID:
                    return (True, post)
        return (False, None)

    def read(self, post: Post):
        if self.posts:
            for pst in self.posts:
                if pst.id == post.id:
                    return (True, self.posts[post.id])
        return (False, None)
    
    def deleteUserPost(self, userID: int):
        if self.posts:
            for i, post in enumerate(self.posts):
                if post.user == userID:
                    del self.posts[i]

