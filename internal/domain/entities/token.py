class TokenClaims:

    def __init__(self, username, expires_at,user_id=None):
        self.user_id = user_id
        self.username = username
        self.expires_at = expires_at
