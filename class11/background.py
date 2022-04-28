import time
from unittest.mock import Mock
import requests
from fastapi import FastAPI, BackgroundTasks


app = FastAPI()


def expensive(email: str):
    # expensive...
    time.sleep(5)
    print(email)


@app.get("/")
async def home(background_task: BackgroundTasks):
    response = requests.get("bbc.com")
    background_task.add_task(expensive, email="test@test.com")
    return {"detail": "Hello world!"}


"""
https://fastapi.tiangolo.com/tutorial/background-tasks/
"""
