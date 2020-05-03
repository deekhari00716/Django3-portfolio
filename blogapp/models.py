from django.db import models

class Inside(models.Model):

    title = models.CharField(max_length = 100)
    text = models.TextField()

# Create your models here.
