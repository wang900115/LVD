from abc import ABC, abstractmethod
from internal.domain.entities.user import User

class UserInterface(ABC):

    @abstractmethod
    def CreateUser(self, user: User)-> User:
        pass

    @abstractmethod
    def QueryUser(self, username: str)-> User:
        pass

    @abstractmethod
    def UpdateUser(self, user: User)-> User:
        pass

    @abstractmethod
    def DeleteUser(self, username: str)-> User:
        pass

    @abstractmethod
    def Login(self, username: str, password: str)-> User:
        pass