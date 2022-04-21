from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from pydantic import BaseModel


app = FastAPI()


class RegisterSchema(BaseModel):
    username: str
    password: str


@app.post("/register/")
async def create_account(register_data: RegisterSchema):
    """Create user account."""
    return register_data


@app.post("/register2/")
async def create_account(username: str = Form(...), password: str = Form(...)):
    """Create user account."""
    return {"username": username, "password": password}


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile, username: str = Form(...)):
    if len(username) < 5:
        raise HTTPException(
            status_code=422,
            detail="error"
        )
    return {"filename": file.filename, "username": username}
