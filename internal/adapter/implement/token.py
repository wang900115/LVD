import redis.asyncio as redis
from internal.domain.interface.token import TokenInterface
from internal.adapter.redispool.model.token import TokenModel
from internal.domain.entities.token import TokenClaims
from datetime import datetime, timedelta, timezone
import jwt
import secrets
import hashlib
import uuid


class TokenImplement(TokenInterface):

    def __init__(self,
                 client: redis.Redis,
                 base_secret: str,
                 duration: float = 30):
        self.client = client
        self.base_secret = base_secret
        self.duration = duration

    def generateSalt(self) -> str:
        return secrets.token_hex(16)

    def _generateSecret(self, salt: str) -> str:
        return hashlib.sha256((self.base_secret + salt).encode()).hexdigest()

    async def CreateToken(self, tokenClaims: TokenClaims) -> str:
        tokenClaims.expires_at = datetime.now(
            timezone.utc) + timedelta(seconds=self.duration)
        salt = self.generateSalt()
        jti = str(uuid.uuid4())
        payload = {
            "user_id": tokenClaims.user_id,
            "username": tokenClaims.username,
            "salt": salt,
            "jti": jti,
            "exp": int(tokenClaims.expires_at.timestamp)
        }
        token = jwt.encode(payload,
                           self._generateSecret(salt),
                           algorithm="HS256")
        await self.client.setex(f"token:{jti}", self.duration, "active")
        return token

    async def ValidateToken(self, token: str) -> TokenClaims:
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            jti = payload.get("jti")
            salt = payload.get("salt")
            if not salt or not jti:
                raise Exception("Token miss field")
            exists = await self.client.exists(f"token:{jti}")
            if not exists:
                raise Exception("Token have been expired")
            secret = self._generateSecret(salt)
            verified_payload = jwt.decode(token, secret, algorithms=["HS256"])
            return TokenClaims(user_id=verified_payload["user_id"],
                               username=verified_payload["username"],
                               expires_at=datetime.utcfromtimestamp(
                                   verified_payload["expires_at"]))
        except jwt.ExpiredSignatureError:
            raise Exception("Token have been expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid Token")

    async def DeleteToken(self, token: str) -> None:
        payload = jwt.decode(token, options={"verify_signature": False})
        jti = payload.get("jti")
        if jti:
            await self.client.delete(f"token:{jti}")