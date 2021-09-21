from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Blog, Category
# Create your views here.

class CategoryListView(TemplateView):
    template_name = "apps/blogs/category_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        list_all_category = Category.objects.all()
        context['list_all_category'] = list_all_category
        return context

class BlogListView(TemplateView):
    template_name = "apps/blogs/blog_list.html"

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
