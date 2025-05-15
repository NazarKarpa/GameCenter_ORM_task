from django.db import models
from django.db.models import ManyToManyField


class Game(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    rating =  models.DecimalField(max_digits=10, decimal_places=2)
    genre = ManyToManyField('Genre')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name