from django.urls import path 
from .views import BlogCreateView, blog_create, BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_list"),
    path('create', BlogCreateView.as_view(), name="blog_create"),
    path('post_create', blog_create, name="blog_post_create"),
]