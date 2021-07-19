import datetime
import array

class Post:
    id: int
    user: int
    date: datetime
    content: str

class User:
    id: int
    username: str
    mail: str

class DBUsers:
    def __init__(self):
        users = {}

    def create(self, user: User):
        if user.id in self.users:
            return False
        else:
            self.users[user.id] = user
            return True
    
    def delete(self, userID: int):
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

    def read(self, userID: int):
        if userID in self.users:
            return (True, self.users[userID])
        else:
            return False

    def read(self, user: User):
        if user.id in self.users:
            return (True, self.users[user.id])
        else:
            return False


class DBPost:
    def __init__():
        posts = {}
    
    def create(self, post: Post):
        if post.id in self.posts:
            return False
        else:
            self.posts[post.id] = post
            return True
    
    def delete(self, postID: int):
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

    def read(self, postID: int):
        if postID in self.posts:
            return (True, self.posts[postID])
        else:
            return False

    def read(self, post: Post):
        if post.id in self.users:
            return (True, self.users[post.id])
        else:
            return False
    
    def deleteUserPost(self, userID: int):
        for post in self.posts:
            if post.user == userID:
                del self.posts[post.id]

