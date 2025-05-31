from internal.domain.entities.token import TokenClaims
from internal.domain.interface.token import TokenInterface


class TokenUsecase:

    def __init__(self, usecase: TokenInterface):
        self.usecase = usecase

    def CreateToken(self, tokenClaims: TokenClaims) -> str:
        return self.usecase.CreateToken(tokenClaims)

    def ValidateToken(self, token: str) -> TokenClaims:
        return self.ValidateToken(token)

    def DeleteToken(self, token: str) -> None:
        return self.usecase.DeleteToken(token)
