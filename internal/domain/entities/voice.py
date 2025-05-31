class Voice:
    def __init__(self, user_id, filename, format, duration, expires_at):
        self.user_id = user_id
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