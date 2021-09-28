from django.urls import path
from .views import BlogListView, BlogCreateView, CategoryListView, BlogDetailView, BlogDeteleView, BlogUpdateView  #, blog_create


urlpatterns = [
    path('category', CategoryListView.as_view(), name="category_list"),

    path('', BlogListView.as_view(), name="blog_list"),
    path('create', BlogCreateView.as_view(), name="blog_create"),
    path('<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
    path('<int:pk>/update', BlogUpdateView.as_view(), name="blog_update"),
    path('<int:pk>/delete', BlogDeteleView.as_view(), name="blog_delete"),
    # path('post_create', blog_create, name="blog_post_create"),
]
