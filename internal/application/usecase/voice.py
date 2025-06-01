from internal.domain.interface.voice import VoiceInterface
from internal.domain.entities.voice import Voice
from typing import List
from internal.adapter.sqlalchemy.model.voice import VoiceTable

class VoiceUsecase:

    def __init__(self, usecase: VoiceInterface):
        self.usecase = usecase
    
    def CreateVoice(self, voice: Voice)-> str:
        return self.usecase.CreateVoice(voice)

    def QueryVoices(self, user_id: int) -> List[Voice]:
        return self.usecase.QueryVoices(user_id)
    
    def QueryVoice(self,filename: str)-> VoiceTable:
        return self.usecase.QueryVoice(filename)
    
    def DeleteVoice(self, filename: str) -> str:
        return self.usecase.DeleteVoice(filename)