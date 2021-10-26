from django.shortcuts import render
from rest_framework import permissions
from products.models import Product, Blog
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework import viewsets, permissions
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
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

class TestApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        data = {
            "method" : "Get",
            "name" : "Nathan",
            "age" : "26",
            "language" : "English",
        }
        return Response(data)

    def post(self, request):
        print(request.data)
        data = {
            "method" : "POST"
        }
        return Response(data)