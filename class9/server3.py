from typing import Optional

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: str = Header(...)):
    if x_token != "test-token":
        raise HTTPException(status_code=401, detail="Wrong token")


async def secret_key(x_key: str = Header(...)):
    if x_key != "test-key":
        raise HTTPException(status_code=401, detail="Wrong key")


@app.get("/items/", dependencies=[Depends(verify_token), Depends(secret_key)])
async def items():    
    return {"is_valid": True}
