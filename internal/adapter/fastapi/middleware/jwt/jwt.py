from internal.application.usecase.token import TokenUsecase

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.responses import JSONResponse

class JWTMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, tokenUsecase: TokenUsecase):
        super().__init__(app)
        self.tokenUsecase = tokenUsecase

    async def dispatch(self, request, call_next):
        try:
            token = self._extractToken(request)
            token_data = self.tokenUsecase.ValidateToken(token)
            
            request.state.username = token_data.username
            request.state.expires_at = token_data.expires_at
        
        except Exception as e:
            return JSONResponse(
                status_code=401,
                content={"message": "Unauthorized", "detail": str(e)}
            )
        
        return await call_next(request)
    
    def _extractToken(self, request: Request) -> str:
        authHeader = request.headers.get("Authorization")
        if not authHeader:
            raise ValueError("no token")
        
        if not authHeader.startswith("Bearer "):
            raise ValueError("invalid authorization format")
        
        return authHeader.replace("Bearer ","",1)