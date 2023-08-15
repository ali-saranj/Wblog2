from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    discretion = models.CharField(max_length=500)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.title