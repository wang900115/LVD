from internal.application.usecase.voice import VoiceUsecase
from internal.adapter.audio.gcs import GCS


class StreamController:

    def __init__(self, voiceUsecase: VoiceUsecase, gcsUsecase: GCS):
        self.voiceUsecase = voiceUsecase
        self.gcsUsecase = gcsUsecase

    def Upload(self, request):
        pass

    def Delete(self, request):
        pass

    def Stream(self, request):
        pass
