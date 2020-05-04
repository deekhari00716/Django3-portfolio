from django.db import models

class Inside(models.Model):

    title = models.CharField(max_length = 100)
    text = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
