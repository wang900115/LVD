from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

import logging

class LoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, logger: logging.Logger):
        super().__init__(app)
        self.logger = logger

    async def dispatch(self, request: Request, call_next):
        body = await request.body()
        async def receive():
            return {"type": "http.request", "body": body}
        request._receive = receive
        response = await call_next(request)
        self.logger.info( f"{request.client.host} {request.method} {request.url} {response.status_code}")
        return response
