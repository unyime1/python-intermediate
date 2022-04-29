import logging
from typing import Callable
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

logger = logging.getLogger(__name__)

MODELS = ["models", "aerich.models"]


async def init_db(app: FastAPI) -> None:
    try:
        register_tortoise(
            app,
            db_url="postgres://postgres:postgres@db:5432/postgres",
            modules={"models": MODELS},
            generate_schemas=True,
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