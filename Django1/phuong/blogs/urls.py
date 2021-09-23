from django.urls import path 
from .views import blog_create, BlogListView, BlogCreateView, CategoryListView, BlogDetailView

urlpatterns = [
    path('category', CategoryListView.as_view, name="category_List"),

    path('', BlogListView.as_view(), name="blog_list"),
    path('create', BlogCreateView.as_view(), name="blog_create"),
    path('post_create', blog_create, name="blog_post_create"),
    path('<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
]