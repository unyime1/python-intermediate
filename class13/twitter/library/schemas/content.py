from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field, validator

from library.schemas.shared import SharedModel


class TweetCreate(BaseModel):
    """Create tweets"""

    content: str = Field(..., max_length=550)


class TweetUpdate(TweetCreate):
    """Update tweets"""


class TweetPublic(SharedModel):
    """Tweet public"""

    content: str


class CommentCreate(BaseModel):
    content: str = Field(..., max_length=550)


class CommentPublic(SharedModel):
    content: str
    user_id: Optional[UUID]


class LikePublic(SharedModel):
    user_id: Optional[UUID]


class TweetGetPublic(TweetPublic):
    comments: Optional[List[CommentPublic]] = []
    likes: Optional[List[LikePublic]] = []

    @validator("comments", pre=True)
    def _iter_comment_list(cls, v):
        return list(v)

    @validator("likes", pre=True)
    def _iter_likes_list(cls, v):
        return list(v)

    class Config:
        orm_mode=True
    