from django.db import models
from rest_framework import serializers
from products.models import Product, Blog

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('name', 'author')