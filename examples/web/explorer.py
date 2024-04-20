from fastapi import APIRouter


router = APIRouter(prefix="/explorer")

@router.get("/")
async def top():
    return "top explorer endpoint"
