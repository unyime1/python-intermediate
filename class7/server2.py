from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(..., max_length=300, min_length=3)
    description: Optional[str] = Field(None, max_length=300, min_length=3)
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.put("/items/{item_id}/")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


"https://fastapi.tiangolo.com/tutorial/body-fields/"