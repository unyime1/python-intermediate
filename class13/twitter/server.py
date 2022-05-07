from fastapi import FastAPI

from library.database.database import create_start_app_handler
from routers.auth import router as AuthRouter
from routers.content import router as ContentRouter


def get_application():

    # start the application.
    app = FastAPI()

    # Connect to database.
    app.add_event_handler("startup", create_start_app_handler(app))
    app.include_router(AuthRouter)
    app.include_router(ContentRouter)

    return app


app = get_application()


@app.get("/")
async def home():
    return {"detail": "hello world!"}
