from tortoise import fields
from tortoise.models import Model


class Student(Model):
    id = fields.UUIDField(pk=True)
    first_name = fields.CharField(max_length=400)
    last_name = fields.CharField(max_length=400)
    email = fields.CharField(max_length=400)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
