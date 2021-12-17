'''
Contains all functional methods (non-OOP) for the module.
'''

import psycopg2 as pg
import datetime
from database import PGDATABASE, PGHOST, PGPORT, PGUSER, PGPASSWORD, DB_TYPE, SessionLocal
import models
from typing import List
import serializers
import json
from time import gmtime

def add_to_befores(befores, uuid):
    '''
    Explodes the 'befores' list and adds each item to a new row in the befores_table.
    '''
    db = SessionLocal()
    for item in list(befores):
        new_row = models.Befores(
            uuid = uuid,
            data = json.dumps(item)
        )
        db.add(new_row)
        db.commit()


def add_to_afters(afters, uuid):
    '''
    Explodes the 'afters' list and adds each item to a new row in the afters_table.
    '''
    db = SessionLocal()
    for item in list(afters):
        new_row = models.Afters(
            uuid = uuid,
            data = json.dumps(item)
        )
        db.add(new_row)
        db.commit()

def add_to_children(children, uuid):
    '''
    Explodes the 'children' list and adds each item to a new row in the children_table.
    '''
    db = SessionLocal()
    for item in list(children):
        new_row = models.Children(
            uuid = uuid,
            data = json.dumps(item)
        )
        db.add(new_row)
        db.commit()

def add_to_attachments(attachments, uuid):
    '''
    Explodes the 'attachments' list and adds each item to a new row in the attachments_table.
    '''
    db = SessionLocal()
    for item in list(attachments):
        new_row = models.Attachments(
            uuid = uuid,
            data = json.dumps(item)
        )
        db.add(new_row)
        db.commit()

def add_to_labels(labels, uuid):
    '''
    Explodes the 'labels' list and adds each item to a new row in the labels_table.
    '''
    db = SessionLocal()
    for item in list(labels):
        new_row = models.Labels(
            uuid = uuid,
            data = json.dumps(item)
        )
        db.add(new_row)
        db.commit()


def add_to_db(data: dict, db = SessionLocal()):
    """
    Adds a new entry to the MAIN table.
    """
    key_list = data.keys()

    uuid = data['uuid']
    start, stop, status = 0, 0, 'NA'
    description, name, fullName = 'NA', 'NA', 'NA'
    testCaseId, historyId = 'NA', 'NA'
    befores, afters, children = False, False, False
    attachments, labels = False, False

    if 'start' in key_list:
        # Because the start times is in milliseconds, we need to divide by 1000.
        start_stamp = data['start']/1000
        print('\nstart: ')
        print(start_stamp)
        start = datetime.datetime.fromtimestamp(start_stamp).strftime('%Y-%m-%d %H:%M:%S')

    if 'stop' in key_list:
        # Because the stop time is in milliseconds, we need to divide by 1000.
        stop_stamp = data['stop']/1000
        print('\nstop: ')
        print(stop_stamp)
        stop = datetime.datetime.fromtimestamp(stop_stamp).strftime('%Y-%m-%d %H:%M:%S')

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
    entry_list = []
    entries = db.query(models.Results).all()
    for entry in entries:
        entry_list.append(serializers.resultmodel_to_resultchema(entry))
    return entry_list

if __name__ == "__main__":
    # TODO: Add test execution.
    pass