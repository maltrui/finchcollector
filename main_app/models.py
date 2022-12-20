from django.db import models

class Finch(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    age = models.IntegerField()
