from django.urls import path
from . import views

urlpatterns = [
    path('noi dung', views.home_page),
    path('About!', views.about_page),
]