from sqlalchemy.orm import Session 
from internal.adapter.sqlalchemy.model.voice import VoiceTable
from internal.domain.entities.voice import Voice
from internal.domain.interface.voice import VoiceInterface
from internal.adapter.sqlalchemy.validtor.voice import VoiceValidator
from typing import List
class VoiceImplement(VoiceInterface):

    def __init__(self,db: Session):
        self.db = db

    def CreateVoice(self, voice: Voice) -> Voice:
        existingVoice = self.db.query(VoiceTable).filter_by(filename=voice.filename).first()
        if existingVoice:
            raise ValueError("this voice has been created")
        validatedVoice = VoiceValidator(**voice.__dict__)
        newVoice = VoiceTable(
            user_id=validatedVoice.user_id,
            filename = validatedVoice.filename,
            format = validatedVoice.format,
            duration = validatedVoice.duration,
            filesize = validatedVoice.filesize,
            uploaded_at = validatedVoice.uploaded_at,
            expires_at=validatedVoice.expires_at
        )
        self.db.add(newVoice)
        self.db.commit()
        self.db.refresh(newVoice)
        return newVoice.Domain()

    def QueryVoice(self, filename: str) -> VoiceTable:
        resultVoice = self.db.query(VoiceTable).filter_by(filename=filename).first()
        if resultVoice is None:
            raise ValueError("filename wrong")
        return resultVoice
    
    def QueryVoices(self,user_id: int)-> List[Voice]:
        resultVoices = self.db.query(VoiceTable).filter_by(user_id=user_id).all()
        return [resultVoice.Domain() for resultVoice in resultVoices]
    
    def DeleteVoice(self, filename: str) -> Voice:
        resultVoice = self.QueryVoice(filename)
        self.db.delete(resultVoice)
        self.db.commit()
        return resultVoice.Domain()