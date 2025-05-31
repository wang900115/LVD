from internal.domain.entities.token import TokenClaims
from datetime import datetime
import jwt


class TokenModel():
    user_id: int
    username: str
    expires_at: datetime

    def Domain(self):
        return TokenClaims(user_id=self.user_id,
                           username=self.username,
                           expires_at=self.expires_at)
