from django.urls import path 
from .views import blog_create, BlockListView

urlpatterns = [
    path('', BlockListView.as_view(), name="blog_list"),
    path('create', blog_create, name="blog_create"),
]