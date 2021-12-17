'''
Contains psuedo-serializers for the system.
'''
from database import SessionLocal
import models
# import schema

def resultmodel_to_resultchema(model: models.Results) -> dict:
    """
    Converts a Results model to a Results schema.
    """
    # body = {key : model.__dict__[key] for key in model.__dict__.keys() if not key.startswith('_')}

    db = SessionLocal()

    if model.befores:
        before_model = db.query(models.Befores).filter(models.Befores.uuid == model.uuid).all()
    else:
        before_model = []

    if model.afters:
        after_model = db.query(models.Afters).filter(models.Afters.uuid == model.uuid).all()
    else:
        after_model = []

    if model.children:
        children_model = db.query(models.Children).filter(models.Children.uuid == model.uuid).all()
    else:
        children_model = []

    if model.attachments:
        attachments_model = db.query(models.Attachments).filter(models.Attachments.uuid == model.uuid).all()
    else:
        attachments_model = []

    if model.labels:
        labels_model = db.query(models.Labels).filter(models.Labels.uuid == model.uuid).all()
    else:
        labels_model = []

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