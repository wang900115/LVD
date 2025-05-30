class User:
    def __init__(self,username):
        self.username = username

    def Dict(self):
        return {
            "username": self.username
        }