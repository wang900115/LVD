from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.responses import JSONResponse

class CORSMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, allow_origin: str = "*"):
        super().__init__(app)
        self.allow_origin = allow_origin
    
    async def dispatch(self, request: Request, call_next):

        if request.method == "OPTIONS":
            return JSONResponse(status_code=204, headers={
                "Access-Control-Allow-Origin": self.allow_origin,
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS, PUT, PATCH, DELETE",
                "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept, Authorization, token",
                "Access-Control-Expose-Headers": "Content-Length, Access-Control-Allow-Origin, Access-Control-Allow-Headers, Cache-Control, Content-Language, Content-Type",
                "Vary": "Origin",
            })
        
        response = await call_next(request)
        response.headers["Vary"] = "Origin"
        response.headers["Access-Control-Allow-Origin"] = self.allow_origin
        response.headers["Access-Control-Allow-Methods"] ="GET, POST, OPTIONS, PUT, PATCH, DELETE" 
        response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept, Authorization, token"
        response.headers["Access-Control-Expose-Headers"] = "Content-Length, Access-Control-Allow-Origin, Access-Control-Allow-Headers, Cache-Control, Content-Language, Content-Type"

        return response
