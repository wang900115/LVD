from internal.application.usecase.user import UserUsecase
from internal.application.usecase.token import TokenUsecase
from internal.domain.entities.user import User
from internal.domain.entities.token import Token

class UserController:

    def __init__(self, userUsecase: UserUsecase, tokenUsecase: TokenUsecase):
        self.userUsecase = userUsecase
        self.tokenUsecase = tokenUsecase
        
    def Login(self, request):
        try:
            user = self.userUsecase.Login(request.username, request.password)
        except Exception as e:
    
    def Logout(self, request):
        try:
            user = self.userUsecase.Logout(request.username)
        except Exception as e:
            