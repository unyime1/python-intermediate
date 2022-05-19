from fastapi import APIRouter, Security

from library.schemas.register import UserPublic
from library.schemas.users import UserUpdate
from library.dependencies.auth import get_current_user
from models.users import User

router = APIRouter(prefix="/user")


@router.put("/update/", response_model=UserPublic)
async def update(
    data: UserUpdate,
    current_user = Security(get_current_user, scopes=["base", "roots"]),
):
    await User.get(id=current_user.id).update(
        **data.dict(exclude_unset=True)
    )
    return await User.get(id=current_user.id)


@router.delete("/delete/")
async def delete(
    current_user = Security(get_current_user, scopes=["base", "roots"]),
):
    await User.get(id=current_user.id).delete()
