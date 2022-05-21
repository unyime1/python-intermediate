import asyncio

import pytest
import redis
from fastapi import FastAPI
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from tortoise.contrib.fastapi import register_tortoise
from passlib.context import CryptContext

from server import get_application

from config import DATABASE_URL
from models.contents import Tweet, Like, Media, Comment
from models.users import User, Picture


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@pytest.fixture(scope="module")
def app() -> FastAPI:
    """Get a reference to the application."""
    app = get_application()
    return app


@pytest.fixture(scope="module")
async def client(app: FastAPI) -> AsyncClient:
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="http://testserver",
            headers={"Content-Type": "application/json"},
        ) as client:
            yield client


@pytest.fixture(scope="module", autouse=True)
async def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={
            "models": [
                "models",
                "aerich.models",
            ]
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="class", autouse=True)
async def clean_database():
    yield
    await User.all().delete()
    await Picture.all().delete()
    await Tweet.all().delete()
    await Like.all().delete()
    await Media.all().delete()
    await Comment.all().delete()


@pytest.fixture(autouse=True)
def clean_redis():
    r = redis.Redis(host="redis", port=6379)
    r.flushall()


@pytest.fixture()
async def test_user():
    user_password = "testing456"
    hashed_password = pwd_context.hash(user_password)

    username = ("username",)
    email = "email@email.com"

    email_exists = await User.filter(email=email).exists()
    username_exists = await User.filter(username=username).exists()

    if email_exists or username_exists:
        return await User.get(email=email)
    else:
        return await User.create(
            username="username",
            email="email@email.com",
            first_name="Test",
            email_verified=True,
            hashed_password=hashed_password,
        )
