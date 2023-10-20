from django.db import models


class Toy(models.Model):
    name = models.TextField()
    price = models.FloatField()
