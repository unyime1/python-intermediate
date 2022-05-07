import logging
from typing import Callable

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_SERVER,
    POSTGRES_PORT,
    POSTGRES_DB,
)

logger = logging.getLogger(__name__)

MODELS = ["models", "aerich.models"]


TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": f"{POSTGRES_SERVER}",
                "port": f"{POSTGRES_PORT}",
                "user": f"{POSTGRES_USER}",
                "password": f"{POSTGRES_PASSWORD}",
                "database": f"{POSTGRES_DB}",
            },
        },
    },
    "apps": {
        "models": {
            "models": MODELS,
            "default_connection": "default",
        }
    },
}


async def init_db(app: FastAPI) -> None:
    """Initialize database."""
    try:
        register_tortoise(
            app,
            db_url=f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}",  # noqa
            modules={"models": MODELS},
            generate_schemas=False,
            add_exception_handlers=True,
        )
        logger.warning("--- DB CONNECTION WAS SUCCESSFUL ---")
    except Exception as e:
        logger.warning("--- DB CONNECTION ERROR ---")
        logger.warning(e)
        logger.warning("--- DB CONNECTION ERROR ---")


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await init_db(app)

    return start_app
