from django.urls import path
from .views import BlogCreateView, blog_create, BlogListView, BlogDetailView, CategoryListView, BlogCreateV2View

urlpatterns = [
    path('category', CategoryListView.as_view(), name="category_list"),

    path('', BlogListView.as_view(), name="blog_list"),
    path('create', BlogCreateView.as_view(), name="blog_create"),
    path('create/v2', BlogCreateV2View.as_view(), name="blog_create_v2"),
    path('post_create', blog_create, name="blog_post_create"),
    path('<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
]
