'''
Contains all functional methods (non-OOP) for the module.
'''

import psycopg2 as pg
from datetime import datetime
from init import BASE_PATH
from database import PGDATABASE, PGHOST, PGPORT, PGUSER, PGPASSWORD, DB_TYPE
import models
from database import SessionLocal
from typing import List
import serializers

def add_to_befores(befores, uuid:int):
    '''
    Explodes the 'befores' list and adds each item to a new row in the befores_table.
    '''
    db = SessionLocal()
    for item in list(befores):
        new_row = models.Befores(
            uuid = uuid,
            data = str(item)
        )
        db.add(new_row)
        db.commit()


def add_to_afters(afters, uuid:int):
    '''
    Explodes the 'afters' list and adds each item to a new row in the afters_table.
    '''
    db = SessionLocal()
    for item in list(afters):
        new_row = models.Afters(
            uuid = uuid,
            data = str(item)
        )
        db.add(new_row)
        db.commit()

def add_to_children(children, uuid:int):
    '''
    Explodes the 'children' list and adds each item to a new row in the children_table.
    '''
    db = SessionLocal()
    for item in list(children):
        new_row = models.Children(
            uuid = uuid,
            data = str(item)
        )
        db.add(new_row)
        db.commit()

def add_to_attachments(attachments, uuid:int):
    '''
    Explodes the 'attachments' list and adds each item to a new row in the attachments_table.
    '''
    db = SessionLocal()
    for item in list(attachments):
        new_row = models.Attachments(
            uuid = uuid,
            data = str(item)
        )
        db.add(new_row)
        db.commit()

def add_to_labels(labels, uuid:int):
    '''
    Explodes the 'labels' list and adds each item to a new row in the labels_table.
    '''
    db = SessionLocal()
    for item in list(labels):
        new_row = models.Labels(
            uuid = uuid,
            data = str(item)
        )
        db.add(new_row)
        db.commit()


def add_to_db(data: dict, db = SessionLocal()):
    """
    Adds a new entry to the MAIN table.
    """
    key_list = data.keys()

    uuid = int(data['uuid'])
    start, stop, status = None, None, 'NA'
    description, name, fullName = 'NA', 'NA', 'NA'
    testCaseId, historyId = 'NA', 'NA'

    if 'start' in key_list:
        start = data['start']

    if 'stop' in key_list:
        stop = data['stop']

    if 'description' in key_list:
        description = data['description']

    if 'name' in key_list:
        name = data['name']

    if 'fullName' in key_list:
        fullName = data['fullName']

    if 'status' in key_list:
        status = data['status']

    if 'testCaseId' in key_list:
        testCaseId = data['testCaseId']

    if 'historyId' in key_list:
        historyId = data['historyId']

    if 'befores' in key_list:
        befores = True
        add_to_befores(data['befores'], data['uuid'])

    if 'afters' in key_list:
        afters = True
        add_to_afters(data['afters'], data['uuid'])

    if 'children' in key_list:
        children = True
        add_to_children(data['children'], data['uuid'])

    if 'attachments' in key_list:
        attachments = True
        add_to_children(data['attachments'], data['uuid'])

    if 'labels' in key_list:
        labels = True
        add_to_children(data['labels'], data['uuid'])



    new_entry = models.Results(
        uuid = uuid,
        start = start,
        stop = stop,
        description = description,
        name = name,
        fullName = fullName,
        status = status,
        testCaseId = testCaseId,
        historyId = historyId,
        # Array of booleans
        befores = befores,
        afters = afters,
        children = children,
        attachments = attachments,
        labels = labels
    )

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    print(new_entry)

def retrieve_from_db(db = SessionLocal()):
    """
    Retrieves all entries from the table.
    """
    # TODO: Add a retrieve method.

if __name__ == "__main__":
    # TODO: Add test execution.
    pass