from internal.application.usecase.voice import VoiceUsecase
from internal.adapter.gcs.gcs import GCS
from internal.adapter.fastapi.validator.stream import DeleteRequest, StreamRequest
from internal.adapter.fastapi.response.json import JsonResponse
from internal.adapter.fastapi.response.message import Message


class StreamController:

    def __init__(self, voiceUsecase: VoiceUsecase, gcsUsecase: GCS, response: JsonResponse):
        self.voiceUsecase = voiceUsecase
        self.gcsUsecase = gcsUsecase
        self.response = response

    def Upload(self, request):
        try:
            voice = self.voiceUsecase.CreateVoice(request.meta)
            self.gcsUsecase.Upload(request.data, voice.filename, voice.format)
            return self.response.successWithData(Message.createSuccess, voice)
        except Exception as e:
            return self.response.failWithError(Message.createFail, e)

    def Delete(self, request: DeleteRequest):
        try:
            voice = self.voiceUsecase.DeleteVoice(request.filename)
            self.gcsUsecase.Delete(voice.filename)
            return self.response.successWithData(Message.deleteSuccess, voice)
        except Exception as e:
            return self.response.failWithError(Message.deleteFail, e)

    def Stream(self, request: StreamRequest):
        pass 
