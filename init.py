'''
Initializes the program; maybe a name-change is in order.
'''

import models
from database import engine
import os


BASE_PATH = os.getcwd()


models.Base.metadata.create_all(bind=engine)
