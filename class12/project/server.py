from typing import List
from fastapi import FastAPI

from database import create_start_app_handler
from models import Student
from schemas import StudentCreate, StudentPublic

def get_application():

    # start the application.
    app = FastAPI()

    # Connect to database.
    app.add_event_handler("startup", create_start_app_handler(app))

    return app

app = get_application()


@app.post("/", response_model=StudentPublic)
async def home(data: StudentCreate):
    student = await Student.create(
        **data.dict(exclude_unset=True)
    )
    return student

@app.get("/", response_model=List[StudentPublic])
async def home(data: StudentCreate):
    return await Student.all()
