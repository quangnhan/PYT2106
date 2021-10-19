from django.urls import path
from rest_framework import routers 
from rest_framework.routers import SimpleRouter
from .views import ProductAPIView, ProductAPIDetail, ProductAPIViewset

# urlpatterns = [
#     path('', ProductAPIView.as_view()),
#     path('<int:pk>', ProductAPIDetail.as_view()),
# ]

router = SimpleRouter()

router.register('', ProductAPIViewset, basename='products')

urlpatterns = router.urls