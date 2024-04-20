from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service


router = APIRouter(prefix="/explorer")

@router.get("/")
async def get_all():
    return service.get_all()

@router.get("/{name}")
async def get_one(name: str)-> Explorer | None:
    return service.get_one(name)

# all the remaining endpoints do nothing yet:
@router.post("/")
async def create(explorer: Explorer)-> Explorer:
    return service.create(explorer)

@router.patch("/")
async def modify(explorer: Explorer)-> Explorer:
    return service.modify(explorer)

@ router.put("/")
async def replace(explorer: Explorer)-> Explorer:
    return service.replace(explorer)

@router.delete("/{name}")
async def delete(name: str)-> None:
    return None

