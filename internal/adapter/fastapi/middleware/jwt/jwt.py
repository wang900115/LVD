from ......internal.application.usecase.token import TokenUsecase
from ......internal.adapter.fastapi.response.json import JsonResponse
from ......internal.adapter.fastapi.response.message import Message
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class JWTMiddleware(BaseHTTPMiddleware):
    def __init__(self, tokenUsecase: TokenUsecase, response: JsonResponse):

        self.tokenUsecase = tokenUsecase
        self.response = response

    async def dispatch(self, request: Request, call_next):
        try:
            token = self._extractToken(request)
            token_data = self.tokenUsecase.ValidateToken(token)
            

            request.state.token = token
            request.state.username = token_data.username
            request.state.expires_at = token_data.expires_at
        
        except Exception as e:
            return self.response.authFailWithError(Message.accessDenied,e)
        
        return await call_next(request)
    
    def _extractToken(self, request: Request) -> str:
        authHeader = request.headers.get("Authorization")
        if not authHeader:
            raise ValueError("no token")
        
        if not authHeader.startswith("Bearer "):
            raise ValueError("invalid authorization format")
        
        return authHeader.replace("Bearer ","",1)