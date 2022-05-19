from typing import Optional
from pydantic import BaseModel, Field


class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=60)
    last_name: Optional[str] = Field(None, max_length=60)
    phone: Optional[str] = Field(None, max_length=15)
    day_of_birth: Optional[str] = Field(None, max_length=15)
    month_of_birth: Optional[str] = Field(None, max_length=15)
    year_of_birth: Optional[str] = Field(None, max_length=15)
