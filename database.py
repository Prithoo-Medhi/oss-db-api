'''
Declares and define the database settings.
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import sessionmaker

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_TYPE = os.environ['DB_TYPE']
PGHOST = os.environ['PGHOST']
PGPORT = os.environ['PGPORT']
PGDATABASE = os.environ['PGDATABASE']
PGUSER = os.environ['PGUSER']
PGPASSWORD = os.environ['PGPASSWORD']

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=64)


SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
