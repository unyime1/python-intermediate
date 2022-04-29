import asyncio
import time
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


async def write_notification(email: str, message=""):
    # time.sleep(5)
    await asyncio.sleep(5)
    print("me")


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    # write_notification(email=email)
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
