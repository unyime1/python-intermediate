from fastapi import APIRouter, Security, status, Path, HTTPException

from library.schemas.register import UserPublic
from library.schemas.users import UserUpdate, FollowStatsPublic
from library.dependencies.auth import get_current_user
from models.users import User, Follows

router = APIRouter(prefix="/user")


@router.put("/update/", response_model=UserPublic)
async def update(
    data: UserUpdate,
    current_user=Security(get_current_user, scopes=["base", "roots"]),
):
    await User.get(id=current_user.id).update(**data.dict(exclude_unset=True))
    return await User.get(id=current_user.id)


@router.delete("/delete/")
async def delete(
    current_user=Security(get_current_user, scopes=["base", "roots"]),
):
    await User.get(id=current_user.id).delete()


@router.get(
    "/follow/{user_id}/",
    name="follow",
    status_code=status.HTTP_201_CREATED
)
async def follow(
    user_id: str = Path(...),
    current_user=Security(get_current_user, scopes=["base", "roots"]),
):
    followee = await User.get_or_none(id=user_id)
    if followee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This user does not exist."
        )
    if followee.id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You can't follow yourself."
        )

    already_followed = await Follows.filter(
        follower_id=current_user.id,
        followee_id=followee.id
    ).exists()

    if already_followed:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You can't follow same person twice."
        )

    await Follows.create(
        follower_id=current_user.id,
        followee_id=followee.id
    )


@router.delete(
    "/unfollow/{user_id}/",
    name="unfollow",
    status_code=status.HTTP_200_OK
)
async def unfollow(
    user_id: str = Path(...),
    current_user=Security(get_current_user, scopes=["base", "roots"]),
):
    followee = await User.get(id=user_id)
    follow = await Follows.get_or_none(follower=current_user, followee=followee)
    if follow is None:
        raise HTTPException(
            status_code=404,
            detail="This follow does not exist."
        )
    await follow.delete()


@router.get(
    "/follow-stats/{user_id}/",
    name="follow:stats",
    status_code=status.HTTP_200_OK,
    response_model=FollowStatsPublic
)
async def stats(
    user_id: str = Path(...),
    current_user=Security(get_current_user, scopes=["base", "roots"]),
):
    user = await User.get(id=user_id)

    followers = await Follows.filter(followee=user)
    followees = await Follows.filter(follower=user)

    response = FollowStatsPublic(
        followers=followers,
        followees=followees
    )
    return response
