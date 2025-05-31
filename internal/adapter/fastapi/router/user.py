from fastapi import APIRouter
from internal.adapter.fastapi.controller.user import UserController


class UserRouter:

    def __init__(self, controller: UserController):
        self.controller = controller

        self.router = APIRouter()

        self.router.add_api_route("/regist", self.regist, methods=["POST"])
        self.router.add_api_route("/login", self.login, methods=["POST"])
        self.router.add_api_route("/logout", self.logout, methods=["POST"])

    def regist(self, request):
        return self.controller.Register(request)

    def login(self, request):
        return self.controller.Login(request)

    def logout(self, request):
        return self.controller.Logout(request)
