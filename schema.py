from pydantic import BaseModel, Json
import datetime
from typing import List

class Input_Tests(BaseModel):
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