from tortoise import fields

from models.base import BaseModel


class User(BaseModel):
    """User table"""

    username = fields.CharField(max_length=50, null=True)
    email = fields.CharField(max_length=100, null=True)
    first_name = fields.CharField(max_length=100, null=True)
    last_name = fields.CharField(max_length=100, null=True)
    last_logged = fields.DatetimeField(null=True)
    hashed_password = fields.CharField(max_length=1000, null=True)
    phone = fields.CharField(max_length=100, null=True)
    day_of_birth = fields.CharField(max_length=20, null=True)
    month_of_birth = fields.CharField(max_length=20, null=True)
    year_of_birth = fields.CharField(max_length=20, null=True)
    email_verified = fields.BooleanField(default=False, null=True)


class Picture(BaseModel):
    user = fields.ForeignKeyField(
        "models.User", related_name="picture", null=True
    )
    url = fields.CharField(max_length=500, null=True)
    filename = fields.CharField(max_length=200, null=True)
    filesize = fields.CharField(max_length=100, null=True)
