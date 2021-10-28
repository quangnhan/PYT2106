from django.shortcuts import render
from django.http.response import HttpResponse
from common.blogs import Blog

# Create your views here.

def blog_list(request):
    blog = Blog()
    list_blog = blog.get_all_blog()
    return HttpResponse(list_blog)