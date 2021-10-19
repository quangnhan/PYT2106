from django.shortcuts import render
from products.models import Product
from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer
# Create your views here.

class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer