from fastapi import Request, HTTPException
from ......internal.application.usecase.token import TokenUsecase

def JWTDependency(tokenUsecase: TokenUsecase):
    def verify(request: Request):
        auth = request.headers.get("authorization")
        if not auth or not auth.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid or missing Authorization header")

        token = auth.replace("Bearer ", "", 1)
        try:
            token_data = tokenUsecase.ValidateToken(token)
        except Exception as e:
            raise HTTPException(status_code=401, detail="Invalid token")

        # Attach to request.state for controller to use
        request.state.token = token
        request.state.username = token_data.username
        request.state.expires_at = token_data.expires_at

        return token_data

    return verify
