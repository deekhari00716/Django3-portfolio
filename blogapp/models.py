from django.db import models

class Inside(models.Model):

    title = models.CharField(max_length = 100)
    text = models.TextField()
    date = models.DateField(auto_now=True)

# Create your models here.
