from django.db import models

# Create your models here.

class Diary(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    date = models.DateField()
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default="default.jpg",upload_to="diary_images/")
