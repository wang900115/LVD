from abc import ABC, abstractmethod
from ....internal.domain.entities.token import TokenClaims


class TokenInterface(ABC):

    @abstractmethod
    def CreateToken(self, tokenClaims: TokenClaims) -> str:
        pass

    @abstractmethod
    def ValidateToken(self, token: str) -> TokenClaims:
        pass

    @abstractmethod
    def DeleteToken(self,token:str) -> None:
        pass
