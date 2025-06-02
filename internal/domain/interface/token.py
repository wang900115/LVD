from abc import ABC, abstractmethod
from ....internal.domain.entities.token import TokenClaims


class TokenInterface(ABC):

    @abstractmethod
    async def CreateToken(self, tokenClaims: TokenClaims) -> str:
        pass

    @abstractmethod
    async def ValidateToken(self, token: str) -> TokenClaims:
        pass

    @abstractmethod
    async def DeleteToken(self,token:str) -> None:
        pass
