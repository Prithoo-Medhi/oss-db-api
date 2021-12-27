'''
Contains psuedo-serializers for the system.
'''
from database import SessionLocal
import models
import json
from datetime import datetime


def model_to_dict(model: any):
    """
    Converts a model to a dictionary.
    """
    body = {key: model.__dict__[key]
            for key in model.__dict__.keys() if not key.endswith('_id')}
    return body


def resultmodel_to_resultchema(model: models.Results) -> dict:
    """
    Converts a Results model to a Results schema.
    """
    db = SessionLocal()

    before_model = []
    after_model = []
    children_model = []
    attachments_model = []
    labels_model = []

    if model.befores == True:
        before_objects = db.query(models.Befores).filter(models.Befores.uuid == model.uuid).all()
        # print(f"Befores for {model.uuid}: {before_objects}")
        for item in before_objects:
            before_model.append(json.loads(item.data))

    if model.afters == True:
        after_objects = db.query(models.Afters).filter(models.Afters.uuid == model.uuid).all()
        # print(f"Afters for {model.uuid}: {after_objects}")
        for item in after_objects:
            after_model.append(json.loads(item.data))

    if model.children == True:
        children_objects = db.query(models.Children).filter(models.Children.uuid == model.uuid).all()
        # print(f"Children for {model.uuid}: {children_objects}")
        for item in children_objects:
            children_model.append(json.loads(item.data))

    if model.attachments == True:
        attachments_objects = db.query(models.Attachments).filter(models.Attachments.uuid == model.uuid).all()
        # print(f"Attachments for {model.uuid}: {attachments_objects}")
        for item in attachments_objects:
            attachments_model.append(json.loads(item.data))

    if model.labels == True:
        labels_objects = db.query(models.Labels).filter(models.Labels.uuid == model.uuid).all()
        # print(f"Labels for {model.uuid}: {labels_objects}")
        for item in labels_objects:
            labels_model.append(json.loads(item.data))

    # Translates the retrieved model.attribute-value pairs to key-value pairs in a dictionary.
    body = {
        'uuid': model.uuid,
        'filename': model.filename,
        'start': int(float(datetime.timestamp(model.start))*1000),
        'stop': int(float(datetime.timestamp(model.stop))*1000),
        'description': model.description,
        'name': model.name,
        'fullName': model.fullName,
        'status': model.status,
        'testCaseId': model.testCaseId,
        'historyId': model.historyId,
        'befores': before_model,
        'afters': after_model,
        'children': children_model,
        'attachments': attachments_model,
        'labels': labels_model
    }

    return body
