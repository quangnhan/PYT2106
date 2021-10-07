from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Blog, Category
# Create your views here.

class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name = "apps/blogs/category_list.html"
    context_object_name = 'list_all_category'
    permission_required = ('blogs.view_category',)

    def handle_no_permission(self):
        return redirect(reverse('home'))

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

class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    template_name = "apps/blogs/blog_create.html"
    fields = ['name', 'description', 'category']
    permission_required = ('blogs.add_category',)

    def get_success_url(self, **kwargs):      
        return reverse_lazy('blog_detail', args = (self.object.id,))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        return redirect(reverse('home'))
        
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