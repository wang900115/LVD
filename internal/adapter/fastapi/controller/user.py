from internal.application.usecase.user import UserUsecase
from internal.application.usecase.token import TokenUsecase
from internal.domain.entities.user import User
from internal.domain.entities.token import Token
from internal.adapter.fastapi.validator.user import LoginRequest, LogoutRequest, RegistRequest


class UserController:

    def __init__(self, userUsecase: UserUsecase, tokenUsecase: TokenUsecase):
        self.userUsecase = userUsecase
        self.tokenUsecase = tokenUsecase

    def Register(self, request: RegistRequest):
        pass

    def Login(self, request: LoginRequest):
        pass

    def Logout(self, request: LogoutRequest):
        pass
