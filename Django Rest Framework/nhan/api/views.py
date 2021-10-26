from django.shortcuts import render
from rest_framework import permissions
from products.models import Product, Blog
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .serializers import ProductSerializer, BlogSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAPIViewset(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BlogAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer