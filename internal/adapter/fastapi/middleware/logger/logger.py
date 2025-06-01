from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class LoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, logger):
        super().__init__(app)
        self.logger = logger

    async def dispatch(self, request: Request, call_next):
        body = await request.body()

        async def receive():
            return {"type": "http.request", "body": body}

        request._receive = receive

        response = await call_next(request)

        self.logger.info(
            "Request",
            extra={
                "ip": request.client.host,
                "method": request.method,
                "url": str(request.url),
                "status_code": response.status_code,
                "body": body.decode("utf-8") if body else "",
            },
        )

        return response
