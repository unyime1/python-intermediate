from fastapi import APIRouter


router = APIRouter(prefix="/auth")


@router.post("/register/")
async def register():
    pass
