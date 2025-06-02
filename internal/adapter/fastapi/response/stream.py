from io import BytesIO
from fastapi.responses import StreamingResponse

class StreamResponse:
    def stream(self, filename: str, file_formate: str, data: bytes) -> StreamingResponse:
        return StreamingResponse(
            content=BytesIO(data),
            media_type=self._mediaType(file_formate),
            headers={
                "Content-Disposition": f'inline; filename="{filename}"'
            }
        )
    def _mediaType(self, format: str) -> str:
        mapping = {
            "mp3": "audio/mpeg",
            "wav": "audio/wav",
            "ogg": "audio/ogg",
            "webm": "audio/webm",
            "m4a": "audio/map4"
        }
        return mapping.get(format.lower(), "application/octet-stream")
        
    