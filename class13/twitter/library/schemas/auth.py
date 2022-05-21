from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from library.schemas.register import UserPublic


class LoginSchema(BaseModel):
    username_or_email: str
    password: str


class JWTSchema(BaseModel):
    user_id: str
    expire: Optional[datetime]


class AuthResponse(BaseModel):
    user: UserPublic
    token: str
