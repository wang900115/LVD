from fastapi import FastAPI

from internal.adapter.fastapi.router.user import UserRouter
from internal.adapter.fastapi.router.stream import StreamRouter
from internal.adapter.fastapi.middleware.cors.cors import CORSMiddleware
from internal.adapter.fastapi.middleware.secure_header.secure_header import SecureHeaderMiddleware
from internal.adapter.fastapi.middleware.jwt.jwt import JWTMiddleware
from internal.adapter.fastapi.middleware.logger.logger import LoggerMiddleware

app = FastAPI()


userRouter = UserRouter(JWTMiddleware).router
streamRouter = StreamRouter().router

app.add_middleware(CORSMiddleware)
app.add_middleware(SecureHeaderMiddleware)
app.add_middleware(LoggerMiddleware)

app.include_router(userRouter,prefix="/api/v1/user", tags=["user"])
app.include_router(streamRouter,prefix="/api/v1/stream", tags=["stream"])

for route in app.routes:
    print(route)
