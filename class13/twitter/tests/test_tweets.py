import pytest
from fastapi import FastAPI, status
from httpx import AsyncClient

from models.contents import Tweet

pytestmark = pytest.mark.asyncio


class TestFake:
    async def test_fake(self, app: FastAPI, client: AsyncClient) -> None:
        assert 1 == 1

    async def test_fake2(
        self,
        app: FastAPI,
        client: AsyncClient,
    ) -> None:
        assert 1 != 2


class TestTweetCreate:
    async def test_create(
        self,
        app: FastAPI, 
        authorized_client: AsyncClient
    ) -> None:
        data = {
            "content": "My very first tweet!"
        }
        res = await authorized_client.post(
            app.url_path_for("tweet:create"), json=data
        )
        assert res.status_code == status.HTTP_201_CREATED

        res_data = res.json()

        assert res_data is not None
        assert "id" in res_data
        assert "content" in res_data
        assert "created_at" in res_data
        assert "updated_at" in res_data

        assert res_data["content"] == data["content"]

        tweet = await Tweet.get_or_none(id=res_data["id"])
        assert tweet is not None
        assert tweet.content == data["content"]
