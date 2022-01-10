from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class SnsModel(models.Model):
    title = CharField(max_length=100)
    content = TextField(max_length=1000)
    contributer = CharField(max_length=100)
    good = IntegerField()
    read = IntegerField()
    readtext = TextField()