from django.db import models

# Create your models here.
class Multiplication(models.Model):
    number = models.PositiveIntegerField()
    count = models.PositiveIntegerField(default=1)
