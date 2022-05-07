from tortoise import fields

from models.base import BaseModel


class Tweet(BaseModel):
    """User tweet"""

    user = fields.ForeignKeyField(
        "models.User", related_name="tweets", null=True
    )
    content = fields.CharField(max_length=600, null=True)


class Like(BaseModel):
    """Tweet likes"""

    tweet = fields.ForeignKeyField(
        "models.Tweet", related_name="likes", null=True
    )
    user = fields.ForeignKeyField(
        "models.User", related_name="likes", null=True
    )


class Comment(BaseModel):
    """Tweet comment"""

    tweet = fields.ForeignKeyField(
        "models.Tweet", related_name="comments", null=True
    )
    user = fields.ForeignKeyField(
        "models.User", related_name="comments", null=True
    )
    content = fields.CharField(max_length=600, null=True)


class Media(BaseModel):
    """Tweet media"""

    tweet = fields.ForeignKeyField(
        "models.Tweet", related_name="medias", null=True
    )
    url = fields.CharField(max_length=500, null=True)
    filename = fields.CharField(max_length=200, null=True)
    filesize = fields.CharField(max_length=100, null=True)
