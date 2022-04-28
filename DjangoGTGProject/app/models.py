from django.db import models
from django.db import models
from enum import Enum


class Drink (models.Model):
    TYPES = (
        ('COFFEE', 'coffee'),
        ('TEA', 'tea'),
        ('JUICE', 'juice'),
    )

    SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
    )
 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50) 
    type = models.CharField(max_length=10, choices = TYPES , default='COFFEE')
    size = models.CharField(max_length=10, choices = SIZES , default='LARGE')
    price = models.DecimalField (max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Order (models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.IntegerField()
