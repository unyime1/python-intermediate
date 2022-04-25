from fastapi import FastAPI
from passlib.context import CryptContext
from pydantic import BaseModel
from jose import jwt


app = FastAPI()

"""Hashing"""
pw_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def hash_password(plaintext_pw: str) -> str:
    return pw_context.hash(plaintext_pw)

def verify_hash(plaintext_pw, hashed_pw) -> bool:
    return pw_context.verify(plaintext_pw, hashed_pw)


class PasswordSchema(BaseModel):
    password: str

@app.post("/hash/")
async def hash(data: PasswordSchema):
    pw_hash = hash_password(data.password)
    return {"plaintext": data.password, "hash": pw_hash}



@app.post("/verify-hash/")
async def verify_hash(data: PasswordSchema):
    pw_hash = "$2b$12$q9GRUrvWFzFH60oSssQjPOxcaxCk9RaQ6hgZfG.i/TKdmwg8mCEWe"
    is_valid = verify_hash(data.password, pw_hash)
    if is_valid:
        # validate login
        pass
    else:
        # raise exception
        pass
    return {"is_valid": is_valid}




"""JWT"""
SECRET_KEY="6e9b583150caad16b6aa99063e148daf4fd6cd8a2683fba7ba8b3d050df4b2bb"
ALGORITHM = "HS256"
EXPIRES_MINUTES = 90

class JWTSchema(BaseModel):
    email: str

def create_jwt(data: JWTSchema):
    data_dict = data.dict()
    encoded_jwt = jwt.encode(data_dict, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_jwt(token):
    payload = jwt.decode(
        token, str(SECRET_KEY), algorithms=[ALGORITHM]
    )
    return payload


@app.post("/jwt/")
async def verify(data: JWTSchema):
    jwtdata = JWTSchema(
        email=data.email
    )
    jwt = create_jwt(data=jwtdata)
    payload = decode_jwt(jwt)

    return {"jwt": jwt, "payload": payload}
