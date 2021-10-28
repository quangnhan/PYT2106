from django.db import models
from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.

class ListBlogView(generics.ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer