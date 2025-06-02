import redis.asyncio as redis
from ....internal.domain.interface.token import TokenInterface
from ....internal.adapter.redispool.model.token import TokenModel
from ....internal.domain.entities.token import TokenClaims
from datetime import datetime, timedelta, timezone
import jwt
import secrets
import hashlib
import uuid


class TokenImplement(TokenInterface):

    def __init__(self,
                 client: redis.Redis,
                 base_secret: str,
                 config: dict):
        self.client = client
        self.base_secret = base_secret
        self.duration = self._parseTimeout(config.get("expiration","24h"))

    def _parseTimeout(self, time: str) -> float:
        if time.endswith("s"):
            return float(time[:-1])
        elif time.endswith("m"):
            return float(time[:-1])*60
        elif time.endswith("h"):
            return float(time[:-1])*3600
        
    def generateSalt(self) -> str:
        return secrets.token_hex(16)

    def _generateSecret(self, salt: str) -> str:
        return hashlib.sha256((self.base_secret + salt).encode()).hexdigest()

    def CreateToken(self, tokenClaims: TokenClaims) -> str:
        tokenClaims.expires_at = datetime.now(
            timezone.utc) + timedelta(seconds=self.duration)
        salt = self.generateSalt()
        jti = str(uuid.uuid4())

        payload = {
            "user_id": tokenClaims.user_id,
            "username": tokenClaims.username,
            "salt": salt,
            "jti": jti,
            "exp": tokenClaims.expires_at
        }

        token = jwt.encode(payload,
                           self._generateSecret(salt),
                           algorithm="HS256")
        self.client.setex(f"token:{jti}", int(self.duration), "active")
        return token

    def ValidateToken(self, token: str) -> TokenClaims:
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            jti = payload.get("jti")
            salt = payload.get("salt")
            if not salt or not jti:
                raise Exception("Token miss field")
            exists = self.client.exists(f"token:{jti}")
            if not exists:
                raise Exception("Token have been expired")
            secret = self._generateSecret(salt)
            verified_payload = jwt.decode(token, secret, algorithms=["HS256"])
            
            return TokenClaims(user_id=verified_payload["user_id"],
                               username=verified_payload["username"],
                               expires_at=verified_payload["exp"])
        
        except jwt.ExpiredSignatureError:
            raise Exception("Token have been expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid Token")

    def DeleteToken(self, token: str) -> None:
        payload = jwt.decode(token, options={"verify_signature": False})
        jti = payload.get("jti")
        if jti:
            self.client.delete(f"token:{jti}")