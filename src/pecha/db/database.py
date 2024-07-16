import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = os.environ["PG_USER"]
password = os.environ['PG_PASSWORD']
SQLALCHEMY_DATABASE_URL = 'postgresql://{user}:{password}@localhost/pecha'

# remove connect_args={'check_same_thread': False} for postgres
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)

Base = declarative_base()
