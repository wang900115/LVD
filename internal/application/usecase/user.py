from internal.domain.interface.user import UserInterface
from internal.domain.entities.user import User
from internal.adapter.sqlachemy.model.user import UserTable
from internal.adapter.sqlachemy.validtor.user import UserValidator

class UserUsecase:
    def __init__(self, usecase: UserInterface):
        self.usecase = usecase

    def CreateUser(self, user: UserValidator) -> User:
        return self.usecase.CreateUser(user)
    
    def DeleteUser(self, username: str)-> User:
        return self.usecase.DeleteUser(username)

    def QueryUser(self, username: str)-> UserTable:
        return self.usecase.QueryUser(username)
    
    def UpdateUser(self, user: UserValidator)-> User:
        return self.usecase.UpdateUser(user)
    
    def Login(self,username: str, password: str) -> User :
        return self.usecase.Login(username, password)
    
    def Logout(self,username: str) -> User :
        return self.usecase.Logout(username)