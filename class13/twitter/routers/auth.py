from uuid import UUID
from fastapi import APIRouter, Path, HTTPException, status
from passlib.context import CryptContext

from library.schemas.register import UserCreate, UserPublic
from models.users import User
from library.security.otp import otp_manager


router = APIRouter(prefix="/auth")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register/", response_model=UserPublic)
async def register(data: UserCreate):
    """Create account."""
    email_exists = await User.filter(email=data.email).exists()
    username_exists = await User.filter(username=data.username).exists()
    if email_exists or username_exists:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="this user already exists!"
        )
    hashed_password = pwd_context.hash(data.password)
    created_user = await User.create(
        **data.dict(exclude_unset=True, exclude={"password"}),
        hashed_password=hashed_password
    )
    # construct email that sends verification token
    token = otp_manager.create_otp(str(created_user.id))
    print(f"sending... verification token: {token}")
    return created_user


@router.get("/verify-account/{otp}/", response_model=UserPublic)
async def verify(otp: str = Path(...)):
    user_id = otp_manager.get_otp_user(otp)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Your OTP is invalid or expired."
        )
    await User.get(id=UUID(user_id)).update(
        email_verified=True
    )
    return await User.get(id=UUID(user_id))
