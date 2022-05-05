from django.db import models
from django.db import models
from datetime import datetime


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
    id = models.AutoField(primary_key=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField (default= 0.0)
    order_date = models.DateTimeField(default = datetime.now())

