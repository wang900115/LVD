from internal.application.usecase.voice import VoiceUsecase
from internal.adapter.gcs.gcs import GCS
from internal.adapter.fastapi.validator.stream import DeleteRequest, StreamRequest

class StreamController:

    def __init__(self, voiceUsecase: VoiceUsecase, gcsUsecase: GCS):
        self.voiceUsecase = voiceUsecase
        self.gcsUsecase = gcsUsecase

    def Upload(self, request):
        pass

    def Delete(self, request: DeleteRequest):
        pass

    def Stream(self, request: StreamRequest):
        pass
