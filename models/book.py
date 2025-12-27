import sqlalchemy
from datetime import datetime
from uuid_extension import uuid7
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

timestamp = datetime.utcnow().isoformat() +'Z'

class Book(Base):
    __tablename__ = "books"
    id = Column(String, primary_key=True)
    title = Column(String(100), nullable=False)
    issn_or_isbn = Column(Integer(50), nullable=False, unique=True)
    author = Column (String(50), nullable=False)
    publisher = Column(String(50), nullable=False)
    created_at = Column(String, timestamp, nullable=False)
    updated_at = Column(String, timestamp, nullable=False)

