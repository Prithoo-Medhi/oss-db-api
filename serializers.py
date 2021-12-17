'''
Contains psuedo-serializers for the system.
'''
from database import SessionLocal
import models

def model_to_dict(model: any):
    """
    Converts a model to a dictionary.
    """
    body = {key : model.__dict__[key] for key in model.__dict__.keys() if not key.endswith('_id')}
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

    if model.befores:
        before_objects = db.query(models.Befores).filter(models.Befores.uuid == model.uuid).all()
        for item in before_objects:
            before_model.append(item.data)

    if model.afters:
        after_objects = db.query(models.Afters).filter(models.Afters.uuid == model.uuid).all()
        for item in after_objects:
            after_model.append(item.data)

    if model.children:
        children_objects = db.query(models.Children).filter(models.Children.uuid == model.uuid).all()
        for item in children_objects:
            children_model.append(item.data)

    if model.attachments:
        attachments_objects = db.query(models.Attachments).filter(models.Attachments.uuid == model.uuid).all()
        for item in attachments_objects:
            attachments_model.append(item.data)
    
    if model.labels:
        labels_objects = db.query(models.Labels).filter(models.Labels.uuid == model.uuid).all()
        for item in labels_objects:
            labels_model.append(item.data)

    body = {
        'uuid': model.uuid,
        'start': model.start,
        'stop': model.stop,
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