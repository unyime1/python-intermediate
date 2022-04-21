from typing import Optional
from fastapi import FastAPI


app = FastAPI()


db = [
    {
        "name": "uche",
        "address": "lagos"
    },
    {
        "name": "mathew",
        "address": "lagos"
    },
    {
        "name": "idd",
        "address": "Abuja"
    },
]


@app.get('/items/{index}')
async def read_item(index: int):
    return {"Hello": index}


@app.get('/items/')
async def me(name: Optional[str] = None):
    print(name)
    return {"hello": "nothing"}
