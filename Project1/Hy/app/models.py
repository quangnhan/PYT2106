from django.db import models
from django.conf import settings
from django import forms
import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta():
        db_table = 'tb_Category'

        def __str__(self):
            return self.name
            
class Product(models.Model):
    name = models.CharField(max_length=100)
    imageUrl = models.ImageField(upload_to='images', null=False, default=None)
    price_start = models.CharField(max_length=100)
    date_post = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(auto_now_add=False, auto_now=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta():
        db_table = 'tb_Product'

        def __str__(self):
            return self.name
            return self.imageUrl
            return self.price_start
            return self.date_post
            return self.date_end
            return self.category
            return self.user_post
class UserBuyProduct(models.Model):
    Price_Final = models.CharField(max_length=100,null=False, default=None)
    date_buy = models.DateTimeField(auto_now_add=True)
    user_buy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, default=None)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta():
        db_table = 'tb_UserBuyProduct'

        def __str__(self):
            return self.Price_Final
            return self.date_buy
            return self.user_buy
            return self.product
