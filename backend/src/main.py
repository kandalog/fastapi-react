from fastapi import Depends, FastAPI, HTTPException

from .models import models
from .schemas import schemas
from .curds import crud
from .databases.databases import engine, get_db
from .routes import todo_router

# テーブル定義をDBに反映
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo_router.router)

@app.get("/", response_model=schemas.SuccessMsg)
def root():
  return{"message": "root"}