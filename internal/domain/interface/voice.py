from abc import ABC, abstractmethod
from typing import List
from internal.domain.entities.voice import Voice
from internal.adapter.sqlachemy.model.voice import VoiceTable
class VoiceInterface(ABC):

    @abstractmethod
    def CreateVoice(self, voice: Voice)-> Voice:
        pass

    @abstractmethod
    def QueryVoices(self, user_id: int)-> List[Voice]:
        pass

    @abstractmethod
    def QueryVoice(self, filename: str)->VoiceTable:
        pass

    @abstractmethod
    def DeleteVoice(self, filename: str)-> str:
        pass