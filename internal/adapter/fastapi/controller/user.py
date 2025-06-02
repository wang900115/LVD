from internal.application.usecase.user import UserUsecase
from internal.application.usecase.token import TokenUsecase
from internal.domain.entities.user import User
from internal.domain.entities.token import TokenClaims
from internal.adapter.fastapi.validator.user import LoginRequest, LogoutRequest, RegistRequest
from internal.adapter.fastapi.response.json import JsonResponse
from internal.adapter.fastapi.response.message import Message
from datetime import datetime


class UserController:

    def __init__(self, userUsecase: UserUsecase, tokenUsecase: TokenUsecase, response: JsonResponse):
        self.userUsecase = userUsecase
        self.tokenUsecase = tokenUsecase
        self.response = response

    def Register(self, request: RegistRequest):
        try:
            user = User(request.username, request.password, request.email)
            resUser = self.userUsecase.CreateUser(user)
            return self.response.successWithData(Message.createSuccess,resUser)
        except Exception as e:
            return self.response.failWithError(Message.createFail, e)

    def Login(self, request: LoginRequest):
        try:
            resUser = self.userUsecase.Login(request.username, request.password)
            tokenClaims = TokenClaims(username=resUser, expires_at=datetime.now())
            token = self.tokenUsecase.CreateToken(tokenClaims)
            return self.response.successWithData(Message.loginSuccess,token)
        except Exception as e:
            return self.response.failWithError(Message.loginFail, e)

    def Logout(self, request: LogoutRequest):
        try:
            self.tokenUsecase.DeleteToken(request)
            return self.response.success(Message.logoutSuccess)
        except Exception as e:
            return self.response.failWithError(Message.logoutFail, e)
