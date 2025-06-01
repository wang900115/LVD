from fastapi import APIRouter
from internal.adapter.fastapi.controller.stream import StreamController


class StreamRouter:

    def __init__(self, controller: StreamController):
        self.controller = controller

        self.router = APIRouter()
        
        self.router.add_api_route("/upload", self.upload, methods=["POST"])
        self.router.add_api_route("/delete", self.delete, methods=["DELETE"])
        self.router.add_api_route("/stream", self.stream, methods=["GET"])

    def upload(self, request):
        return self.controller.Upload(request)

    def delete(self, request):
        return self.controller.Delete(request)

    def stream(self, request):
        return self.controller.Stream(request)
