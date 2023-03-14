from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas import schemas
from ..curds import todo_crud as crud
from ..databases.databases import engine, get_db
from ..databases.databases import get_db

router = APIRouter()

@router.get("/api/todo", response_model=list[schemas.Todo])
def get_todo(db: Session = Depends(get_db)):
    return crud.get_todo(db=db)

@router.get("/api/todo/{id}", response_model=schemas.Todo)
def find_by_id(id: int, db: Session = Depends(get_db)):
    return crud.find_by_id(id=id, db=db)

@router.post("/api/todo", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@router.delete("/api/todo/{id}")
def todo_delete(id: int, data: schemas.TodoUpdate, db: Session = Depends(get_db)):
    return crud.todo_delete(db=db, id=id)