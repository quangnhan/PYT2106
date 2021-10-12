from django.db import models
from buyers.models import Buyer
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
