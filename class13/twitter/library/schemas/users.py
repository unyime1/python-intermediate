from typing import Optional, List
from pydantic import BaseModel, Field

from library.schemas.register import UserPublic


class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=60)
    last_name: Optional[str] = Field(None, max_length=60)
    phone: Optional[str] = Field(None, max_length=15)
    day_of_birth: Optional[str] = Field(None, max_length=15)
    month_of_birth: Optional[str] = Field(None, max_length=15)
    year_of_birth: Optional[str] = Field(None, max_length=15)


class FollowStatsPublic(BaseModel):
    followers: Optional[List[UserPublic]] = []
    followees: Optional[List[UserPublic]] = []

    class Config:
        orm_mode=True
