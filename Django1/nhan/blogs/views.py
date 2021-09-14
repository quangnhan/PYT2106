from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class BlogListView(TemplateView):
    template_name = "apps/blogs/blog_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        list_all_blog = [
            {'id': 1, 'name': 'name11'},
            {'id': 2, 'name': 'name22'},
        ]
        context['list_all_blog'] = list_all_blog
        return context

def blog_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f"Create blog {name} success")
