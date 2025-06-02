from pydantic import BaseModel, EmailStr


class RegistRequest(BaseModel):
    username: str
    password: str
    email: EmailStr


class LoginRequest(BaseModel):
    username: str
    password: str


