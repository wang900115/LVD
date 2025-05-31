from internal.application.usecase.user import UserUsecase
from internal.application.usecase.token import TokenUsecase
from internal.domain.entities.user import User
from internal.domain.entities.token import TokenClaims
from internal.adapter.fastapi.validator.user import LoginRequest, LogoutRequest, RegistRequest
from datetime import datetime


class UserController:

    def __init__(self, userUsecase: UserUsecase, tokenUsecase: TokenUsecase):
        self.userUsecase = userUsecase
        self.tokenUsecase = tokenUsecase

    def Register(self, request: RegistRequest):
        user = User(request.username, request.password, request.email)
        resUser = self.userUsecase.CreateUser(user)
        pass

    def Login(self, request: LoginRequest):
        resUser = self.userUsecase.Login(request.username, request.password)
        tokenClaims = TokenClaims(username=resUser, expires_at=datetime.now())
        token = self.tokenUsecase.CreateToken(tokenClaims)
        pass

    def Logout(self, request: LogoutRequest):
        self.tokenUsecase.DeleteToken(request)
        pass
