from pydantic import BaseModel

class TodoCreate(BaseModel):
  title: str
  description: str

class Todo(BaseModel):
  id: str
  title: str
  description: str

  class Config:
    orm_mode = True

class SuccessMsg(BaseModel):
  message: str
