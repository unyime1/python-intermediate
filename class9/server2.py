from typing import Optional

from fastapi import FastAPI, Depends

app = FastAPI()


def q_depends(q: Optional[str] = None):
    return q

def query_depends(q: str = Depends(q_depends), r: Optional[str] = None):
    return {"q": q, "r": r}

@app.get("/")
async def home(query = Depends(query_depends)):
    return query


@app.get("/items/")
async def items(query = Depends(query_depends)):
    return query

