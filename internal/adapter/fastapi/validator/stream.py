from pydantic import BaseModel
from datetime import datetime

class DeleteRequest(BaseModel):
    filename: str
    format: str

class StreamRequest(BaseModel):
    filename: str
    format: str