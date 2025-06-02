from fastapi import APIRouter, Depends, Body, Request
from .....internal.adapter.fastapi.validator.user import RegistRequest, LoginRequest
from .....internal.adapter.fastapi.controller.user import UserController
from .....internal.adapter.fastapi.middleware.jwt.jwt import JWTMiddleware
import json
class UserRouter:

    def __init__(self, controller: UserController, jwt: JWTMiddleware):
        self.controller = controller

        self.router = APIRouter()

        self.router.add_api_route("/regist", self.regist, methods=["POST"])
        self.router.add_api_route("/login", self.login, methods=["POST"])
        self.router.add_api_route("/logout", self.logout, methods=["POST"], dependencies=[Depends(jwt)])

    def regist(self, request: RegistRequest):
        return self.controller.Register(request)

    async def login(self, request: LoginRequest):
        return self.controller.Login(request)

    def logout(self, request: Request):
        return self.controller.Logout(request)
