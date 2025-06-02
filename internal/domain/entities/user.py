class User:
    def __init__(self,username, password, email,id=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def Dict(self):
        return {
            "id": self.id,
            "username": self.username
        }