from umongo import fields,Document

class BaseDocument(Document):
    modified = fields.DateTimeField()
    active = fields.BooleanField(default=True)

    meta = {'abstract': True}


