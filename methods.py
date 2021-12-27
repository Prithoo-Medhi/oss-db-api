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


def add_to_befores(befores: List[any], uuid):
    '''
    Explodes the 'befores' list and adds each item to a new row in the befores_table.
    '''
    db = SessionLocal()
    for item in list(befores):
        new_row = models.Befores(
            uuid=uuid,
            data=json.dumps(item)
        )
        db.add(new_row)
        db.commit()


def add_to_afters(afters: List[any], uuid):
    '''
    Explodes the 'afters' list and adds each item to a new row in the afters_table.
    '''
    db = SessionLocal()
    for item in list(afters):
        new_row = models.Afters(
            uuid=uuid,
            data=json.dumps(item)
        )
        db.add(new_row)
        db.commit()


def add_to_children(children: List[any], uuid):
    '''
    Explodes the 'children' list and adds each item to a new row in the children_table.
    '''
    db = SessionLocal()
    for item in list(children):
        new_row = models.Children(
            uuid=uuid,
            data=json.dumps(item)
        )
        db.add(new_row)
        db.commit()


def add_to_attachments(attachments: List[any], uuid):
    '''
    Explodes the 'attachments' list and adds each item to a new row in the attachments_table.
    '''
    db = SessionLocal()
    for attachment in attachments:
        print(f"attachment: {attachment}")
        new_row = models.Attachments(
            uuid=uuid,
            data=json.dumps(attachment)
        )
        db.add(new_row)
        db.commit()


def add_to_labels(labels: List[any], uuid):
    '''
    Explodes the 'labels' list and adds each item to a new row in the labels_table.
    '''
    db = SessionLocal()
    for label in labels:
        print(f"label: {label}")
        new_row = models.Labels(
            uuid=uuid,
            data=json.dumps(label)
        )
        db.add(new_row)
        db.commit()


def write_to_config(line: str, db=SessionLocal()):
    '''
    Writes to a row in the test-configuration file.
    '''
    new_row = models.TextConfig(
        data=line
    )

    db.add(new_row)
    db.commit()


def add_to_db(data: dict, db=SessionLocal()):
    '''
    Adds a new entry to the 'results' table.
    '''

    # Initializing with default values.
    uuid = data['uuid']
    filename = data['filename']
    start, stop, status = 0, 0, ''
    description, name, fullName = '', '', ''
    testCaseId, historyId = '', ''
    befores, afters, children = False, False, False
    attachments, labels = False, False

    key_list = data.keys()

    # If a key is found in the dictionary, pull the corresponding value.

    if 'start' in key_list:
        # Because the start time is in milliseconds, we need to divide by 1000.
        start_stamp = data['start']/1000
        start = datetime.datetime.fromtimestamp(
            start_stamp).strftime('%Y-%m-%d %H:%M:%S.%f')

    if 'stop' in key_list:
        # Because the stop time is in milliseconds, we need to divide by 1000.
        stop_stamp = data['stop']/1000
        stop = datetime.datetime.fromtimestamp(
            stop_stamp).strftime('%Y-%m-%d %H:%M:%S.%f')

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

    # Array type Columns.
    if 'befores' in key_list:
        befores = True
        # print(f"\nBefores for {data['uuid']}: {data['befores']}")
        add_to_befores(data['befores'], data['uuid'])

    if 'afters' in key_list:
        afters = True
        # print(f"\nAfters for {data['uuid']}: {data['afters']}")
        add_to_afters(data['afters'], data['uuid'])

    if 'children' in key_list:
        children = True
        # print(f"\nChildren for {data['uuid']}: {data['children']}")
        add_to_children(data['children'], data['uuid'])

    if 'attachments' in key_list:
        attachments = True
        # print(f"\nAttachments for {data['uuid']}: {data['attachments']}")
        add_to_attachments(data['attachments'], data['uuid'])

    if 'labels' in key_list:
        labels = True
        # print(f"\nLabels for {data['uuid']}: {data['labels']}")
        add_to_labels(data['labels'], data['uuid'])

    # Committing to the 'results' table.
    new_entry = models.Results(
        uuid=data['uuid'],
        filename=filename,
        start=start,
        stop=stop,
        description=description,
        name=name,
        fullName=fullName,
        status=status,
        testCaseId=testCaseId,
        historyId=historyId,
        # Array of booleans if Array exists
        befores=befores,
        afters=afters,
        children=children,
        attachments=attachments,
        labels=labels
    )

    db.add(new_entry)
    db.commit()

def retrieve_from_db(db=SessionLocal()):
    '''
    Retrieves all rows from the 'results' table.
    '''
    entry_list = []
    entries = db.query(models.Results).all()
    # print(entries)

    for entry in entries:
        entry_list.append(serializers.resultmodel_to_resultchema(entry))

    return entry_list


if __name__ == "__main__":
    # TODO: Add test execution.
    pass
