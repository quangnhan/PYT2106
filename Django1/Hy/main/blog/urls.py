from django.urls import path
from .views import BlogListView,blog_create,BlogCreateView,CategoryListView,BlogbyCategoryView
urlpatterns = [

    path('',BlogListView.as_view(), name="blog_list"),
    path('create', BlogCreateView.as_view(), name="blog_create"),

    path('post_create', blog_create,name="blog_post_create"),
    path('category', CategoryListView.as_view(), name="category_list"),
    path("blog_by_category",BlogbyCategoryView.as_view(),name="blog_by_cate")
]