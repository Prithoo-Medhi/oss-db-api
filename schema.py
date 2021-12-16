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

    uuid: int
    start: datetime
    stop: datetime
    description: str
    name: str
    fullName: str
    status: str
    testCaseId: int
    historyId: str
    befores: List[Json]
    afters: List[Json]
    children: List[Json]
    attachments: List[Json]
    labels: List[Json]