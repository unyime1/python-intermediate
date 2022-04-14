import time
from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()


class RegisterSchema(BaseModel):
    first_name: str
    surname: str
    password: str
    date_of_birth: str
    gender: Optional[str] = "female"
    phone_number: int
    email: EmailStr


@app.post("/register/")
async def create_account(register_data: RegisterSchema):
    """Create user account."""
    time.sleep(2)
    return register_data
