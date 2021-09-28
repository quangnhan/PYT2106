from django.urls import path
from .views import index,ProductListView,ProductCreateView,ProductUpdateView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('', index.as_view(), name="homepage"),
    path('product',ProductListView.as_view(),name="product_list"),
    path('create', ProductCreateView.as_view(), name="product_create"),
    path('<int:pk>/update', ProductUpdateView.as_view(), name="product_update"),
    # login user 
    path('login/',auth_views.LoginView.as_view(template_name="apps/users/login.html"), name="login"),
    # log out
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)