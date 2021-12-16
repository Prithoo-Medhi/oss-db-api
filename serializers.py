from database import SessionLocal
import models
import schema

def capmodel_to_capschema(model: models.Results, before: models.Befores, after: models.Afters, children: models.Children, attachments: models.Attachments, labels: models.Labels):
    """
    Converts a Capabilities model to a Capabilities schema.
    """
    # body = {key : model.__dict__[key] for key in model.__dict__.keys() if not key.startswith('_')}

    db = SessionLocal()

    if model.befores:
        before_model = db.query(before).filter(models.Befores.uuid == model.uuid).all()
    else:
        before_model = []

    if model.afters:
        after_model = db.query(after).filter(models.Afters.uuid == model.uuid).all()
    else:
        after_model = []

    if model.children:
        children_model = db.query(children).filter(models.Children.uuid == model.uuid).all()
    else:
        children_model = []

    if model.attachments:
        attachments_model = db.query(attachments).filter(models.Attachments.uuid == model.uuid).all()
    else:
        attachments_model = []

    if model.labels:
        labels_model = db.query(labels).filter(models.Labels.uuid == model.uuid).all()
    else:
        labels_model = []

    body = schema.Input_Tests(
        uuid=model.uuid,
        start=model.start,
        stop=model.stop,
        description=model.description,
        name=model.name,
        fullName=model.fullName,
        status=model.status,
        testCaseId=model.testCaseId,
        historyId=model.historyId,
        befores=before_model,
        afters=after_model,
        children=children_model,
        attachments=attachments_model,
        labels=labels_model
    )

    return body