from umongo import fields,Document
# from imdbapp.models import BaseDocument
from imdbapp import instance

@instance.register
class Movie(Document):
    name = fields.StringField(required=True)
    director = fields.StringField(required=True)
    categories = fields.ListField(fields.StringField())
    imdb_score = fields.FloatField()
    popularity_99 = fields.FloatField()


    def __str__(self):
        return f"{self.name} : {self.director}"
    
    def __repr__(self):
        return f"<{self.name} : {self.director}>"
