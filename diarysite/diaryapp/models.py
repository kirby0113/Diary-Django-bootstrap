from django.db import models

# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    author = models.CharField(max_length=100)
    content = models.TextField()
