
from marshmallow import Schema, ValidationError, fields, validate, validates_schema


class Movie(Schema):
    name = NonEmptyStringField(required=True)
    director = NonEmptyStringField(required=True)
    categories = fields.List(fields.String(),required=True,validate=validate.Length(min=1))
    imdb_score = fields.Float(required=True)
    popularity_99 = fields.Float(required=True)