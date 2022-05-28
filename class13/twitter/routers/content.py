from fastapi import APIRouter, status, Security, Path, Depends, HTTPException

from library.schemas.content import (
    TweetCreate,
    TweetPublic,
    TweetUpdate,
    CommentCreate,
    CommentPublic,
)
from library.dependencies.auth import get_current_user
from models.contents import Tweet, Media, Comment
from library.dependencies.content import check_tweet_permissions


router = APIRouter(prefix="/content")


@router.post(
    "/create-tweet/",
    name="tweet:create",
    status_code=status.HTTP_201_CREATED,
    response_model=TweetPublic,
    description="Create a tweet.",
)
async def create_tweets(
    data: TweetCreate, current_user=Security(get_current_user, scopes=["base"])
):
    tweet = await Tweet.create(content=data.content, user=current_user)
    return tweet


@router.put(
    "/update-tweet/{tweet_id}/",
    name="tweet:update",
    status_code=status.HTTP_200_OK,
    response_model=TweetPublic,
    description="Update a tweet.",
    dependencies=[Depends(check_tweet_permissions)],
)
async def update_tweets(
    data: TweetUpdate,
    tweet_id: str = Path(...),
    current_user=Security(get_current_user, scopes=["base"]),
):
    await Tweet.get(id=tweet_id).update(**data.dict(exclude_unset=True))
    return await Tweet.get(id=tweet_id)


@router.delete(
    "/delete-tweet/{tweet_id}/",
    name="tweet:delete",
    status_code=status.HTTP_200_OK,
    description="Delete a tweet.",
    dependencies=[Depends(check_tweet_permissions)],
)
async def delete_tweet(
    tweet_id: str = Path(...),
    current_user=Security(get_current_user, scopes=["base"]),
):
    await Tweet.get(id=tweet_id).delete()


@router.post(
    "/comment-create/{tweet_id}/",
    name="comment:create",
    status_code=status.HTTP_201_CREATED,
    description="Create a comment",
    response_model=CommentPublic,
)
async def create_comment(
    data: CommentCreate,
    tweet_id: str = Path(...),
    current_user=Security(get_current_user, scopes=["base"]),
):
    tweet = await Tweet.get_or_none(id=tweet_id)
    if tweet is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This tweet ID is invalid."
        )
    comment = await Comment.create(
        tweet=tweet,
        user=current_user,
        content=data.content
    )
    return comment


@router.delete(
    "/delete-comment/{comment_id}/",
    name="comment:delete",
    status_code=status.HTTP_200_OK,
    description="Delete Comment."
)
async def delete_comment(
    comment_id: str = Path(...),
    current_user=Security(get_current_user, scopes=["base"]),   
):
    comment = await Comment.get_or_none(id=comment_id)
    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This comment does not exist!"
        )
    if comment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to delete this comment."
        )
    await comment.delete()
