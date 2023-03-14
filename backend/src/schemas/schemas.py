from pydantic import BaseModel

class SuccessMsg(BaseModel):
  message: str

class TodoCreate(BaseModel):
  title: str
  description: str

class Todo(BaseModel):
  id: str
  title: str
  description: str

  class Config:
    orm_mode = True

class TodoUpdate(BaseModel):
  title: str | None = None
  description: str | None = None
