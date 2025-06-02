from fastapi import FastAPI
import uvicorn

#  config
from ....pkg.config.config import AppConfig
from ....pkg.logger.logger import Logger
from ....pkg.env.env import EnvConfig
#  adapter
from ....internal.adapter.redispool.redis import RedisPool
from ....internal.adapter.sqlalchemy.sqlalchemy import Mysql
from ....internal.adapter.gcs.gcs import GCS
#  implement
from ....internal.adapter.implement.token import TokenImplement
from ....internal.adapter.implement.user import UserImplement
from ....internal.adapter.implement.voice import VoiceImplement
#  usecase
from ....internal.application.usecase.token import TokenUsecase
from ....internal.application.usecase.user import UserUsecase
from ....internal.application.usecase.voice import VoiceUsecase
#  fastapi
from ....internal.adapter.fastapi.controller.user import UserController
from ....internal.adapter.fastapi.controller.stream import StreamController
from ....internal.adapter.fastapi.router.user import UserRouter
from ....internal.adapter.fastapi.router.stream import StreamRouter
from ....internal.adapter.fastapi.middleware.cors.cors import CORSMiddleware
from ....internal.adapter.fastapi.middleware.jwt.jwt import JWTMiddleware
from ....internal.adapter.fastapi.middleware.logger.logger import LoggerMiddleware
from ....internal.adapter.fastapi.middleware.secure_header.secure_header import SecureHeaderMiddleware
from ....internal.adapter.fastapi.response.json import JsonResponse
from ....internal.adapter.fastapi.response.stream import StreamResponse


class App:
    def __init__(self):
        self.app = FastAPI()
    
    def Setup(self):
        
        env = EnvConfig("C:\\Users\\a0970\\2025\\2025 04-06\\LVD\\config\\.env")
        config = AppConfig("C:\\Users\\a0970\\2025\\2025 04-06\\LVD\\config\\app.yaml")
        logger = Logger(config.log)
        mysql = Mysql(config.mysql)
        redis = RedisPool(config.redis)
        gcs = GCS(env.BUCKET_NAME)


        jsonResponser = JsonResponse()
        streamResponser = StreamResponse()
        tokenUsecase = TokenUsecase(TokenImplement(redis, env.BASE_SECRET , config.jwt))
        userUsecase = UserUsecase(UserImplement(mysql))
        voiceUsecase = VoiceUsecase(VoiceImplement(mysql))

        userController = UserController(userUsecase, tokenUsecase, jsonResponser)
        streamController = StreamController(voiceUsecase, gcs, jsonResponser, streamResponser)

        CORSMid = CORSMiddleware(App)
        JWTMid  = JWTMiddleware(App,tokenUsecase,jsonResponser)
        loggerMid = LoggerMiddleware(App, logger)
        SecureMid = SecureHeaderMiddleware(App)

        userRouter = UserRouter(userController, JWTMid).router
        streamRouter = StreamRouter(streamController).router

        self.app.add_middleware(CORSMid)
        self.app.add_middleware(loggerMid)
        self.app.add_middleware(SecureMid)

        self.app.include_router(userRouter,prefix="/api/v1/user", tags=["user"])
        self.app.include_router(streamRouter,prefix="/api/v1/stream", tags=["stream"])

    def Run(self, host, port):
        uvicorn.run(app=self.app, host=host, port=port)








