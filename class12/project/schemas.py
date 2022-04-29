from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class StudentPublic(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    created_at: datetime
    updated_at: datetime


class StudentCreate(BaseModel):
    first_name: str = Field(..., max_length=399)
    last_name: str = Field(..., max_length=399)
    email: EmailStr