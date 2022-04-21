import time
from fastapi import FastAPI, Request
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)


@app.get("/")
async def hello():
    return {"detail": "Hello world"}


@app.get("/items/")
async def items():
    print("Processing ..........")
    time.sleep(5)
    return {"detail": "Hello items"}
