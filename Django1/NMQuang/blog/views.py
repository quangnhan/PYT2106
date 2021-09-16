from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Blog


class BlogListView(TemplateView):
    template_name = "apps/blog/blog_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        list_all_blog = Blog.objects.all()
        context['list_all_blog'] = list_all_blog
        return context

class BlogCreateView(TemplateView):
    template_name = "apps/blog/blog_create.html"

def blog_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Blog.objects.create(name=name)
        return HttpResponse(f"Create blog {name} success")
