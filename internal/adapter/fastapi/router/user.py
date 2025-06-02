from fastapi import APIRouter, Depends, Body, Request
from .....internal.adapter.fastapi.validator.user import RegistRequest, LoginRequest
from .....internal.adapter.fastapi.controller.user import UserController
from .....internal.adapter.fastapi.depend.jwt.jwt import JWTDependency
from .....internal.application.usecase.token import TokenUsecase
class UserRouter:

    def __init__(self, controller: UserController, tokenUsecase: TokenUsecase):
        self.controller = controller

        self.router = APIRouter()

        self.router.add_api_route("/regist", self.regist, methods=["POST"])
        self.router.add_api_route("/login", self.login, methods=["POST"])
        self.router.add_api_route("/logout", self.logout, methods=["POST"], dependencies=[Depends(JWTDependency(tokenUsecase))])

    def regist(self, request: RegistRequest):
        return self.controller.Register(request)

    async def login(self, request: LoginRequest):
        return self.controller.Login(request)

    def logout(self, request: Request):
        return self.controller.Logout(request)
