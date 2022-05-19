import pytest
from fastapi import FastAPI
from httpx import AsyncClient


pytestmark = pytest.mark.asyncio


class TestFake:
    async def test_fake(
        self,
        app: FastAPI,
    ) -> None:
        assert 1 == 1
    
    async def test_fake2(
        self,
        app: FastAPI,
    ) -> None:
        assert 1 != 2
