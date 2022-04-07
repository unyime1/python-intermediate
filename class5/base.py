from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello world"}


@app.post('/mike/')
async def mike():
    return {"message": "Hello Mike 4"}

@app.put('/mike-update/')
async def mike1():
    return {"message": "mike update"}

@app.delete('/mike-delete/')
async def mike2():
    return {"message": "mike delete"}
