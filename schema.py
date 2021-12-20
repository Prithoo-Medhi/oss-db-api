'''
Contains the definitions for all the pydantic-schemas to be used as serializers.
'''

from pydantic import BaseModel
import datetime
from typing import List


class Results(BaseModel):
    '''
    Schema to serialize the Results model.
    '''
    uuid: str
    start: datetime.datetime
    stop: datetime.datetime
    description: str
    name: str
    fullName: str
    status: str
    testCaseId: str
    historyId: str
    befores: List[dict]
    afters: List[dict]
    children: List[dict]
    attachments: List[dict]
    labels: List[dict]
