'''
Contains the models for the database.
'''
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, JSON
from database import Base
import json


class Results(Base):
    '''
    Model/Table to contain results for each test-case:
    '''
    __tablename__ = 'results'

    uuid = Column(String, primary_key=True, index=True)
    filename = Column(String)
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
    '''
    Model to contain all the before processes for each test-report.
    '''
    __tablename__ = 'befores'

    before_id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String)
    data = Column(String)


class Afters(Base):
    '''
    Model to contain all the after processes for each test-report.
    '''
    __tablename__ = 'afters'

    after_id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String)
    data = Column(String)

class Children(Base):
    '''
    Model to contain all the child processes for each test-report.
    '''
    __tablename__ = 'children'

    children_id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String)
    data = Column(String)

class Attachments(Base):
    '''
    Model to contain all the attachment processes for each test-report.
    '''
    __tablename__ = 'attachments'

    attachment_id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String)
    data = Column(String)

class Labels(Base):
    '''
    Model to contain all the labels and tags for each test-report.
    '''
    __tablename__ = 'labels'

    label_id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String)
    data = Column(String)

class TextConfig(Base):
    '''
    Model to contain the parsed text-lines from the test-configuration '.txt' files.
    '''

    __tablename__ = 'txt_config'

    conf_id = Column(Integer, primary_key=True, index=True)
    data = Column(String)





