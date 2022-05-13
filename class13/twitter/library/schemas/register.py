from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(..., max_length=40)
    email: EmailStr
    first_name: str = Field(..., max_length=60)
    last_name: Optional[str] = Field(None, max_length=60)
    phone: Optional[str] = Field(None, max_length=15)
    day_of_birth: Optional[str] = Field(None, max_length=15)
    month_of_birth: Optional[str] = Field(None, max_length=15)
    year_of_birth: Optional[str] = Field(None, max_length=15)
    password: str = Field(..., min_length=8, max_length=1500)


class UserPublic(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    first_name: str
    last_name: Optional[str]
    phone: Optional[str]
    day_of_birth: Optional[str]
    month_of_birth: Optional[str]
    year_of_birth: Optional[str]
    created_at: datetime
    created_at: datetime
    email_verified: bool
