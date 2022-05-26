from dbm.ndbm import library
from fastapi import Path, Depends, Security, HTTPException, status

from library.dependencies.auth import get_current_user
from models.contents import Tweet


async def get_tweet_by_id_from_path(tweet_id: str = Path(...)):
    return await Tweet.get(id=tweet_id)


async def check_tweet_permissions(
    tweet = Depends(get_tweet_by_id_from_path),
    current_user = Security(get_current_user, scopes=["base"])
):
    if tweet.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to perform this action."
        )
