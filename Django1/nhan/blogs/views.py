from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog, Category
# Create your views here.

class CategoryListView(ListView):
    template_name = "apps/blogs/category_list.html"
    model = Category
    context_object_name = 'list_all_category'

class BlogListView(ListView):
    template_name = "apps/blogs/blog_list.html"
    model = Blog

    def get_context_data(self, *args, **kwargs):
        # Get data
        category_id = self.request.GET.get('category_id', None)
        context = super().get_context_data(*args, **kwargs)

        # Get list blog by category
        list_all_blog = Blog.objects.filter(category__id=category_id) 
        context['list_all_blog'] = list_all_blog
        return context

class BlogCreateView(TemplateView):
    template_name = "apps/blogs/blog_create.html"

def blog_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Blog.objects.create(name=name)
        return HttpResponse(f"Create blog {name} success")

class BlogDetailView(DetailView):
    template_name = "apps/blogs/blog_detail.html"
    model = Blog
