from django.urls import path
from rest_framework import routers 
from rest_framework.routers import SimpleRouter
from .views import ProductAPIView, ProductAPIDetail, ProductAPIViewset, BlogAPIViewset

# urlpatterns = [
#     path('', ProductAPIView.as_view()),
#     path('<int:pk>', ProductAPIDetail.as_view()),
# ]

router = SimpleRouter()

router.register('product', ProductAPIViewset, basename='products')
router.register('blog', BlogAPIViewset, basename='blogs')

urlpatterns = router.urls