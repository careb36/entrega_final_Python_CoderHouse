from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Stores(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    schedules = models.CharField(max_length=100)

class Opinions(models.Model):
    name = models.CharField(max_length=50)
    calification = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    comment = models.CharField(max_length=150)
