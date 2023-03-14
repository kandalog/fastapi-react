from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..databases.databases import Base

class Todo(Base):
  __tablename__ = "todos"
  id = Column(Integer, autoincrement=True, primary_key=True, index=True)
  title = Column(String(100))
  description = Column(String(259))