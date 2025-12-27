from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#database setup
engine = create_engine("sqlite:///library.db", connect_args=("check_same_thread"))

#session maker
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base class for models
Base = declarative_base()

def init_db():
    #initialize database tables
    from models.customer import User
    Base.metadata.create_all(bind=engine)