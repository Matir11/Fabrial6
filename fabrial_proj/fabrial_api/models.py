from django.db import models

# Create your models here.
class Chore(models.Model):
    id: models.CharField(max_length=25)
    title: models.CharField(max_length=50)
    value: models.FloatField
    done: models.BooleanField