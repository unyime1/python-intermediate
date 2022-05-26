from fastapi import APIRouter, status, Security, Path, Depends

from library.schemas.content import TweetCreate, TweetPublic, TweetUpdate
from library.dependencies.auth import get_current_user
from models.contents import Tweet, Media
from library.dependencies.content import check_tweet_permissions


router = APIRouter(prefix="/content")


@router.post(
    "/create-tweet/",
    name="tweet:create",
    status_code=status.HTTP_201_CREATED,
    response_model=TweetPublic,
    description="Create a tweet."
)
async def create_tweets(
    data: TweetCreate,
    current_user = Security(get_current_user, scopes=["base"])
):
    tweet = await Tweet.create(
        content=data.content,
        user=current_user
    )
    return tweet


@router.put(
    "/update-tweet/{tweet_id}/",
    name="tweet:update",
    status_code=status.HTTP_200_OK,
    response_model=TweetPublic,
    description="Update a tweet.",
    dependencies = [Depends(check_tweet_permissions)]
)
async def update_tweets(
    data: TweetUpdate,
    tweet_id: str = Path(...),
    current_user = Security(get_current_user, scopes=["base"])
):
    await Tweet.get(id=tweet_id).update(
        **data.dict(exclude_unset=True)
    )
    return await Tweet.get(id=tweet_id)


@router.delete(
    "/delete-tweet/{tweet_id}/",
    name="tweet:delete",
    status_code=status.HTTP_200_OK,
    description="Delete a tweet.",
    dependencies = [Depends(check_tweet_permissions)]
)
async def delete_tweet(
    tweet_id: str = Path(...),
    current_user = Security(get_current_user, scopes=["base"])
):
    await Tweet.get(id=tweet_id).delete()
