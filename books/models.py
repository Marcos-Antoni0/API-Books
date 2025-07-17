from django.db import models
from uuid import uuid4

# Create your models here.

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    release_date = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
