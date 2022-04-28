from typing import Optional, Dict
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel



app = FastAPI()


fake_secret_token = "coneofsilence"

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}


class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None


@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: str = Header(...)):
    """Insert item into db."""
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = item
    return item


@app.get("/items/", response_model=Dict)
async def get_item(x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    return fake_db


@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]



"""
https://fastapi.tiangolo.com/tutorial/testing/
"""
