from internal.domain.interface.voice import VoiceInterface
from internal.adapter.sqlachemy.validtor.voice import VoiceValidator
from internal.domain.entities.voice import Voice
from typing import List

class VoiceUsecase:

    def __init__(self, usecase: VoiceInterface):
        self.usecase = usecase
    
    def CreateVoice(self, voice: VoiceValidator)-> str:
        return self.usecase.CreateVoice(voice)

    def QueryVoices(self) -> List[Voice]:
        return self.usecase.QueryVoices()
    
    def QueryVoice(self,filename: str)-> Voice:
        return self.usecase.QueryVoice(filename)
    
    def DeleteVoice(self, filename: str) -> str:
        return self.usecase.DeleteVoice(filename)