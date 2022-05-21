from datetime import datetime, timezone

from jose import jwt, JWTError
from pydantic import ValidationError
from fastapi import Depends, HTTPException, status
from fastapi.security import (
    OAuth2PasswordBearer,
    SecurityScopes,
)
from library.schemas.auth import JWTSchema
from config import SECRET_KEY, ALGORITHM
from models.users import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login/",
    scopes={"base": "For ordinary users", "root": "For super users"},
)


async def get_current_user(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
):
    auth_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Your auth token is invalid.",
    )
    try:
        payload = jwt.decode(token, str(SECRET_KEY), algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        expire = payload.get("expire")

        token_data = JWTSchema(user_id=user_id, expire=expire)

        if user_id is None or expire is None:
            raise auth_exception
    except (JWTError, ValidationError):
        raise auth_exception

    # Check expiration.
    if datetime.now(timezone.utc) > token_data.expire:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Your token has expired. Please login.",
        )

    user = await User.get_or_none(id=token_data.user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="This user does not exist.",
        )

    return user
