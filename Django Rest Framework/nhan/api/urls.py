from django.urls import path 
from .views import ProductAPIView, ProductAPIDetail

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('<int:pk>', ProductAPIDetail.as_view()),
]