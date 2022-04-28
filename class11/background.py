import time
from fastapi import FastAPI, BackgroundTasks


app = FastAPI()


def expensive(email: str):
    # expensive...
    time.sleep(5)
    print(email)


@app.get("/")
async def home(background_task: BackgroundTasks):
    background_task.add_task(expensive, email="test@test.com")
    return {"detail": "Hello world!"}
