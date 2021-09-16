from django.urls import path
from .views import BlogListView,blog_create
urlpatterns = [
    path('',BlogListView.as_view(), name="blog_list"),
    #path('create', blog_create,name="blog_create"),

]