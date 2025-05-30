from abc import ABC, abstractmethod
from typing import List
from internal.adapter.sqlachemy.validtor.voice import VoiceValidator
from internal.domain.entities.voice import Voice

class VoiceInterface(ABC):

    @abstractmethod
    def CreateVoice(self, voice: VoiceValidator)-> str:
        pass

    @abstractmethod
    def QueryVoices(self)-> List[Voice]:
        pass

    @abstractmethod
    def QueryVoice(self, filename: str)->Voice:
        pass

    @abstractmethod
    def DeleteVoice(self, filename: str)-> str:
        pass