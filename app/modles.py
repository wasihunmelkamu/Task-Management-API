from sqlalchemy import Column,Integer,String,Boolean,DateTime
from sqlalchemy.sql import func
from .databse import Base


class Task(Base):
    _tablename_='tasks'
    id=Column(Integer,primary_key=True,index=True) 
    title=Column(String,index=True)
    description=Column(String)
    completed=Column(Boolean,defualt=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    