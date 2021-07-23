import datetime
import array

from marshmallow.fields import DateTime

class Post:
    id: int
    user: int
    date: datetime
    content: str

    def __init__(self, id: int, user: int, date: DateTime, content:str):
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
    # users: dict[int, dict[str, object]]
    users = {
            0 : {"id": 0, "username": "daniel", "mail":"danielvieiucv@gmail.com"}
            }

    def create(self, user: User):
        if user.id in self.users:
            return False
        else:
            self.users[user.id] = user
            return True
    
    def deleteByID(self, userID: int):
        if userID in self.users:
            del self.users[userID]
            return True
        else:
            return False
    
    def delete(self, user: User):
        if user.id in self.users:
            del self.users[user.id]
            return True
        else:
            return False

    def update(self, user: User):
        if user.id in self.users:
            self.users[user.id] = user
            return True
        else:
            return False

    def readByID(userID: int):
        if userID in DBUsers.users:
            return (True, DBUsers.users[userID])
        else:
            return (False, None)

    def read(self, user: User):
        if user.id in self.users:
            return (True, self.users[user.id])
        else:
            return (False, None)


class DBPost:
    posts = {
            0 : {"id": 0, "user": 0, "date": "01/01/2021", "content": "Test Post"}
            }
    
    def create(self, post: Post):
        if post.id in self.posts:
            return False
        else:
            self.posts[post.id] = post
            return True
    
    def deleteByID(self, postID: int):
        if postID in self.posts:
            del self.posts[postID]
            return True
        else:
            return False
    
    def delete(self, post: Post):
        if post.id in self.posts:
            del self.posts[post.id]
            return True
        else:
            return False

    def update(self, post: Post):
        if post.id in self.posts:
            self.posts[post.id] = post
            return True
        else:
            return False

    def readByID(self, postID: int):
        if postID in self.posts:
            return (True, self.posts[postID])
        else:
            return (False, None)

    def read(self, post: Post):
        if post.id in self.users:
            return (True, self.users[post.id])
        else:
            return False
    
    def deleteUserPost(self, userID: int):
        for post in self.posts:
            if post.user == userID:
                del self.posts[post.id]

