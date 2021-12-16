'''
Contains the models for the database.
'''
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, JSON
from sqlalchemy.sql.sqltypes import DateTime
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql.schema import ForeignKey
from database import Base


class Results(Base):
    '''
    Model/Table to contain capabilities for each test-case:
    '''
    __tablename__ = 'results'

    uuid = Column(Integer, primary_key=True, index=True)
    start = Column(DateTime)
    stop = Column(DateTime)  
    description = Column(String)
    name = Column(String)
    fullName = Column(String)
    status = Column(String) 
    testCaseId = Column(String)
    historyId  = Column(String) 
    befores = Column(Boolean)
    afters = Column(Boolean)
    children = Column(Boolean)
    attachments = Column(Boolean)
    labels = Column(Boolean)

class Befores(Base):
    __tablename__ = 'befores'

    before_id = Column(Integer, primary_key=True, index=True)
    uuid = Column(Integer)
    data = Column(String)

class Afters(Base):
    __tablename__ = 'afters'

    after_id = Column(Integer, primary_key=True, index=True)
    uuid = Column(Integer)
    data = Column(String)

class Children(Base):
    __tablename__ = 'children'

    children_id = Column(Integer, primary_key=True, index=True)
    uuid = Column(Integer)
    data = Column(String)

class Attachments(Base):
    __tablename__ = 'attachments'

    attachment_id = Column(Integer, primary_key=True, index=True)
    uuid = Column(Integer)
    data = Column(String)

class Labels(Base):
    __tablename__ = 'labels'

    label_id = Column(Integer, primary_key=True, index=True)
    uuid = Column(Integer)
    data = Column(String)





