class User:
    def __init__(self,username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def Dict(self):
        return {
            "username": self.username
        }