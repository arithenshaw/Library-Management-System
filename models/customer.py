import sqlalchemy
from datetime import datetime
from uuid_extension import uuid7
from sqlalchemy import Column, String, Integer
from database import Base

timestamp = datetime.utcnow().isoformat() +'Z'

class User(Base):
    __tablename__ = "Customer"
    id = Column(String(255), primary_key=True)
    # username = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone_no = Column(Integer(50), nullable=False)
    address = Column (String(255), nullable=False)
    # created_at = Column(String, timestamp, nullable=False)
    # updated_at = Column(String, timestamp, nullable=False)
    # password_hash = Column(String(255), nullable=False, unique=True)