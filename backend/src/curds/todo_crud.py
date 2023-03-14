from sqlalchemy.orm import Session

from ..schemas import schemas
from ..models import models


def get_todo(db: Session) -> list[schemas.Todo]:
    all_todo = db.query(models.Todo).all()
    return all_todo

def find_by_id(db: Session, id: int) -> schemas.Todo:
    todo = db.query(models.Todo).get(id)
    return todo

def create_todo(db: Session, todo: schemas.TodoCreate) -> schemas.Todo:
    todo = models.Todo(**dict(todo))
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_todo(db: Session, id: int, data: schemas.TodoUpdate) -> schemas.Todo | None:
    todo = db.query(models.Todo).get(id)
    todo.title = data.title or data.title
    todo.description = data.description or todo.description
    db.commit()
    db.refresh(todo)
    return todo

def todo_delete(db: Session, id: int) -> bool:
    todo = db.query(models.Todo).get(id)
    if todo:
        db.delete(todo)
        return True
    return False