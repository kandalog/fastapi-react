from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models import models
from ..schemas import schemas
from ..curds import crud
from ..databases.databases import engine, get_db
from ..databases.databases import get_db

router = APIRouter()

@router.post("/todo", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)
