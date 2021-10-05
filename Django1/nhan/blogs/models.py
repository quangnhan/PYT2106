from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default="Empty")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name