class Voice:
    def __init__(self, filename, format, duration, expires_at):
        self.filename = filename
        self.format= format
        self.duration = duration
        self.expires_at = expires_at
    
    def Dict(self):
        return {
            "filename": self.filename,
            "format": self.format,
            "duration": self.duration,
            "expires_at": self.expires_at
        }