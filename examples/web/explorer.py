from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service


router = APIRouter(prefix="/explorer")

@router.get("/")
def get_all():
    return service.get_all()

@router.get("/{name}")
def get_one(name: str)-> Explorer | None:
    return service.get_one(name)

# all the remaining endpoints do nothing yet:
@router.post("/")
def create(explorer: Explorer)-> Explorer:
    return service.create(explorer)

@router.patch("/")
def modify(explorer: Explorer)-> Explorer:
    return service.modify(explorer)

@ router.put("/a ")
def replace(explorer: Explorer)-> Explorer:
    return service.replace(explorer)

@router.delete("/{name}")
def delete(name: str)-> None:
    return None

