from django.urls import path
from . import views

urlpatterns = [
    path('ooooooooooooooo', views.home_page), #trong dau nhay don la ten duong dan url
    path('About', views.about_page),
]
