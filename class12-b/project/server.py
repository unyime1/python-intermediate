from fastapi import FastAPI

from database import create_start_app_handler
from models import Student

def get_application():

    # start the application.
    app = FastAPI()

    # Connect to database.
    app.add_event_handler("startup", create_start_app_handler(app))

    return app

app = get_application()


@app.get("/")
async def home():
    await Student.create(
        first_name="me",
        last_name="you",
        email="test@test.com"
    )
    return {"detail": "Hello world"}
