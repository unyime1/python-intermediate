from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

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
