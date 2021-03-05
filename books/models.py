from django.db import models
from uuid import uuid4

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    description = models.TextField()
    year = models.IntegerField()
    pages = models.IntegerField()

 