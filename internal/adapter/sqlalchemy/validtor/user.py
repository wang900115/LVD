from pydantic import BaseModel, EmailStr, Field


class UserValidator(BaseModel):
    username: str = Field(..., min_length=5, max_length=30)
    password: str = Field(..., min_length=5, max_length=30)
    email: EmailStr
