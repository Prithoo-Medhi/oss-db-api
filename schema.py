'''
Contains the definitions for all the pydantic-schemas to be used as serializers.
'''

from pydantic import BaseModel, Json
import datetime
from typing import List

class Results(BaseModel):
    '''
    Schema to serialize the Results model.
    '''

    uuid: any
    
    start: any
    stop: any
    description: any
    name: any
    fullName: any
    status: any
    testCaseId: any
    historyId: any
    befores: any
    afters: any
    children: any
    attachments: any
    labels: any