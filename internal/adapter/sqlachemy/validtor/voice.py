from pydantic import BaseModel
from datetime import datetime

class VoiceValidator(BaseModel):
    user_id: int
    filename: str
    format: str
    duration: float
    filesize: float

    upload_at: datetime
    expires_at: datetime