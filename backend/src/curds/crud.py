from sqlalchemy.orm import Session

from ..schemas import schemas
from ..models import models


def get_todo(db: Session):
    return db.query(models.Todo).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    todo = models.Todo(title=todo.title, description=todo.description)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo