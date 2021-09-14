from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog_list(request):
    if request.method == 'GET':
        list_all_blog = [
            {'id': 1, 'name': 'name1'},
            {'id': 2, 'name': 'name2'},
        ]
        data = {
            'list_all_blog': list_all_blog
        }
        return render(request, 'apps/blogs/blog_list.html',data)
    elif request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f"Create blog {name} success")