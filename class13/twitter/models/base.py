from tortoise import fields
from tortoise.models import Model


class BaseModel(Model):
    """Define datetime model mixin."""

    id = fields.UUIDField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True
