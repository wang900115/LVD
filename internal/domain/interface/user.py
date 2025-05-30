from abc import ABC, abstractmethod
from internal.adapter.sqlachemy.validtor.user import UserValidator
from internal.domain.entities.user import User

class UserInterface(ABC):

    @abstractmethod
    def CreateUser(self, user: UserValidator)-> User:
        pass

    @abstractmethod
    def QueryUser(self, id: int)-> User:
        pass

    @abstractmethod
    def UpdateUser(self, user: UserValidator)-> User:
        pass

    @abstractmethod
    def DeleteUser(self, username: str)-> User:
        pass

    @abstractmethod
    def Login(self, username: str, password: str)-> User:
        pass

    @abstractmethod
    def Logout(self, username: str, password: str)-> User:
        pass