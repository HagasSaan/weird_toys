from django.db import models


class Customer(models.Model):
    login = models.TextField()
    password = models.TextField()


class Toy(models.Model):
    name = models.TextField(default='')
    details = models.TextField(default='')
    material = models.TextField(default='')  # TODO: probably enum

    colors = models.TextField(default='')  # TODO: should be array
    out_of_stock = models.BooleanField(default=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Card(models.Model):
    name = models.TextField()
    card_number = models.CharField(max_length=20)
    expiry_date = models.DateField()
    cvv = models.SmallIntegerField()


class Order(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    country = models.TextField()
    city = models.TextField()
    address = models.TextField()

