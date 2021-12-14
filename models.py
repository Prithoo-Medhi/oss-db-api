'''
Contains the models for the database.
'''
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql.schema import ForeignKey
from database import Base


class Caps(Base):
    '''
    Model/Table to contain capabilities for each test-case:
    '''
    
    __tablename__ = 'cap_matrix'

    cap_id = Column(Integer, primary_key=True, index=True)
    device_type = Column(String)
    device_name = Column(String)
    browser_name = Column(String)
    screen_resolution = Column(String)
    bs_run_mode = Column(String)
    is_device_real = Column(Boolean)
    network_type = Column(String)
