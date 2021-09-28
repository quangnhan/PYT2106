from django.db import models
from django.shortcuts import render, resolve_url
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Blog, Category
# Create your views here.

class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "apps/blogs/category_list.html"
    model = Category
    context_object_name = 'list_all_category'

class BlogListView(LoginRequiredMixin, ListView):
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

class BlogDetailView(LoginRequiredMixin, DetailView):
    template_name = "apps/blogs/blog_detail.html"
    model = Blog

class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = "apps/blogs/blog_create.html"
    model = Blog
    fields = ['name', 'description', 'category']

    def get_success_url(self, **kwargs):      
        return reverse_lazy('blog_detail', args = (self.object.id,))

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "apps/blogs/blog_update.html"
    model = Blog
    fields = ['name', 'description', 'category']

    def get_success_url(self, **kwargs):      
        return reverse_lazy('blog_detail', args = (self.object.id,))

class BlogDeteleView(LoginRequiredMixin, DeleteView):
    template_name = "apps/blogs/blog_delete.html"
    model = Blog
    success_url = reverse_lazy('category_list')

# ==============================================================================================
class BlogCreateV2View(TemplateView):
    template_name = "apps/blogs/blog_create_2.html"

def blog_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Blog.objects.create(name=name)
        return HttpResponse(f"Create blog {name} success")