from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from .....internal.domain.entities.voice import Voice

Base = declarative_base()

class VoiceTable(Base):
    __tablename__= 'voice'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)

    filename = Column(Text, nullable=False)
    format = Column(String(10), nullable=False)
    duration = Column(Float, nullable=False)
    filesize = Column(Float, nullable=False)

    uploaded_at = Column(DateTime, nullable=False)
    expires_at = Column(DateTime, nullable=False)

    def Domain(self):
        return Voice(
            filename=self.filename,
            format=self.format,
            duration=self.duration,
            expires_at=self.expires_at
        )


